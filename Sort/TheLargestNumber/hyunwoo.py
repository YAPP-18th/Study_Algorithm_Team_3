import functools

def solution(numbers):
    def sort(a, b):
        return  1 if (a + b) > (b + a) else -1
    numbers = [str(el) for el in numbers]
    numbers = sorted(numbers, key=functools.cmp_to_key(sort), reverse=True)
    return str(int("".join(numbers)))