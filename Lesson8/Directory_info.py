'''Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и
все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
- Для дочерних объектов указывайте родительскую директорию.
- Для каждого объекта укажите файл это или директория.
- Для файлов сохраните его размер в байтах,
а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
'''

from os import listdir, chdir, getcwd
from os.path import isdir, isfile, getsize
import json
import csv
import pickle

def getsize_directory(directory: str) -> int:
    result = 0
    chdir(directory)
    for item in listdir():
        if isdir(item):
            result += getsize_directory(item)
        else:
            result += getsize(item)
    chdir('../')
    return result


def get_directory_info() -> dict:
    result = {}
    for item in listdir():
        if isdir(item):
            chdir(item)
            items_in_dir = get_directory_info()
            chdir('../')
            result.update({item: {'type': 'directory',
                                  'size': getsize_directory(item),
                                  'parent': getcwd(),
                                  'files': items_in_dir}})
        if isfile(item):
            result.update({item: {'type': 'file',
                                  'size': getsize(item),
                                  'parent': getcwd()}})
    return result


def save_json(file_name: str, data: dict):
    if not file_name.endswith('.json'):
        file_name.replace('.', '')
        file_name += '.json'
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False)


def save_csv(file_name: str, data: dict):
    if not file_name.endswith('.csv'):
        file_name.replace('.', '')
        file_name += '.csv'
    with open(file_name, 'w', encoding='utf-8') as f:
        csv_write = csv.DictWriter(f, fieldnames=['item', 'value'])
        all_data = []
        for key, value in data.items():
            all_data.append(f'{key} {value}')
        csv_write.writerows(all_data)


def save_pickle(file_name: str, data: dict):
    if not file_name.endswith('.pickle'):
        file_name.replace('.', '')
        file_name += '.pickle'
    with open(file_name, 'wb') as f:
        pickle.dump(data, f)


if __name__ == '__main__':
    data = get_directory_info()
    save_json('file', data)
    # save_csv('file', data)
    save_pickle('file', data)

