
from tree_structures import TreeNode

def make_tree_by(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value is None:
            return

        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2 * idx + 1) #왼쪽 자식 만들기
        parent.right = make_tree_by(lst, 2 * idx + 2) #오자 만들기

    return parent
