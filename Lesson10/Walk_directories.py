from os import listdir, chdir, getcwd
from os.path import isdir, isfile, getsize
import json
import csv
import pickle


class Get_Directory_Info:
    def __init__(self, path: str = './'):
        self.result_dict = {}
        self.path = path

    def __getsize_directory(self, directory: str) -> int:
        result = 0
        chdir(directory)
        for item in listdir():
            if isdir(item):
                result += self.__getsize_directory(item)
            else:
                result += getsize(item)
        chdir('../')
        return result

    def __walk_process(self) -> dict:
        result = {}
        for item in listdir():
            if isdir(item):
                result.update({item: {'type': 'directory',
                                      'size': self.__getsize_directory(item),
                                      'parent': getcwd()}})
                chdir(item)
                result.update(self.__walk_process())
                chdir('../')
            if isfile(item):
                result.update({item: {'type': 'file',
                                      'size': getsize(item),
                                      'parent': getcwd()}})
        return result

    def walk_directory(self):
        start_dir = getcwd()
        chdir(self.path)
        self.result_dict.update(self.__walk_process())
        chdir(start_dir)

class Directory_Info_Saver:
    def __init__(self, directory_info: dict, file_name: str, file_format: str):
        self.file_format = file_format
        self.file_name = file_name
        self.directory_info = directory_info

    def save(self):
        if self.file_format == 'csv':
            if not self.file_name.endswith('.csv'):
                self.file_name.replace('.', '')
                self.file_name += '.csv'
            with open(self.file_name, 'w', encoding='utf-8') as f:
                csv_write = csv.DictWriter(f, fieldnames=['name', 'type', 'size', 'parent'])
                csv_write.writeheader()
                all_data = []
                for key, value in self.directory_info.items():
                    row = {'name': key}
                    row.update(value)
                    all_data.append(row)
                csv_write.writerows(all_data)
        elif self.file_format == 'json':
            if not self.file_name.endswith('.json'):
                self.file_name.replace('.', '')
                self.file_name += '.json'
            with open(self.file_name, 'w', encoding='utf-8') as f:
                json.dump(self.directory_info, f, ensure_ascii=False)
        elif self.file_format == 'pickle':
            if not self.file_name.endswith('.pickle'):
                self.file_name.replace('.', '')
                self.file_name += '.pickle'
            with open(self.file_name, 'wb') as f:
                pickle.dump(self.directory_info, f)


if __name__ == '__main__':
    dictionary = Get_Directory_Info('D:/GeekBrains/Python_Advanced/Lesson10')
    dictionary.walk_directory()
    saver = Directory_Info_Saver(dictionary.result_dict, 'file', 'json')
    saver.save()