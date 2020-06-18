#encoding:utf-8
import porter
import time

stopwords = []
text = {}


def read_in_line():
    with open('stopwords.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            stopwords.append(line)

    with open('npl-doc-text.txt', 'r') as f:
        id = '1'
        for line in f:
            line = line.rstrip().strip(b'\x00'.decode())
            if line.isdigit():
                id = line
                text[id]=""
                last_id=str(int(line)-1)
                if last_id != '0':
                    text[last_id] = str(text[last_id]).lstrip(" ").rstrip("    /")
            else:
                text[id]=text[id]+" "+line
        text[id]=str(text[id]).lstrip(" ").rstrip("    /")


def stem():
    p = porter.PorterStemmer()
    text_index = 0
    while text_index < len(text):
        term = {}
        text_origin = text[str(text_index+1)]
        term_origin = str(text_origin).split(" ")

        for word in term_origin:
            if word != " " and word!="":
                word=p.stem(word)
                if word not in stopwords:
                    if word in term.keys():
                        term[word]=term[word]+1
                    else:
                        term[word]=1
        temp_term = {}
        for k, v in term.items():
            if v != 1:
                temp_term.update({k: v})
        text[str(text_index + 1)] = temp_term
        del temp_term
        text_index = text_index+1


def printStem():
    text_index = 0
    while text_index < len(text):
        single_text = text[str(text_index+1)]
        s = sorted(single_text.items(), key=lambda x: x[1],reverse=True)
        if len(s)>0:
            print(str(text_index + 1), end=":\n")
            print(s)
        text_index = text_index+1



if __name__ == '__main__':
    start_time = time.process_time()
    read_in_line()
    stem()
    printStem()
    end_time = time.process_time()
    print('Time is {} seconds'.format(end_time-start_time) )