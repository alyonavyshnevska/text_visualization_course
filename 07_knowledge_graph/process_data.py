import pandas as pd
import time
import zipfile
from collections import defaultdict
import json


def make_small_csv(input_file, out_file, in_columns):
    start_time = time.time()
    df = pd.read_csv(input_file, sep='\t')
    df_columns = df.columns
    df = df[in_columns]
    print("Converting the file took --- %s seconds ---" % (time.time() - start_time))
    return df

def extract_zip():
    zip_ref = zipfile.ZipFile('data/fma_metadata.zip', 'r')
    zip_ref.extractall('fma_metadata')
    zip_ref.close()


def make_butterfly_data():
    df = make_small_csv('data/butterfly.csv', 'data/butterfly_small.csv', ['kingdom', 'phylum', 'class', 'order', 'family', 'genus', 'species'])
    return df

def use_butterfly_data():
    df = pd.read_csv('data/butterfly_small.csv')
    return df

def save_to_json(file_name, nested_dict, save=False):
    if save == True:
        with open(file_name, "w") as write_file:
            json.dump(nested_dict, write_file)


def create_dict_from_csv():
    df = pd.read_csv('data/genres.csv')
    df = df[['genre_id', 'title', 'parent']]

    genres = zip(df.genre_id, df.title)
    genres_dict = dict()
    for id, genre in genres:
        genres_dict[str(id)] = genre

    #(node, its parent)
    parents_zip = zip(df.title, df.parent)
    parents_zip = list(parents_zip)

    # Find parents = the nodes whose parent is 0
    top_parents = set([title for (title,parent) in parents_zip if parent == 0])

    #generate children dictionary
    children_dict = defaultdict(list)
    for title, parent in parents_zip:
        #exclude top parents
        if parent != 0:
            children_dict[genres_dict[str(parent)]].append(title)

    nested_dict = dict()
    nested_dict['name'] = 'Music Genres'
    nested_dict['children'] = []

    for parent in top_parents:
        d = {'name' : parent, 'children' : [{'name': child} for child in children_dict[parent]]}
        nested_dict['children'].append(d)

    return nested_dict

#change to True to create a new file
nested_dict = create_dict_from_csv()
save_to_json('music.json', nested_dict, save=False)
