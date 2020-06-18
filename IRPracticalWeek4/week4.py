# encoding:utf-8
word = {}


def read_in_line():
    with open('index.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            sequence = line.split(" ")
            term = sequence[0]
            index = []
            for i in range(len(sequence)):
                if i != 0:
                    index.append(int(sequence[i]))
            word[term] = index


def merge_and(a,b):
    token_a = word[a]
    token_b = word[b]
    answer = []
    index_a = 0
    index_b = 0
    while index_a != len(token_a) and index_b != len(token_b):
        if token_a[index_a] == token_b[index_b]:
            answer.append(token_a[index_a])
            index_a = index_a+1
            index_b = index_b+1
        elif token_a[index_a] < token_b[index_b]:
            index_a = index_a + 1
        else:
            index_b = index_b + 1
    return answer


def merge_or(a, b):
    token_a = word[a]
    token_b = word[b]
    answer = []
    index_a = 0
    index_b = 0
    while index_a != len(token_a) or index_b != len(token_b):
        if index_a == len(token_a):
            answer.append(token_b[index_b:])
            return answer
        elif index_b == len(token_b):
            answer.append(token_a[index_a:])
            return answer
        else:
            if token_a[index_a] == token_b[index_b]:
                answer.append(token_a[index_a])
                index_a = index_a + 1
                index_b = index_b + 1
            elif token_a[index_a] < token_b[index_b]:
                answer.append(token_a[index_a])
                index_a = index_a + 1
            else:
                answer.append(token_b[index_b])
                index_b = index_b + 1
    return answer


def search():
    prompt = input('Search What?')
    if prompt.find(' AND ') != -1:
        end=prompt.find(' AND ')
        word1 = prompt[0:end]
        word2 = prompt[end+5:]
        return merge_and(word1,word2)
    elif prompt.find(' OR ') != -1:
        end = prompt.find(' OR ')
        word1 = prompt[0:end]
        word2 = prompt[end + 4:]
        print(word1+'-----'+word2)
        return merge_and(word1, word2)
    else:
        return word[prompt]


def merge_not(a,b):
    token_a = word[a]
    token_b = word[b]
    answer = []
    index_a = 0
    index_b = 0
    while index_a != len(token_a) or index_b != len(token_b):
        if index_a == len(token_a):
            return answer
        elif index_b == len(token_b):
            answer.append(token_a[index_a:])
            return answer
        else:
            if token_a[index_a] == token_b[index_b]:
                index_a = index_a + 1
                index_b = index_b + 1
            elif token_a[index_a] < token_b[index_b]:
                answer.append(token_a[index_a])
                index_a = index_a + 1
            else:
                index_b = index_b + 1
    return answer


read_in_line()
print(('(HH)AND((JJ)OR(JJ OR MM))').replace("AND","+").replace("OR","-"))

