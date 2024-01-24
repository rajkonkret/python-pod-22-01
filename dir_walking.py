import os

# os do dziłań z plikami i katalogami

for root, dirs, files in os.walk("../python-pod-22-01"):
    for file in files:
        if file == 'main.py':
            file_path = os.path.join(root, file)
            print(file_path)

for root, dirs, files in os.walk(".."):
    abs_root = os.path.abspath(root)
    # print(abs_root)
    if dirs:
        print('directories')
        for dir_ in dirs:
            print(dir_)
    if files:  # if files==True
        print("Files:")
        for filename in files:
            print(filename)
