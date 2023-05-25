from sys import stdin, stdout
n = int(stdin.readline())
inorder = list(map(int, stdin.readline().split()))
inorder_index = {val:idx for idx, val in enumerate(inorder)}
postorder = list(map(int, stdin.readline().split()))

preorder = []
stack = [(0, n-1, 0, n-1)]
while stack:
    in_start, in_end, post_start, post_end = stack.pop()
    if in_start > in_end or post_start > post_end:
        continue
    root = postorder[post_end]
    preorder.append(root)
    in_root_idx = inorder_index[root]
    left_length = in_root_idx - in_start
    stack.append((in_start + left_length + 1, in_end, post_start + left_length, post_end - 1))
    stack.append((in_start, in_start + left_length - 1, post_start, post_start + left_length - 1))


stdout.write(" ".join(map(str, preorder)))
