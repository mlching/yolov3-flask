from ultralytics import YOLO
import cv2
import os
import mod
import csv
import time

# Load YOLO model
model_name = "yolov8x"
model = YOLO(f"./weights/{model_name}.pt")

# Define input and output folders
input = "testing2"
input_folder = f'/Users/martinlee/{input}'  # Change this to the folder containing your input images
output_folder = f'./output_images/{model_name}'  # Change this to the desired output folder for processed images

# Get a list of image file names in the folder
image_names = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', 'JPG'))]

# Define a function to extract the numeric part from the filename
def extract_number(filename):
    try:
        return int(filename[len("photo"):filename.index(".")])
    except ValueError:
        return float('inf')  # Return a very large value for filenames that don't match the pattern

# Sort the image file names based on the extracted numbers
sorted_image_names = sorted(image_names, key=extract_number)
print(sorted_image_names)


# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Define output CSV file
output_csv = f'./data/{model_name}_{input}_results.csv'  # Change this to the desired output CSV file name

# Initialize CSV writer
csv_file = open(output_csv, 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Image', 'Object', 'Distance', 'Location', 'Time', 'Confidence'])

# Process images in the input folder
for image_filename in sorted_image_names:
    if image_filename.endswith(('.jpg', '.jpeg', '.png', 'JPG')):
        image_path = os.path.join(input_folder, image_filename)
        frame = cv2.imread(image_path)

        start = time.time()
        prediction = model(frame, conf=0.5)[0]
        end = time.time() - start
        data = prediction.boxes.data.tolist()
        lists = []
        for i in data:
            text, lis = mod.give_direction(i[:4], prediction.names[i[5]], frame)
            lis["confidence"] = i[4]
            lists.append(lis)

        for lis in lists:
            if lis['movable']:
                cv2.rectangle(frame, tuple(lis['bbox'][:2]), tuple(lis['bbox'][2:]), (0, 0, 255), 1)
            else:
                cv2.rectangle(frame, tuple(lis['bbox'][:2]), tuple(lis['bbox'][2:]), (0, 255, 0), 1)
            cv2.putText(frame, f"Object:{lis['object']}, Distance:{lis['distance']}, Location:{lis['location']}",
                        tuple([lis['bbox'][0], lis['bbox'][1]]), 0, 1, (0, 0, 0), 2)
            csv_writer.writerow([image_filename, lis['object'], lis['distance'], lis['location'], end, lis['confidence']])

            # Save the processed image with bounding boxes in the output folder
        output_image_path = os.path.join(output_folder, f"processed_{image_filename}")
        cv2.imwrite(output_image_path, frame)

        # Write data to CSV


# Close the CSV file
csv_file.close()
