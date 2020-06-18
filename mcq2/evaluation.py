#encoding:utf-8
import math

rele = {
    'd1':1,
    'd2':3,
    'd3':1,
    'd4':2,
    'd5':1,
    'd9':1,
    'd10':1,
    'd11':2,
    'd12':3,
    'd16':2,
    'd17':2,
    'd20':2,
}

non_rele = ['d0']

ret = ['d17','d4','d15','d8','d1','d13','d3','d5','d14','d18']


def pre():
    global rele
    global non_rele
    global ret

    length_ret = len(ret)
    rel_ret = 0
    for key in rele.keys():
        if key in ret:
            rel_ret = rel_ret +1

    return rel_ret/length_ret

def rec():
    global rele
    global non_rele
    global ret

    length_rel = len(rele)
    rel_ret = 0
    for key in rele.keys():
        if key in ret:
            rel_ret = rel_ret + 1

    return rel_ret/length_rel

def p_at_n(n):
    global rele
    global non_rele
    global ret

    index =0
    rele_number = 0
    while index<n and index<len(ret):
        doc_check =ret[index]
        if doc_check in rele.keys():
            rele_number =rele_number +1
        index = index +1

    return rele_number/n


def p_at_r():
    global rele
    global non_rele
    global ret
    length_rel = len(rele)
    return p_at_n(length_rel)


def map():
    global rele
    global non_rele
    global ret

    index = 0
    total_precison = 0
    rel_ret = 0
    while index < len(ret):
        if ret[index] in rele.keys():
            total_precison = total_precison + p_at_n(index+1)
        index = index +1

    return total_precison/len(rele)


def bpref():
    global rele
    global non_rele
    global ret
    total_B= 0
    rel_ret = 0
    index = 0
    non_rele_found = 0
    while index < len(ret):
        if ret[index] in rele.keys():
            rel_ret = rel_ret + 1
            if non_rele_found < len(rele):
                total_B = total_B + (1-non_rele_found/len(rele))
            else:
                total_B = total_B
        elif ret[index] in non_rele:
            non_rele_found = non_rele_found +1

        index = index +1

    return total_B/len(rele)


def NDCG_at_n(n):
    global rele
    global non_rele
    global ret

    all_dcoument = []
    sort_rele = sorted(rele.items(), key=lambda x: x[1], reverse=True)
    for doc in sort_rele:
        all_dcoument.append({'id':doc[0], 'rele':doc[1]})
    for doc in non_rele:
        all_dcoument.append({'id':doc, 'rele':0})
    returned_list = []
    for doc in ret:
        relevance = 0
        if doc in rele.keys():
            relevance = rele[doc]
        returned_list.append({'id':doc, 'rele':relevance})
    index = 0
    while index < len(returned_list):
        if index == 0:
            doc = returned_list[index]
            doc['dcg'] = doc['rele']
            returned_list[index] =doc
        else:
            doc = returned_list[index]
            doc_past = returned_list[index-1]
            doc['dcg'] = (doc['rele']/math.log(index+1,2) )+doc_past['dcg']
            returned_list[index] = doc
        index = index+1

    index = 0
    while index < len(all_dcoument):
        if index == 0:
            doc = all_dcoument[index]
            doc['dcg'] = doc['rele']
            all_dcoument[index] =doc
        else:
            doc = all_dcoument[index]
            doc_past = all_dcoument[index-1]
            doc['dcg'] = (doc['rele']/math.log(index+1,2) )+doc_past['dcg']
            all_dcoument[index] = doc
        index = index+1
    doc_at_n = returned_list[n-1]
    answer_at_n = all_dcoument[n-1]
    return doc_at_n['dcg']/answer_at_n['dcg']


def organize():
    feedback = {}
    index = 0
    while index < len(ret):
        if ret[index] in rele.keys():
            feedback[ret[index]] = "R"
        elif ret[index] in non_rele:
            feedback[ret[index]] = "N"
        else:
            feedback[ret[index]] = "U"
        index = index +1
    step = 1
    for key, value in feedback.items():
        print('rank'+str(step)+' '+key+":"+value)
        step +=1
    print()


if __name__ == '__main__':
    organize()
    print('Precision: '+str(round(pre(), 4)))
    print('Recall: '+str(round(rec(), 4)))
    print('P@10: '+str(round(p_at_n(10), 4)))
    print('RPrecision: '+str(round(p_at_r(), 4)))
    print('MAP: '+str(round(map(), 4)))
    print('bpref: '+str(round(bpref(), 4)))
    print('NDCG at 10: '+str(round(NDCG_at_n(5), 4)))
