#!/usr/bin/env python3
import fileinput
import shutil 
import subprocess

fortune = subprocess.run(["fortune", "fortunes"], capture_output=True)

shutil.copyfile('template.html', 'index.html')

with fileinput.FileInput("index.html", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("{{}}", fortune.stdout.decode('utf-8')), end='')