#encoding:utf-8
with open('words.txt', 'r') as f:
    dict={}
    for line in f:
        line = line.strip('\n')
        line=line.rstrip()
        line=line.lower()
        words=line.split(" ")
        for word in words:
            if word in dict.keys():
                dict[word]=dict[word]+1
            else:
                dict[word]=1
    print("-----------")
    for k, v in dict.items():
        print("{}:{}".format(v,k))
    print("-----------")