# encoding:utf-8
import re
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
    answer = []
    index_a = 0
    index_b = 0
    while index_a != len(a) and index_b != len(b):
        if a[index_a] == b[index_b]:
            answer.append(a[index_a])
            index_a = index_a+1
            index_b = index_b+1
        elif a[index_a] < b[index_b]:
            index_a = index_a + 1
        else:
            index_b = index_b + 1
    return answer


def merge_or(a, b):
    token_a = a
    token_b = b
    answer = []
    index_a = 0
    index_b = 0
    while index_a != len(token_a) or index_b != len(token_b):
        if index_a == len(token_a):
            answer=answer+token_b[index_b:]
            # answer.append(token_b[index_b:])
            return answer
        elif index_b == len(token_b):
            answer = answer +token_a[index_a:]
            # answer.append(token_a[index_a:])
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


def merge_operation(n1, n2, operator):
    merge_result = []
    if operator == "+":
        merge_result = merge_and(n1, n2)
    if operator == "-":
        merge_result = merge_or(n1, n2)
    return merge_result


# 判断是否是运算符，如果是返回True
def is_operator(e):
    opers = ['+', '-', '(', ')']
    return True if e in opers else False


def query_format(query):
    query= re.sub(' ', '', query)
    formula_list = [i for i in re.split('(\[a-zA-Z]*)', query) if i]

    final_formula = []

    for item in formula_list:
        item_split = [i for i in re.split('([\+\-\(\)])', item) if i]
        final_formula += item_split

    index = 0
    while index < len(final_formula):
        if not is_operator(final_formula[index]):
            final_formula[index] = word[final_formula[index]]
        index += 1

    return final_formula


def query_decision(tail_op, now_op):

    """
    :param tail_op: 运算符栈的最后一个运算符
    :param now_op: 从算式列表取出的当前运算符
    :return: 1 代表弹栈运算，0 代表弹运算符栈最后一个元素， -1 表示入栈
    """
    # 定义4种运算符级别
    rate1 = ['+', '-']
    rate3 = ['(']
    rate4 = [')']

    if tail_op in rate1:
        if now_op in rate3:
            # 说明连续两个运算优先级不一样，需要入栈
            return -1
        else:
            return 1

    elif tail_op in rate3:
        if now_op in rate4:
            return 0  # ( 遇上 ) 需要弹出 (，丢掉 )
        else:
            return -1  # 只要栈顶元素为(，当前元素不是)都应入栈。
    else:
        return -1


def final_query(formula_list):
    word_stack = []  # 数字栈
    op_stack = []  # 运算符栈
    for e in formula_list:
        operator = is_operator(e)
        if not operator:
            word_stack.append(e)
        else:
            # 如果是运算符
            while True:
                # 如果运算符栈等于0无条件入栈
                if len(op_stack) == 0:
                    op_stack.append(e)
                    break
                # decision 函数做决策
                tag = query_decision(op_stack[-1], e)
                if tag == -1:
                    # 如果是-1压入运算符栈进入下一次循环
                    op_stack.append(e)
                    break
                elif tag == 0:
                    # 如果是0弹出运算符栈内最后一个(, 丢掉当前)，进入下一次循环
                    op_stack.pop()
                    break
                elif tag == 1:
                    # 如果是1弹出运算符栈内最后两个元素，弹出数字栈最后两位元素。
                    op = op_stack.pop()
                    num2 = word_stack.pop()
                    num1 = word_stack.pop()
                    # 执行计算
                    # 计算之后压入数字栈
                    word_stack.append(merge_operation(num1, num2, op))
    # 处理大循环结束后 数字栈和运算符栈中可能还有元素 的情况
    while len(op_stack) != 0:
        op = op_stack.pop()
        num2 = word_stack.pop()
        num1 = word_stack.pop()
        word_stack.append(merge_operation(num1, num2, op))

    return word_stack, op_stack


if __name__ == '__main__':
    read_in_line()
    query = 'a AND (b OR c)'
    query = query.replace("AND", "+").replace("OR", "-")
    query_list = query_format(query)
    result, _ = final_query(query_list)

    print("Query Result：", result[0])

    print(word['a'])
    print(merge_or(word['b'],word['c']))