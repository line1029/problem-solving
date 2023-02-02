def infix_to_postfix(expression):
    stack = []
    result = []
    operators = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}

    for char in expression:
        if char.isalpha():
            result.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and operators[stack[-1]] >= operators[char]:
                result.append(stack.pop())
            stack.append(char)



    return "".join(result + stack[::-1])

print(infix_to_postfix(input()))