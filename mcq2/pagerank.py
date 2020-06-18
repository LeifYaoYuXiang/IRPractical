#encoding:utf-8
relationship = {
    'A': ['C'], # 指向A的所有元素
    'B': ['A'],
    'C': ['A','B','D'],
    'D': []
}

inital = 1
damping_factor = 0.85
iter = 3



last_score ={

}
score = {

}


def check_contribute(item):
    outside_link = 0
    for value in relationship.values():
        if item in value:
            outside_link = outside_link +1
    return outside_link


def page_rank():
    global iter
    global relationship
    global last_score
    global score
    step = 0
    iter = iter + 1
    while step < iter:
        if step == 0:
            for key, value in relationship.items():
                last_score[key] = inital
        else:
            for key, value in last_score.items():
                contribution = 0
                contribution_item = relationship[key]
                for page in contribution_item:
                    contribution = contribution + last_score[page]/check_contribute(page)
                score[key] = (1- damping_factor) + damping_factor * contribution
            last_score =score
            score = {}
        step = step + 1
    return last_score


if __name__ == '__main__':
    feedback = page_rank()
    print(feedback)



