#encoding:utf-8
#机器返回值
import math

result = []
#标准答案
judgement = []


def read_from_file():
    with open('results.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            line = line.split(" ")
            result.append({"qid":line[0],'docid':line[2], 'rank':line[3] })
    with open('qrels.txt', 'r') as f:
        for line in f:
            line = line.rstrip()
            line = line.split(" ")
            judgement.append({'qid':line[0],'docid':line[2], 'relevance':line[3]})


def precision():
    ret = len(result)
    relret = 0
    for result_item in result:
        docID = result_item['docid']
        for judgement_item in judgement:
            if judgement_item['docid'] == docID and int(judgement_item['relevance']) != 0:
                relret=relret+1
    return relret/ret


def recall():
    rel = 0
    for judgement_item in judgement:
        if int(judgement_item['relevance']) !=0:
            rel=rel+1
    relret = 0
    for result_item in result:
        docID = result_item['docid']
        for judgement_item in judgement:
            if judgement_item['docid'] == docID and int(judgement_item['relevance']) != 0:
                relret=relret+1
    return relret/rel


def precision_at_n(n):
    index = 0
    relret = 0
    while index < n:
        result_item = result[index]
        docID = result_item['docid']
        for judgement_item in judgement:
            if judgement_item['docid'] == docID and int(judgement_item['relevance']) != 0:
                relret = relret + 1
        index=index+1
    return relret/n


def r_precision():
    rel = 0
    for judgement_item in judgement:
        if int(judgement_item['relevance']) != 0:
            rel = rel + 1
    return precision_at_n(rel)


def map():
    rel = 0
    sum_pre=0
    for judgement_item in judgement:
        if int(judgement_item['relevance']) != 0:
            rel = rel + 1
    index = 0
    while index < len(result):
        result_item =result[index]
        docID = result_item['docid']
        for judgement_item in judgement:
            if judgement_item['docid'] == docID and int(judgement_item['relevance']) != 0:
                sum_pre=sum_pre+precision_at_n(index+1)
        index=index+1

    return sum_pre/rel


def bpref():
    rel=0
    non_rel=0
    total_weight=0
    for judgement_item in judgement:
        if int(judgement_item['relevance']) != 0:
            rel = rel + 1

    for result_item in result:
        docID=result_item['docid']
        for judgement_item in judgement:
            if judgement_item['docid'] == docID:
            #judged
                weight = 0
                if int(judgement_item['relevance']) == 0:
                    non_rel=non_rel+1
                else:
                    if non_rel<rel:
                        weight = 1-(non_rel/rel)
                    else:
                        weight = 0
                total_weight=total_weight+weight

    return total_weight/rel


def ndcg_at_n(n):
    return_result = []
    relevance = 0
    for result_item in result:
        # docID = result_item['docid']
        # for judgement_item in judgement:
        #     if judgement_item['docid'] == docID:
        #         relevance = judgement_item['relevance']
        #         return_result.append({'docid':docID,'gain':relevance,'rank':result_item['rank']})
        index = 0
        docID = result_item['docid']
        while index < len(judgement):
            judgement_item = judgement[index]
            if judgement_item['docid'] == docID:
                relevance = judgement_item['relevance']
                return_result.append({'docid':docID,'gain':relevance,'rank':result_item['rank']})
                break
            index=index+1

        if index == len(judgement):
            judgement_item = judgement[index-1]
            if judgement_item['docid'] != docID:
                return_result.append({'docid': docID, 'gain': 0, 'rank': result_item['rank']})
        index = 0


    index = 0
    while index < len(return_result):
        result_item = return_result[index]
        if index == 0:
            result_item['dcg'] = int(result_item['gain'])
        else:
            before_result_item = return_result[index - 1]
            result_item['dcg'] = float(result_item['gain'])/math.log2(int(result_item['rank'])) + float(before_result_item['dcg'])
        index = index + 1
    print(return_result)
    term_at_n = return_result[n-1]
    dcg_at_n = term_at_n['dcg']

    index = 0
    normalized_result =[]
    while index <n:
        judgement_item=judgement[index]
        normalized_result.append({'docID':judgement_item['docid'], 'ig':int(judgement_item['relevance'])})
        index=index+1
    normalized_result = sorted(normalized_result, key=lambda e: e.__getitem__('ig'),reverse=True)

    print(normalized_result)
    index = 0
    while index < len(normalized_result):
        judgement_item = normalized_result[index]
        if index == 0:
            judgement_item['idcg'] = int(judgement_item['ig'])
        else:
            befor_judgement_item = normalized_result[index - 1]
            judgement_item['idcg'] = float(judgement_item['ig']) / math.log2(index + 1) + float(befor_judgement_item['idcg'])
        index = index + 1

    print(normalized_result)

    term_at_n = normalized_result[n-1]


    idcg_at_n = term_at_n['idcg']
    return float(dcg_at_n)/float(idcg_at_n)



if __name__ == "__main__":
    read_from_file()
    # print(precision())
    # print(recall())
    # print(precision_at_n(10))
    # print(r_precision())
    # print(map())
    # print(bpref())
    print(ndcg_at_n(10))