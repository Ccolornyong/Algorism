def solution(num_list):
    # even_sum = [num_list[i] for i in range(len(num_list)) if i%2==0]
    # odd_sum = [num_list[i] for i in range(len(num_list)) if i%2!=0]
    even_sum = ""
    odd_sum = ""
    
    for i in num_list:
        if i%2==0:
            even_sum+=str(i)
            
    for i in num_list:
        if i%2!=0:
            odd_sum+=str(i)
            
    return int(odd_sum)+int(even_sum)