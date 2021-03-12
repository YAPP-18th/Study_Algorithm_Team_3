def solution(numbers):
    answer = ''
    strings = []
    for num in numbers:
        strings.append(str(num))
    strings.sort()
    strings = strings[::-1]

    # 모범답안 참고 - 각 number*3 한 숫자를 기준으로 number 정렬
    # sorted의 정렬 기준을 설정하는 key 
    strings = sorted(strings, key=lambda x:x*3, reverse = True)
    
    for string in strings:
        answer += string
    return str(int(answer))





'''
다른 풀이
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) # t1이 크다면 1 // t2가 크다면 -1 //  같으면 0
    # 1 반환, 즉 t1이 크다면 a->b로 정렬
    # -1 반환, 즉 t2가 크다면 b->a로 정렬
    # 0 반환, 같다면 a->b?

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer

sort의 key는 정렬 기준을 지정한다.
여기선 sorted함수의 key function인 cmp_to_key를 이용했다.
위 comparator함수 역할을 하는 것이 python2의 cmp()함수인데 python3에서는 사라졌다고 한다. 
comparator함수는 인자 2개를 받아 비교해서, 작으면 음수(-1), 같으면 0, 크면 양수(1)를 반환한다.

'''