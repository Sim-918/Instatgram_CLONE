import sys
input=sys.stdin.readline

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported = {x: 0 for x in id_list}

    for r in set(report):
        a,b = r.split()
        reported[b] += 1

    for r in set(report):
        a,b = r.split()
        if reported[b] >= k:
            answer[id_list.index(a)] += 1

    return answer


'''
    id_list는 유저
    report는 x y -> x가 y를 신고
    k만큼 신고를 당하면 
    유저에게 정지된 id개수 출력

'''

