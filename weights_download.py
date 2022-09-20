import os
import convert_weights

file_list = ['checkpoint', 'yolov3_weights.tf.data-00000-of-00001', 'yolov3_weights.tf.index']

list1 = []

for file in file_list:
    list1.append(os.path.isfile(file))

if all(list1):
    print('Weight exists. Conversion not needed')
else:
    print('Converting .weights file to tf file')
    convert_weights.main()
    os.remove('yolov3.weights')
