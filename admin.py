import json


def data_from_txt(path):
    f = open(path, 'r')
    lines = f.read().split('\n')
    f.close()

    data = []
    for i in range(0, 10, 4):
        data.append({
            'question': lines[i],
            'answers': [
                lines[i + 1],
                lines[i + 2],
                lines[i + 3]
            ]
        })

    return data


def data_to_json(data, path):
    f = open(path, 'w')
    json.dump(data, f)
    f.close()


data_to_json(data_from_txt('src/txt/test.txt'), 'src/json/data_test.json')
