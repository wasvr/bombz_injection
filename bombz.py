import os
import random
import time
from colorama import Fore, init, deinit
import shutil

init()

path = input(Fore.LIGHTRED_EX + '\nEnter the path for the bombz_injection: ')
howmany = int(input('\nHow many folders: '))

deinit()

if not os.path.exists(path):
    print('Directory does not exist.')
    quit()

try:
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            shutil.rmtree(os.path.join(root, name))
except FileNotFoundError:
    print('error')

start_time = time.perf_counter()

for i in range(howmany):
    init()
    foldnames = random.randint(0, 10000000000000000000000)
    folder_path = os.path.join(path, str(foldnames))
    os.mkdir(folder_path)
    print(folder_path + '\n')
    file_name = f"{foldnames}.txt"
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w') as file:
        txtz = str(foldnames)
        file.write('HACKED FOLDER BY BOMBZ_INJECTION EZ, GOODBYE ENCODED DIR ' + txtz)
    print(Fore.LIGHTGREEN_EX + f'Folder made - {foldnames} // {i} -\n')

end_time = time.perf_counter()
print(f'\nFinished bomb in {end_time}ms/seconds')

deinit()