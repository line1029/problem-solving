from sys import stdin, stdout
n = int(stdin.readline())
tree = dict((k, v) for k, *v in map(lambda x: x.split(), stdin.read().splitlines()))
preorder, inorder, postorder = [], [], []
def traverse_tree(node="A"):
    if node != ".":
        preorder.append(node)
        traverse_tree(tree[node][0])
        inorder.append(node)
        traverse_tree(tree[node][1])
        postorder.append(node)
    return


traverse_tree()
stdout.write(f"{''.join(preorder)}\n{''.join(inorder)}\n{''.join(postorder)}")