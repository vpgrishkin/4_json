import json
import sys
import os

DEFAULT_FILE_NAME = 'default.json'
DEFAULT_INDENT = 4


def load_data(file_path):
    with open(file_path, 'rt') as json_file:
        json_string = json_file.read()
        parsed_string = json.loads(json_string)
        return parsed_string

def pretty_print_json(data):
    return json.dumps(data, indent=DEFAULT_INDENT, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Нет параметров для запуска! Файл по умолчанию: {}'.format(DEFAULT_FILE_NAME))
        work_file = DEFAULT_FILE_NAME
    else:
        work_file = sys.argv[1]
        if os.path.isfile(work_file):
            print('Рабочий файл: {}'.format(work_file))

    if not os.path.exists(work_file):
        print('Файл {} не существует'.format(work_file))
        sys.exit(1)

    data_from_json = load_data(work_file)
    print(pretty_print_json(data_from_json))