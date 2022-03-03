# def max_profit(A):
#     profit = 0
#     for i in range(len(A)-1):
#         if A[i] < A[i+1]:
#             profit += A[i+1]-A[i]
#     return profit
#
#
# A= [1,4,5,2,6,8,9]
# print(max_profit(A))

def max_profit(prices: list):
    l = 0
    r = 0
    maxprofit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxprofit = max(maxprofit, profit)
        else:
            l = r
        r += 1
    return maxprofit


print(max_profit([4, 5, 1, 2, 6, 8, 9]))
