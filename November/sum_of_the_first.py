def series_sum(n):
    nomenator = 1
    denominator = 1
    sum_not_null = 0
    while n is not 0:
        denominator += 3
        print()
        sum_not_null = nomenator + (1/denominator)
        n -= 1
        return str(round(sum_not_null, 2))
    else:
        return str(round(0, 2))

series_sum(4)


