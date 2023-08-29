from sys import stdin, stdout
def main():
    programs = stdin.read().split("\n\n")
    programs.pop()
    ans = []
    for program in map(lambda x: x.splitlines(), programs):
        k = program.index("END")
        program, inputs = program[:k], map(lambda x: [int(x)], program[k + 2:])
        for stack in inputs:
            for operation in program:
                if operation == "POP":
                    if not stack:
                        ans.append("ERROR")
                        break
                    stack.pop()
                elif operation == "INV":
                    if not stack:
                        ans.append("ERROR")
                        break
                    stack[-1] = -stack[-1]
                elif operation == "DUP":
                    if not stack:
                        ans.append("ERROR")
                        break
                    stack.append(stack[-1])
                elif operation == "SWP":
                    if len(stack) < 2:
                        ans.append("ERROR")
                        break
                    stack[-1], stack[-2] = stack[-2], stack[-1]
                elif operation == "ADD":
                    if len(stack) < 2:
                        ans.append("ERROR")
                        break
                    x = stack.pop()
                    stack[-1] += x
                elif operation == "SUB":
                    if len(stack) < 2:
                        ans.append("ERROR")
                        break
                    x = stack.pop()
                    stack[-1] -= x
                elif operation == "MUL":
                    if len(stack) < 2:
                        ans.append("ERROR")
                        break
                    x = stack.pop()
                    stack[-1] *= x
                elif operation == "DIV":
                    if len(stack) < 2:
                        ans.append("ERROR")
                        break
                    sign = 1 if stack[-1]*stack[-2] >= 0 else -1
                    x = abs(stack.pop())
                    if not x:
                        ans.append("ERROR")
                        break
                    stack.append((abs(stack.pop())//x)*sign)
                elif operation == "MOD":
                    if len(stack) < 2:
                        ans.append("ERROR")
                        break
                    sign = 1 if stack[-2] >= 0 else -1
                    x = abs(stack.pop())
                    if not x:
                        ans.append("ERROR")
                        break
                    stack.append((abs(stack.pop())%x)*sign)
                else:
                    stack.append(int(operation.split()[1]))
            else:
                if len(stack) != 1 or abs(stack[0]) > 10**9:
                    ans.append("ERROR")
                else:
                    ans.append(str(stack[0]))
        ans.append("")
    ans.pop()
    stdout.write("\n".join(ans))
main()