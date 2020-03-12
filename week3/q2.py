# encoding:utf-8
with open('words.txt', 'r') as f:
    for line in f:
        line = line.strip('\n')
        line=line.rstrip()
        line = "("+line+")"
        line = line.replace(" ", ")(")
        print(line, end="\n")
