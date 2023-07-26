import sys
import gc
import os

def tree_make(n):
    """ Creates a tree recursively based on lists of 2 elements """
    node = [None, None]
    if n == 0:
        return node
    node[0] = tree_make(n-1)
    node[1] = tree_make(n-1)
    return node

def tree_check(n):
    """ Walkthrough the tree and add 1 for each node found """
    if n[0] is None:
        return 1
    left_result = tree_check(n[0])
    right_result = tree_check(n[1])
    result = 1 + left_result + right_result
    return result

def tree_make_and_check(n, keep_in_memory=False):
    """ Create a tree and check for its value based on nodes """
    tree = tree_make(n)
    check = tree_check(tree)
    if keep_in_memory:
        return (tree, check)
    return (None, check)

def data_iter(d, n):
    """ Iterate over tree and check its content """
    niter = 1 << (n - d + 4)
    results = [0] * niter
    for index in range(0, niter):
        tree = tree_make(d)
        check = tree_check(tree)
        results[index] = check
    c = sum(results)
    return niter, d, c

def binary_trees_run(n):
    """ Run binary trees benchmark """
    gc.disable()
    result = {}
    depth_list = list(range(4, n, 2) if n % 2 != 0 else range(4, n+1, 2))
    id_list = list(range(0, len(depth_list)))
    iter_list = zip(depth_list, id_list)
    for work in iter_list:
        item = work[1]
        d = work[0]
        result[item] = data_iter(d, n)
    for value in id_list:
        niter, d, c = result[value]
        # print("{}\t trees of depth {}\t check: {}".format(niter, d, c))
        print("%d\t trees of depth %d\t check: %d" % (niter, d, c))

if __name__ == "__main__":
    n = int(sys.argv[1])
    binary_trees_run(n)
