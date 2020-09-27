def two_number_sum_up_for_a_value(L,k):
    for l in L:
        if k - l in L:
            return True
        else:
            return False
ans = two_number_sum_up_for_a_value([10, 15, 3, 7],17)
print(ans)