import json


def data_from_txt(path):
    f = open(path, 'r', encoding='utf-8')
    lines = f.read().split('\n')
    f.close()

    data = []
    for i in range(0, 10, 4):
        data.append({
            'question': lines[i],
            'answer': [
                lines[i + 1],
                lines[i + 2],
                lines[i + 3]
            ]
        })

    return data


def data_to_json(data, path):
    f = open(path, 'w', encoding='utf-8')
    json.dump(data, f)
    f.close()


def data_from_json(path):
    f = open(path, 'r', encoding='utf-8')
    data = json.load(f)
    return data
