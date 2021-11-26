def solution(A):

    def prefix_sums(A):
        n = len(A)
        P = [0] * (n + 1)
        for k in range(1, n + 1):
            P[k] = P[k - 1] + A[k - 1]
        return P

    prefix_sums_arr = [0] * (len(A)+1)
    prefix_sums_arr = prefix_sums(A)
    passing_cars = 0
    for iter in range(len(A)):
        if A[iter] == 0:
            passing_cars += (prefix_sums_arr[len(A)] - prefix_sums_arr[iter])
            if passing_cars > 1000000000:
                return -1
    
    return passing_cars
