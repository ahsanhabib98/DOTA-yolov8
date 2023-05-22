import os

def file_format(file_path, classes):
    with open(file_path, 'r') as file:
        content = file.readlines()
    
    modified_content = []
    for c, line in enumerate(content):
        columns = line.split()
        if columns:
            column = columns[-2]
            columns = columns[:-2]
            modified_line = str(classes[column]) + ' ' + ' '.join(columns) + '\n'
            modified_content.append(modified_line)

    with open(file_path, 'w') as file:
        file.writelines(modified_content)
    
classes = {'small-vehicle':0, 'large-vehicle':1, 'plane':2, 'storage-tank':3, 'ship':4, 'harbor':5, 'ground-track-field':6, 'soccer-ball-field':7, 'tennis-court':8, 'swimming-pool':9, 'baseball-diamond':10, 'roundabout':11, 'basketball-court':12, 'bridge':13, 'helicopter':14, 'container-crane':15}

dirs = ['datasets/train/labels', 'datasets/val/labels']
for directory in dirs:
    for filename in os.listdir(directory):
        file_path = directory+ '/' +filename
        file_format(file_path, classes)
