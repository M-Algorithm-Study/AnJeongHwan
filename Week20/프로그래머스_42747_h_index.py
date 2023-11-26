def solution(citations):
    citations = sorted(citations, reverse=True)
    
    for i, citation in enumerate(citations):
        if i >= citation:  # h번 이상 인용된 논문이 h편 이상일 때
            return i
    
    return len(citations)