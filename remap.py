import os
studio =  [{
      "id": 0,
      "name": "airplane"
    },
    {
      "id": 1,
      "name": "apple"
    },
    {
      "id": 2,
      "name": "backpack"
    },
    {
      "id": 3,
      "name": "banana"
    },
    {
      "id": 4,
      "name": "baseball bat"
    },
    {
      "id": 5,
      "name": "baseball glove"
    },
    {
      "id": 6,
      "name": "bear"
    },
    {
      "id": 7,
      "name": "bed"
    },
    {
      "id": 8,
      "name": "bench"
    },
    {
      "id": 9,
      "name": "bicycle"
    },
    {
      "id": 10,
      "name": "bird"
    },
    {
      "id": 11,
      "name": "boat"
    },
    {
      "id": 12,
      "name": "book"
    },
    {
      "id": 13,
      "name": "bottle"
    },
    {
      "id": 14,
      "name": "bowl"
    },
    {
      "id": 15,
      "name": "broccoli"
    },
    {
      "id": 16,
      "name": "bus"
    },
    {
      "id": 17,
      "name": "cake"
    },
    {
      "id": 18,
      "name": "car"
    },
    {
      "id": 19,
      "name": "carrot"
    },
    {
      "id": 20,
      "name": "cat"
    },
    {
      "id": 21,
      "name": "cell phone"
    },
    {
      "id": 22,
      "name": "chair"
    },
    {
      "id": 23,
      "name": "clock"
    },
    {
      "id": 24,
      "name": "couch"
    },
    {
      "id": 25,
      "name": "cow"
    },
    {
      "id": 26,
      "name": "cup"
    },
    {
      "id": 27,
      "name": "dining table"
    },
    {
      "id": 28,
      "name": "dog"
    },
    {
      "id": 29,
      "name": "donut"
    },
    {
      "id": 30,
      "name": "elephant"
    },
    {
      "id": 31,
      "name": "fire hydrant"
    },
    {
      "id": 32,
      "name": "fork"
    },
    {
      "id": 33,
      "name": "frisbee"
    },
    {
      "id": 34,
      "name": "giraffe"
    },
    {
      "id": 35,
      "name": "hair drier"
    },
    {
      "id": 36,
      "name": "handbag"
    },
    {
      "id": 37,
      "name": "horse"
    },
    {
      "id": 38,
      "name": "hot dog"
    },
    {
      "id": 39,
      "name": "keyboard"
    },
    {
      "id": 40,
      "name": "kite"
    },
    {
      "id": 41,
      "name": "knife"
    },
    {
      "id": 42,
      "name": "laptop"
    },
    {
      "id": 43,
      "name": "microwave"
    },
    {
      "id": 44,
      "name": "motorcycle"
    },
    {
      "id": 45,
      "name": "mouse"
    },
    {
      "id": 46,
      "name": "orange"
    },
    {
      "id": 47,
      "name": "oven"
    },
    {
      "id": 48,
      "name": "parking meter"
    },
    {
      "id": 49,
      "name": "person"
    },
    {
      "id": 50,
      "name": "pizza"
    },
    {
      "id": 51,
      "name": "potted plant"
    },
    {
      "id": 52,
      "name": "refrigerator"
    },
    {
      "id": 53,
      "name": "remote"
    },
    {
      "id": 54,
      "name": "sandwich"
    },
    {
      "id": 55,
      "name": "scissors"
    },
    {
      "id": 56,
      "name": "sheep"
    },
    {
      "id": 57,
      "name": "sink"
    },
    {
      "id": 58,
      "name": "skateboard"
    },
    {
      "id": 59,
      "name": "skis"
    },
    {
      "id": 60,
      "name": "snowboard"
    },
    {
      "id": 61,
      "name": "spoon"
    },
    {
      "id": 62,
      "name": "sports ball"
    },
    {
      "id": 63,
      "name": "stop sign"
    },
    {
      "id": 64,
      "name": "suitcase"
    },
    {
      "id": 65,
      "name": "surfboard"
    },
    {
      "id": 66,
      "name": "teddy bear"
    },
    {
      "id": 67,
      "name": "tennis racket"
    },
    {
      "id": 68,
      "name": "tie"
    },
    {
      "id": 69,
      "name": "toaster"
    },
    {
      "id": 70,
      "name": "toilet"
    },
    {
      "id": 71,
      "name": "toothbrush"
    },
    {
      "id": 72,
      "name": "traffic light"
    },
    {
      "id": 73,
      "name": "train"
    },
    {
      "id": 74,
      "name": "truck"
    },
    {
      "id": 75,
      "name": "tv"
    },
    {
      "id": 76,
      "name": "umbrella"
    },
    {
      "id": 77,
      "name": "vase"
    },
    {
      "id": 78,
      "name": "wine glass"
    },
    {
      "id": 79,
      "name": "zebra"
    }]

yolo = {"person": "0", "bicycle": "1", "car": "2", "motorcycle": "3", "airplane": "4", "bus": "5", "train": "6", "truck": "7", "boat": "8", "traffic light": "9", "fire hydrant": "10", "stop sign": "11", "parking meter": "12", "bench": "13", "bird": "14", "cat": "15", "dog": "16", "horse": "17", "sheep": "18", "cow": "19", "elephant": "20", "bear": "21", "zebra": "22", "giraffe": "23", "backpack": "24", "umbrella": "25", "handbag": "26", "tie": "27", "suitcase": "28", "frisbee": "29", "skis": "30", "snowboard": "31", "sports ball": "32", "kite": "33", "baseball bat": "34", "baseball glove": "35", "skateboard": "36", "surfboard": "37", "tennis racket": "38", "bottle": "39", "wine glass": "40", "cup": "41", "fork": "42", "knife": "43", "spoon": "44", "bowl": "45", "banana": "46", "apple": "47", "sandwich": "48", "orange": "49", "broccoli": "50", "carrot": "51", "hot dog": "52", "pizza": "53", "donut": "54", "cake": "55", "chair": "56", "couch": "57", "potted plant": "58", "bed": "59", "dining table": "60", "toilet": "61", "tv": "62", "laptop": "63", "mouse": "64", "remote": "65", "keyboard": "66", "cell phone": "67", "microwave": "68", "oven": "69", "toaster": "70", "sink": "71", "refrigerator": "72", "book": "73", "clock": "74", "vase": "75", "scissors": "76", "teddy bear": "77", "hair drier": "78", "toothbrush": "79"}

folder_path = "./labels"  # Replace with the path to your folder

def modify_first_value(file_path):
    with open(file_path, "r") as f:
        lines = f.readlines()

    with open(file_path, "w") as f:
        for line in lines:
            values = line.strip().split()
            if values:
                word = studio[int(values[0])]["name"]
                new_value = yolo[word]  # Modify the first value
                new_line = " ".join([new_value] + values[1:])
                f.write(new_line + "\n")

def process_txt_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)
            modify_first_value(file_path)
            print(f"Modified {filename}.")

if __name__ == "__main__":
    process_txt_files(folder_path)
    print("All files processed.")
