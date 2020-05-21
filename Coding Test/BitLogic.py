def maxXor(lo, hi, k):
    max = -1
    a, b = lo, hi

    for a in range(lo, hi):
        for b in range(a+1, hi+1):
            temp = a ^ b
            if temp <= k:
                if temp > max:
                    temp = max





        a += 1
        if a >= b:
            if b == hi:
                a -= 1
                break
            else:
                b += 1





    while False:
        result = a ^ b
        if result > k:
            a
        else:
            return result

print(bin(12))
print(int('0b1100',2))
