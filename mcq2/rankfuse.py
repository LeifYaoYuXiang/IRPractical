#encoding:utf-8

feedback ={
    '0':[1,'d9','d12','d15','d6','d3','d13','d10','d7','d5'],
    '1':[1,'d7','d4','d1','d10','d11','d3','d12','d5','d2','d0'],
    '2':[1,'d1','d11','d15','d8','d3','d2','d9']
}


def interleaving():
    fusion = []
    index = 0
    total_doc = 0
    length_engine = len(feedback)
    for value in feedback.values():
        total_doc = total_doc + len(value)
    while index < total_doc:
        eng = str(index % length_engine)
        eng_doc = feedback[eng]
        if eng_doc[0] < len(eng_doc):
            while eng_doc[0] < len(eng_doc) and eng_doc[eng_doc[0]] in fusion:
                eng_doc[0] = eng_doc[0] + 1
            if eng_doc[0] < len(eng_doc):
                step = eng_doc[0]
                doc = eng_doc[step]
                fusion.append(doc)
            eng_doc[0] = eng_doc[0] + 1
        index = index + 1

    return fusion


def borda():
    all_document = []

    index = 0
    while index < len(feedback):
        engine = feedback[str(index)]
        for doc in engine:
            if type(doc) == str and doc not in all_document:
                all_document.append(doc)
        index =index +1


    doc_credit = {}
    for doc in all_document:
        doc_credit[doc] = 0
    doc_number =len(all_document)

    index = 0
    offset = {}
    while index < len(feedback):
        engine = feedback[str(index)]
        offset[str(index)] = (doc_number-(len(engine)-1)+1)/2
        index = index + 1
    for doc in doc_credit.keys():
        index = 0
        score = 0
        while index <len(feedback):
            engine = feedback[str(index)]
            if doc in engine:
                pos = engine.index(doc)
                score = score + (doc_number-pos+1)
            else:
                score = score + offset[str(index)]
            index = index + 1
        doc_credit[doc] = score
    rank_doc = sorted(doc_credit.items(), key=lambda x: x[1], reverse=True)
    for key, value in rank_doc:
        print(key+': '+ str(round(value,4)))
    return rank_doc




def rrf():
    funsion = {}
    k= 60
    index = 0
    while index < len(feedback):
        engine = feedback[str(index)]
        step = 1
        while step < len(engine):
            doc  = engine[step]
            if doc in funsion.keys():
                funsion[doc] = funsion[doc] + 1/(k+step)
            else:
                funsion[doc] = 1/(k+step)
            step = step + 1
        index =index +1
    rank_doc = sorted(funsion.items(), key=lambda x: x[1], reverse=True)
    for key, value in rank_doc:
        print(key+': '+ str(round(value,4)))
    return rank_doc



if __name__ == '__main__':
    print('Interleaving: ')
    print(interleaving())
    print()
    print('borda: ')
    borda()
    print()
    print('RRF: ')
    rrf()



