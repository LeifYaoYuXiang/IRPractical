#encoding:utf-8
from math import sqrt

doc1=[0, 0, 0, 0.584, 0, 0, 0.584, 0, 1.584]
length1=0
doc2=[0, 1.584, 0.584, 0, 0, 0, 0.584, 1.584, 0]
length2=0
doc3=[0, 0, 0.584, 0.584, 3.168, 1.584, 0, 0, 0]
length3=0
query=[0, 0, 0, 0.584, 0, 0, 0, 0, 0]
lengthq=0

if __name__ == '__main__':
    for dig in doc1:
        length1=length1+dig*dig
    length1=sqrt(length1)

    for dig in doc2:
        length2=length2+dig*dig
    length2=sqrt(length2)

    for dig in doc3:
        length3=length3+dig*dig
    length3=sqrt(length3)

    for dig in query:
        lengthq=lengthq+dig*dig
    lengthq=sqrt(lengthq)


    q1=0
    q2=0
    q3=0

    index=0;
    while index<len(query):
        q1 = q1 + query[index] * doc1[index]
        q2 = q2 + query[index] * doc2[index]
        q3 = q3 + query[index] * doc3[index]
        index=index+1


    cosq1 = q1 / (length1 * lengthq)
    cosq2 = q2 / (length2 * lengthq)
    cosq3 = q3 / (length3 * lengthq)

    print(cosq1)
    print(cosq2)
    print(cosq3)