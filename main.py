def pi(n):
    n += 2
    n1 = 0
    s = 10002499687
    ms = 8
    m = ms
    f1 = 10**ms
    f2 = f1**2
    a = 10005 * f2 - s**2

    while ms < n:
        a *= f2
        b = s * 2 * f1
        d = a // b
        s = s * f1 + d
        a -= d * (b + d)
        ms += m
        if ms * 2 > n: m = n - ms
        else: m = ms
        f1 = 10**m
        f2 = f1**2
        n1 += 1

    base = 10**n
    A = 13591409 * base
    B = A
    c3 = 13591409
    k = 1
    while abs(A) > 5:
        c1 = ((108 - 72 * k) * k - 46) * k + 5
        c2 = 10939058860032000 * k**3
        c4 = c3
        c3 += 545140134
        k += 1
        A = A * c1 * c3 // (c2 * c4)
        B += A

    result = 426880 * base * s // B // 100
    final = str(result)[0] + ',' + str(result)[1:n-1]
    return final
