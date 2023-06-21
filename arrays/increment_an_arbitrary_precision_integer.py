"""
Write a program which takes as input an array
 of digits encoding a nonnegative decimal integer
 D and updates the array to represent the integer D + 1.
 For example, if the input is (1,2,9) then you should update
 the array to (1,3,0). Your algorithm should work even if
  it is implemented in a language that has finite-precision arithmetic.
"""


def plus_one(a: list):
    a[-1] += 1
    for i in reversed(range(1, len(a))):
        if a[i] != 10:
            break
        a[i] = 0
        a[i - 1] += 1
    if a[0] == 10:
        a[0] = 1
        a.append(0)
    return a


a_list = [1, 2, 9]
print(plus_one(a_list))
