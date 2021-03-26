def solution(phone_book):
    # 같은 글자 크기는 서로 다를 수 밖에 없음
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True