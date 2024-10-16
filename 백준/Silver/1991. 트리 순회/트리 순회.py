import sys

n = int(sys.stdin.readline().strip())
tree={}
for _ in range(n) :
  root, left, right = sys.stdin.readline().strip().split()
  tree[root] = [left,right]

def front(root) :
  if root != '.' :
    print(root, end='')
    front(tree[root][0])
    front(tree[root][1])

def middle(root) :
  if root != '.' :
    middle(tree[root][0])
    print(root, end='')
    middle(tree[root][1])

def back(root) :
  if root != '.' :
    back(tree[root][0])
    back(tree[root][1])
    print(root, end='')

front('A')
print()
middle('A')
print()
back('A')