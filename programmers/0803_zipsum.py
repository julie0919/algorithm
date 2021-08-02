def solution(A, B):
    answer = []
    for a, b in zip(A, B):
        answer_in = []
        for c, d in zip(a, b):
            answer_in.append(c + d)
        answer.append(answer_in)
    return answer