"""Data tools.

This module has tools to work with simple data.
"""
import json
import os


def data_from_txt(path):
    """Take data from text file"""
    f = open(path, 'r', encoding='utf-8')
    lines = f.read().split('\n')
    f.close()

    data = []
    for i in range(0, len(lines), 4):
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
    """Make a json file with data."""
    f = open(path, 'w', encoding='utf-8')
    json.dump(data, f)
    f.close()


def data_from_json(path):
    """Take data from json file."""
    f = open(path, 'r', encoding='utf-8')
    data = json.load(f)
    return data


def push_dest(dest, mes):
    """Push destination file to the online repository."""
    os.chdir(dest)

    os.system('git add .')
    os.system('git commit -m "{}"'.format(mes))
    os.system('git push')
