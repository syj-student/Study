import math
import collections


def solution(fees, records):
    endtime = 24 * 60 - 1

    def cal_fee(car):
        fee = fee_info[car]
        if parking_info[car]:
            fee += endtime
        print(car, fee)
        if fee <= fees[0]:
            return fees[1]
        else:
            return fees[1] + math.ceil((fee - fees[0]) / fees[2]) * fees[3]

    def cal_time(t):
        h, m = map(int, t.split(':'))
        total_m = h * 60 + m
        return total_m

    fee_info = collections.defaultdict(int)
    parking_info = dict()
    for l in records:
        t, car, io = l.split()
        if io == 'IN':
            fee_info[car] -= cal_time(t)
            parking_info[car] = 1
        else:
            fee_info[car] += cal_time(t)
            parking_info[car] = 0
    answer_list = sorted(parking_info.keys())
    answer = list()
    for x in answer_list:
        answer.append(cal_fee(x))
    return answer
