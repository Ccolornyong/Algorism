def solution(n, lost, reserve):
    answer = 0
    CanShare = sorted(list(set(reserve) - set(lost))) # 2개 있는 애 중에 도난 안당한 애 (빌려주기 가능)
    Search = [] # 이미 빌린 학생인지 확인 (도난 당한 애 중)
    OnlyOneCloth = n - len(set(reserve) | set(lost))
    lost = sorted(lost)
    CanShare = sorted(CanShare)
    
    # 빌린 애 찾기 (CanShare랑 lost 비교)
    for i in CanShare:
        if i-1 in lost and i-1 not in Search:
            Search.append(i-1)
            continue
        elif i+1 in lost and i+1 not in Search:
            Search.append(i+1)
            continue
    
    # 여벌이 있는 애(도난과 상관없이)와 빌린 애 교집합 
    # + 애초에 한개만 가져온 애    
    answer = len(set(reserve) | set(Search)) + OnlyOneCloth
    
    return answer