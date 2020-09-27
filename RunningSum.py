def RunningSum(a):
    sum=[]
    sum_i=0
    for i in a:
        sum_i = sum_i + i
        sum.append(sum_i)
    return sum


a=[3,1,2,10,1]
print(RunningSum(a))
