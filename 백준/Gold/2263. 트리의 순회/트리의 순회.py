from sys import stdin, stdout, setrecursionlimit
n = int(stdin.readline())
inorder = list(map(int, stdin.readline().split()))
inorder_index = {val:idx for idx, val in enumerate(inorder)}
postorder = list(map(int, stdin.readline().split()))
if n > 999:
    setrecursionlimit(n + 1)

preorder = []
def get_preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    root = postorder[post_end]
    preorder.append(root)
    if in_start == in_end:
        return
    in_root_idx = inorder_index[root]
    left_length = in_root_idx - in_start
    get_preorder(in_start, in_start + left_length - 1, post_start, post_start + left_length - 1)
    get_preorder(in_start + left_length + 1, in_end, post_start + left_length, post_end - 1)

get_preorder(0, n-1, 0, n-1)
stdout.write(" ".join(map(str, preorder)))
