def solution(ineq, eq, n, m):
    answer = 0
    if ineq == ">" and eq == "=":
        answer = int(n>=m)
    if ineq == "<" and eq == "=":
        answer = int(n<=m)
    if ineq == ">" and eq == "!":
        answer = int(n>m)
    if ineq == "<" and eq == "!":
        answer = int(n<m)
    return answer