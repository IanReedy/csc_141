filename = '/Users/ianreedy/Desktop/Python/chap10/learning_python.txt'

with open(filename) as file:
    for line in file:
        print(line.replace("Python", "C").strip())