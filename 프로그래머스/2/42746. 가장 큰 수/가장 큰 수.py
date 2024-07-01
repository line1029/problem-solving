def solution(numbers): 
    
    return "".join(sorted(map(str, numbers), key=lambda x: (x*4)[:4], reverse=True)) if not all(v == 0 for v in numbers) else "0"