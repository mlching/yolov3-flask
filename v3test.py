import cv2
import os
import csv
import time
import requests

input = "testing2"
input_folder = f"/Users/martinlee/{input}"
output_folder = f"./output_images/yolov3"

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
output_csv = f'./data/yolov3_{input}_results.csv'  # Change this to the desired output CSV file name

# Initialize CSV writer
csv_file = open(output_csv, 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Image', 'Object', 'Distance', 'Location', 'Time', 'Confidence'])

# Process images in the input folder
for image_filename in sorted_image_names:
    if image_filename.endswith(('.jpg', '.jpeg', '.png', 'JPG')):
        image_path = os.path.join(input_folder, image_filename)
        frame = cv2.imread(image_path)

        resp = requests.post("http://127.0.0.1:5000/", files={'file': open(f'{input_folder}/{image_filename}', 'rb')})
        print(image_filename)
        print(resp.json())
        try:
            lists = resp.json()["lists"]
            height, width, _ = frame.shape
            line1_pos = int(width * 20 / 100)
            line2_pos = int(width * 80 / 100)
            time = resp.json()["time"]

            # Draw lines on the frame
            green = (0, 255, 0)
            black = (0, 0, 0)
            red = (0, 0, 255)

            # drawing bounding boxes
            for lis in lists:
                if lis['movable']:
                    cv2.rectangle(frame, tuple(lis['bbox'][0]), tuple(lis['bbox'][1]), red, 1)
                else:
                    cv2.rectangle(frame, tuple(lis['bbox'][0]), tuple(lis['bbox'][1]), green, 1)
                cv2.putText(frame, f"Object:{lis['object']}, Distance:{lis['distance']}, Location:{lis['location']}",
                            tuple(lis['bbox'][0]), 0, 1, black, 2)
                csv_writer.writerow([image_filename, lis['object'], lis['distance'], lis['location'], time, lis['confidence']])
        except KeyError:
            continue

        # Save the processed image with bounding boxes in the output folder
        output_image_path = os.path.join(output_folder, f"processed_{image_filename}")
        cv2.imwrite(output_image_path, frame)

        # Write data to CSV


# Close the CSV file
csv_file.close()