def check_pow(N, k):
    if k < 0 or N < 0:
        raise ValueError("k and N must be greater than 0")
    if k == 0 and N == 1:
        return True
    if k in (0, 1) and N != 1:
        return False

    num = k
    while num < N:
        num *= k
    return num == N
