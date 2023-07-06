def is_palindrome(s: str):
    word = ""
    for i in s:
        if not i.isalpha():
            continue
        else:
            word += i
    if word == word[::-1]:
        return True
    else:
        return False


def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def bubble_sort(li):
    for i in range(len(li)):
        for j in range(0, len(li) - i - 1):
            if li[j] > li[j + 1]:
                temp = li[j]
                li[j] = li[j + 1]
                li[j + 1] = temp
    return li
