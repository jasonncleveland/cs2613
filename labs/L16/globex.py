#!/usr/bin/python3
import glob
import os

new_dir = os.path.expanduser('~/cs2613/labs/test')

python_files_for = []

for file in glob.glob('*.py'):
    python_files_for.append(os.path.join(new_dir, file))

python_files_comp = [os.path.join(new_dir, file) for file in glob.glob('*.py')]

python_files_map = map(lambda file: os.path.join(new_dir, file), glob.glob('*.py'))
