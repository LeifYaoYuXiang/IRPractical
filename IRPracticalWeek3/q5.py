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
    sorted_words = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    for sorted_word in sorted_words:
       print(sorted_word)
    print("-----------")