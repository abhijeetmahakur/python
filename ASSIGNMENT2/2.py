def isprime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True


def ispersq(n):
    k = int(n**0.5)
    return k * k == n


def isperqu(n):
    k = round(n ** (1/3))
    return k ** 3 == n


def isclassify(nums):
    res = {
        "prime": [],
        "composite": [],
        "perfectsq": [],
        "perfectqu": []
    }

    for n in nums:
        if isprime(n):
            res["prime"].append(n)
        else:
            res["composite"].append(n)

        if ispersq(n):
            res["perfectsq"].append(n)

        if isperqu(n):
            res["perfectqu"].append(n)

    return res

nums = [2, 3, 5, 7, 89, 16, 27, 64]
result = isclassify(nums)
print(result)
