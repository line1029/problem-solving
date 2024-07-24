class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["*", "+", "-", "/"]
        st = []
        for x in map(lambda x: x if x in ops else int(x), tokens):
            if x in ops:
                a, b = st.pop(), st.pop()
                if x == "*":
                    st.append(a*b)
                elif x == "+":
                    st.append(a+b)
                elif x == "-":
                    st.append(b - a)
                else:
                    k = b//a
                    if k < 0 and b%a: k += 1
                    st.append(k)
            else:
                st.append(x)
        return st[0]
        