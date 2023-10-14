from ultralytics import YOLO

model = YOLO('./runs/detect/train4/weights/best.pt')
#model.train(data='./dataset/data.yaml', epochs=50, imgsz=640, batch=8)
results = model.predict('test4.jpg', save=False, imgsz=640, conf=0.4, save_txt=True)
for result in results:
  print(result.boxes.data)
  data = result.boxes.data
  last_column_tensor = data[:, -1]

  # Convert the PyTorch tensor to a list of integers
  last_column_list = last_column_tensor.cpu().int().tolist()

  # Print the list of integers
  print(last_column_list)

import yaml

# Specify the path to your YAML file
yaml_file_path = 'class_names.yaml'  # Replace with your file path

# Read and parse the YAML file
with open(yaml_file_path, 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)

# Access the 'names' key from the parsed data
names = data['names']
print(names)
for column in last_column_list:
   print(names[column])