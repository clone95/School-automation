import os
import sys

def ensure_dir_exists(directory):
    if not os.path.exists(directory):
        print(f'Making folder: {directory}')
        os.makedirs(directory)

input_folder = './School-automation/Ragazzi'
remove = ['\t', '\t\t', '']
root_name = './School-automation/Materiale Ordinato'

ensure_dir_exists(root_name)

for age in os.listdir(input_folder):
    ensure_dir_exists(f'{root_name}/{age}')

    for room in os.listdir(f'{input_folder}/{age}'):
        
        room_name = room.split('.')[0]
        
        with open(f'{input_folder}/{age}/{room}', 'r') as file:
            kids = file.read().split('\n')
            kids = [x.replace('\t', '') for x in kids if x.strip() not in remove]
        
        for kid in kids:
            ensure_dir_exists(f'{root_name}/{age}/{room_name}/{kid}/Immagini')
            ensure_dir_exists(f'{root_name}/{age}/{room_name}/{kid}/Video')
            ensure_dir_exists(f'{root_name}/{age}/{room_name}/{kid}/Documenti')
            ensure_dir_exists(f'{root_name}/{age}/{room_name}/{kid}/Altro')





