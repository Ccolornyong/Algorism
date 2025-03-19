def solution(code):
    ret = ''
    mode = 0
    idx = len(code)
    modes = []
    
    for i in range(idx):  
        if mode == 0:
            if code[i] != '1' and i%2==0:
                ret += code[i]
            if code[i] == '1':
                mode = 1
            continue
        if mode == 1:
            if code[i] != '1' and i%2!=0:
                ret += code[i]
            if code[i] == '1':
                mode = 0
                
    if len(ret)==0:
        return "EMPTY"
    
    return ret