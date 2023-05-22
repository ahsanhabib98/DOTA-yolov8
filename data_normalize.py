from PIL import Image
import os

def data_normalize(file_path):
    normalized_labels = []
    
    with open(file_path, 'r') as file:
        content = file.readlines()
        
    image_path = file_path.split('.')[0]+'.png'
    image_path = image_path.split('labels')
    image_path = image_path[0] + 'images' + image_path[1]
    image = Image.open(image_path)
    image_width, image_height = image.size
    
    modified_content = []
    for c, line in enumerate(content):
        values = line.strip().split()
        class_index = int(values[0])
        coordinates = [float(coord) for coord in values[1:]]

        normalized_coordinates = []
        for i in range(0, len(coordinates), 2):
            x = coordinates[i] / image_width
            y = coordinates[i + 1] / image_height
            normalized_coordinates.extend([x, y])
    
        normalized_labels.append((class_index, normalized_coordinates))
    
    modified_content = []
    for label in normalized_labels:
        class_index, coordinates = label
        modified_line = f"{class_index} {' '.join(map(str, coordinates))}\n"
        modified_content.append(modified_line)
    
    with open(file_path, 'w') as file:
        file.writelines(modified_content)
    

dirs = ['datasets/train/labels', 'datasets/val/labels']
for directory in dirs:
    for filename in os.listdir(directory):
        file_path = directory+ '/' +filename
        data_normalize(file_path)
