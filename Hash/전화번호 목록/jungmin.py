import re

def solution(phone_book):
    answer = True
    
    # 리스트 -> 딕셔너리
    phone_book= dict(zip(range(len(phone_book)), phone_book))
    
    # 일부 일치하는 값이 있으면 false
    for k in phone_book.keys():
        for v in phone_book.values():
            if re.search("^"+phone_book[k],v) and phone_book[k]!=v:
                answer = False
        
            
    return answer

