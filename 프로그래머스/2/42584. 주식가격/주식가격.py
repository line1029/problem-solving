def solution(prices):
    price_stack = []
    idx_stack = []
    res = list(range(len(prices) - 1, -1, -1))
    for idx, price in enumerate(prices):
        while price_stack and price_stack[-1] > price:
            falled_idx, falled_price = idx_stack.pop(), price_stack.pop()
            res[falled_idx] = idx - falled_idx
        price_stack.append(price)
        idx_stack.append(idx)
    return res
            
        
            