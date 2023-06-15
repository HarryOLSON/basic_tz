import os
import glob


class FilesManager:
    PATH = os.path.join(os.path.join(os.getcwd(), 'files_manager'), 'output')

    def get_files(self, file_type='dump'):
        return glob.glob(f'{self.PATH}/*.{file_type}')

    @staticmethod
    def get_file_data(file):
        data = {}
        with open(file, 'r') as file_data:
            for line in file_data:
                line = line.strip()
                if line:
                    line_split = line.split('\t')
                    if len(line_split) == 1:
                        line_split = line.split(':')
                    key, value = line_split
                    key = key.strip()
                    value = value.strip()
                    data[key] = value
        return data
