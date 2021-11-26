def solution(X, A):
    count = [0] * (X)
    iter_count = 0
    for element in A:
        count[element-1] += 1
        iter_count += 1
        if 0 not in count:
            return (iter_count-1)
    return -1
   
def solution2(X, A):
    count = [1] * (X)
    iter_count = 0
    for element in A:
        count[element-1] = 0
        iter_count += 1
        if sum(count) == 0:
            return (iter_count-1)
    return -1
    
def solution_best(X, A):
    count = [1] * (X)
    iter_count = 0
    countdown = X
    for element in A:
        if count[element-1] == 1:
            count[element-1] = 0
            countdown -= 1          
            if countdown == 0:
                return (iter_count)
        iter_count += 1
    return -1
