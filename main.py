import os
import re

try:
    img_max_width = int(input())
    print(f'using user specified value: {img_max_width}')
except:
    img_max_width = 600
    print('using default value: 600')

current_dir = os.getcwd()

try:
    os.remove('merged.html')
except FileNotFoundError:
    print("Merged.html not found so can't be deleted.")

with open("merged.html", 'a') as merged:
    for root, dirs, files in os.walk(current_dir):
        if root == current_dir:
            for file in files:
                if file.endswith('.html') and file != 'merged.html':
                    print(file)
                    with open(file, 'r') as opened:
                        for line in opened:
                            if '/graphics/' in line:
                                line = re.sub(r'/graphics/.+assets/', '../graphics/', line)
                                line = re.sub(r'file:///[0123456789]+/graphics/', '../graphics/', line)
                                line = re.sub(r'/graphics/[0123456789]+/graphics/image/', '../graphics/', line)
                                line = re.sub(r'/graphics/[0123456789]+/graphics/Images/', '../graphics/', line)

                                line = line.replace('img src=',
                                                    f'img style="max-width: {img_max_width}px; height: auto" src=')

                            merged.write(line)
