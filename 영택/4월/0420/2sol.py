# 프로그래머스 이모티콘 할인행사
# https://school.programmers.co.kr/learn/courses/30/lessons/150368

from copy import deepcopy as dc

def get_possible(idx, dis_list, n, emo) :
    global dis
    if idx == n : 
        temp = dc(dis_list)
        dis.append(temp)
        return
    discount = [10,20,30,40]
    for d in discount : 
        dis_list[idx] = d
        get_possible(idx+1,dis_list,n,emo)

def check(users,pay_list, emo) :
    global buy, pay
    my_dict = {10 : 0.9, 20 : 0.8, 30 : 0.7, 40 : 0.6}
    plus = 0
    payment = 0
    for user in users : 
        sum_pay = 0
        for i, p in enumerate(pay_list) :
            if user[0] <= p : 
                sum_pay += round(emo[i]*my_dict[p])
        if sum_pay >= user[1] :
            plus += 1
        else : 
            payment += sum_pay

    if plus == buy : 
        buy = plus
        pay = max(payment, pay)
    elif buy < plus : 
        buy = plus
        pay = payment

def solution(users, emoticons):
    global buy, pay, dis
    buy = pay = 0
    dis = list()
    get_possible(0,[0]*len(emoticons),len(emoticons),emoticons)
    for d in dis : 
        check(users, d, emoticons)


    return [buy, pay]