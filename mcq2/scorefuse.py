#encoding:utf-8
feedback ={
    '0': {'d51':9.0486,'d31':8.8005,'d70':7.1033,'d16':6.2594,'d22':5.1080,'d92':5.0407,'d39':3.8981,'d100':3.4933,'d4':2.9667,'d38':2.4860},
    # '1': {'d0':93.7531,'d1':90.7096,'d4':77.2629,'d6':58.2031,'d3':53.4187,'d11':45.0629,'d2':32.1287,'d14':26.5387,'d10':8.1426},
    # '2': {'d9':0.9595,'d8':0.4709,'d4':0.3829,'d7':0.3384,'d3':0.2777,'d13':0.1164,'d0':0.0806},
}
weight = {
    '0': 2,
    '1': 1.5,
    '2': 1.2
}


def normalize():
    global feedback
    feedback_normalize ={}
    index = 0
    while index < len(feedback):
        normalize_engine = {}
        engine =  feedback[str(index)]
        max = sorted(engine.items(), key=lambda x: x[1], reverse=True)[0][1]
        min = sorted(engine.items(), key=lambda x: x[1], reverse=False)[0][1]
        for key,value in engine.items():
            normalize_engine[key] = (value-min)/(max-min)
        feedback_normalize[str(index)] = normalize_engine
        index =index + 1

    index = 0
    while index < len(feedback):
        if index == 0:
            print('A Engine:')
        elif index == 1:
            print('B Engine')
        else:
            print('C Engine')
        engine = feedback_normalize[str(index)]
        for key, value in engine.items():
            print("---" + str(key) + ": " + str(round(value, 4)))
        index = index + 1

    return feedback_normalize


def combMNZ(normalized_feedback):
    index = 0
    rank_feedback = {}
    doc_engine = {}

    while index < len(normalized_feedback):
        engine = normalized_feedback[str(index)]
        for key, value in engine.items():
            if key not in doc_engine.keys():
                doc_engine[key] =1
            else:
                doc_engine[key] =doc_engine[key] + 1
        index = index + 1

    index = 0
    while index < len(normalized_feedback):
        engine = normalized_feedback[str(index)]
        for key, value in engine.items():
            if key not in rank_feedback.keys():
                rank_feedback[key] =value
            else:
                rank_feedback[key] =rank_feedback[key] + value
        index = index +1

    for key, value in rank_feedback.items():
        rank_feedback[key] =rank_feedback[key] * doc_engine[key]

    rank = sorted(rank_feedback.items(), key=lambda x: x[1], reverse=True)
    for rank_doc in rank:
        print(rank_doc[0]+": "+str(round(rank_doc[1],4)))
    return rank


def combSUM(normalized_feedback):
    rank_feedback = {}
    index = 0
    while index < len(normalized_feedback):
        engine = normalized_feedback[str(index)]
        for key, value in engine.items():
           if key not in rank_feedback.keys():
                rank_feedback[key] = value
           else:
               rank_feedback[key] = rank_feedback[key] + value
        index = index + 1
    rank = sorted(rank_feedback.items(), key=lambda x: x[1], reverse=True)
    for rank_doc in rank:
        print(rank_doc[0]+": "+str(round(rank_doc[1],4)))
    return rank


def LC(normalized_feedback):
    rank_feedback = {}
    global weight
    index = 0
    while index <len(normalized_feedback):
        engine = normalized_feedback[str(index)]
        for key, value in engine.items():
           if key not in rank_feedback.keys():
                rank_feedback[key] = value * weight[str(index)]
           else:
               rank_feedback[key] = rank_feedback[key] + value * weight[str(index)]
        index = index +1
    rank = sorted(rank_feedback.items(), key=lambda x: x[1], reverse=True)
    for rank_doc in rank:
        print(rank_doc[0]+": "+str(round(rank_doc[1],4)))
    return rank


if __name__ == '__main__':
    print('Normalized')
    normalized_feedback = normalize()

    # print()
    # print('combMNZ:')
    # combMNZ(normalized_feedback)
    #
    # print()
    # print('combSUM')
    # combSUM(normalized_feedback)
    #
    # print()
    # print('LC')
    # LC(normalized_feedback)
