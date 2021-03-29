def solution(phone_book):
    answer = True
    hash = {}
    phone_book.sort()
    for i in range(0, len(phone_book)-1):
        if (phone_book[i+1].startswith(phone_book[i],0)):
            answer = False
            return answer
    
    return answer


'''
추가설명

- startswith(시작하는문자, 시작지점) 
: 문자열이 특정문자로 시작하는지 여부를 알려준다. 
true나 false 를 반환. 
두번째 인자를 넣음으로써 찾기시작할 지점을 정할수있다.

- endswith(끝나는문자, 문자열의시작, 문자열의끝) 
: endswith는 문자열이 특정문자로 끝나는지 여부를 알려준다. 
true나 false를 반환. 
두번째인자로 문자열의 시작과 세번째인자로 문자열의 끝을 지정할 수 있다.
'''


'''
<첫번째 시도>
정렬해서 연속된 번호 검사 : Testcase13 failed. 
->[반례] 1, 22, 2322 -> true 인데 false나옴. 
안에 포함되는게 아니라 '접두어'인점 주의 : << in -> startswith >>
for i in range(0, len(phone_book)-1):
    if phone_book[i] in phone_book[i+1]:
        answer = False
        return answer
        
'''