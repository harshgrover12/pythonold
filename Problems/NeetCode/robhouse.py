def rob(l1:list):
    rob1, rob2 = 0, 0
    # [rob1, rob2, n, n+1,....]
    for n in l1:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2


print(rob([1,2,3,1]))