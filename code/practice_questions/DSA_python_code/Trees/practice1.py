'''1. Create the following binary tree:

```
      10
     /  \
    5    15
    
Display the root, left child, and right child.

'''

def Node(data):
    return {'data': data, 'left': None, 'right': None}

root = Node(10)
