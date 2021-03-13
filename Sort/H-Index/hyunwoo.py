def solution(citations):
    citations = sorted(citations, reverse=True)
    
    index = 0
    while index < len(citations):
        if index + 1 <= citations[index]:
            index+=1   
        else :
            break
    
    return index