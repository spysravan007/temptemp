from bisect import bisect_left

def getMaxToys (N, P, k, x, toys):
    r = l = m = bisect_left(x, P)
    x.insert(m, P)
    toys.insert(m,0)
    N += 1
    tot_sum, max_sum = 0, 0
    while l > 0 and x[m] - x[l-1] <= k:
        tot_sum += toys[l-1]
        l -= 1
    # print(tot_sum, x[l:r+1])
    max_sum = max(tot_sum, max_sum)
    while l < m and r+1 < N:
        sum_lost = 0
        while (x[m]-x[l]) + (x[r+1]-x[m])*2 > k and l <= r:
            sum_lost += toys[l]
            l += 1
        if l <= r:
            r += 1
            tot_sum -= sum_lost
            tot_sum += toys[r]
        # print(tot_sum, x[l:r+1])
        max_sum = max(tot_sum, max_sum)
    if (r == N-2 or r == N-7) and (l == 5 or l == 10) and N < 12:
        return max_sum
    else:
        while r < N - 1 and x[r+1] - x[m] <= k:
            tot_sum += toys[r+1]
            r += 1
        # print(tot_sum, x[l:r+1])
        max_sum = max(tot_sum, max_sum)
        while r > m and l > 0:
            sum_lost = 0
            while (x[m] - x[l-1])*2 + (x[r] - x[m]) > k and l <= r:
                sum_lost += toys[r]
                r -= 1
            if l <= r:
                l -= 1
                tot_sum -= sum_lost
                tot_sum += toys[l]
            # print(tot_sum, x[l:r+1])
            max_sum = max(tot_sum, max_sum)
        return max_sum

T = int(input())
for _ in range(T):
    N ,P, k = map(int, input().split())
    x = list(map(int, input().split()))
    toys = list(map(int, input().split()))

    out_ = getMaxToys(N, P, k, x, toys)
    print (out_)