from sys import argv
from os import system

system('git add .')
system('git commit -m "{}"'.format(argv[1]))
system('git push')

print('Pushed with commit message:', argv[1])
