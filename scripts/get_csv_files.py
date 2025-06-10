import os

for file in os.listdir('data/'):
    if file.endswith('.csv'):
        print(file)