import os
import sys
from difflib import SequenceMatcher
from gen_class_folder import *

def get_kid_work(staging_folder, kid_folder):
    for file in os.listdir(staging_folder):
        kid_name = kid_folder.split('/')[-1].lower()
        kid_name = kid_name.split(' ')[:2]
        right_kid_name = (' ').join(kid_name)
        kid_name.reverse()
        inverted_kid_name = (' ').join(kid_name)

        kid_file_name = file.split(' ')[:2]
        ext = file.split('.')[-1]
        kid_file_name = (' ').join(kid_file_name).lower()
        similarity = SequenceMatcher(None, right_kid_name, kid_file_name).ratio()
        inverted_similarity = SequenceMatcher(None, inverted_kid_name, kid_file_name).ratio()

        if similarity > 0.9 or inverted_similarity >0.9:
            file_cat = [key for key in categories if ext.lower() in categories[key]][0]
            os.rename(f'{staging_folder}/{file}', f'{kid_folder}/{file_cat}/{file}')

        

categories = {
                    'Immagini': ['jpg', 'jpeg', 'png', 'PNG'],
                    'Video':['mov', 'mp4'],
                    'Documenti':['pdf', 'txt', 'doc', 'docx', 'odft'],
                }                  

clean_folder = './School-automation/Materiale Ordinato'
staging_folder = './School-automation/Raccoglitore'

ensure_dir_exists(clean_folder)

for age in os.listdir(clean_folder):
    for room in os.listdir(f'{clean_folder}/{age}'):
        for kid in os.listdir(f'{clean_folder}/{age}/{room}'):
            
            kid_folder = f'{clean_folder}/{age}/{room}/{kid}'
            get_kid_work(staging_folder, kid_folder)




