#node class
class Node:
    def __init__(self, label):
        self.label = label
        self.left = None
        self.right = None
        self.parent = None

# global root
root = None
   
# create new tree (root)
def create_new_tree(label):
    global root
    if root is not None:
        print('Tree sudah dibuat')
    else:
        root = Node(label)
        print(f'Node {label} berhasil dibuat menjadi root.')

# insert left
def insert_left(label, node):
    global root
    if root is None:
        print("Buat tree terlebih dahulu")
        return None
    if node.left is not None:
        print(f'Node {node.label} sudah ada anak kiri!')
        return None
    new_node = Node(label)
    new_node.parent = node
    node.left = new_node
    print(f'Node {label} berhasil ditambakan ke anak kiri {node.label}')
    return new_node

# insert right
def insert_right(label, node):
    global root
    if root is None:
        print("Buat tree terlebih dahulu")
        return None
    if node.right is not None:
        print(f'Node {node.label} sudah ada anak kiri!')
        return None
    
    new_node = Node(label)
    new_node.parent = node
    node.right = new_node
    print(f'Node {label} berhasil ditambahkan ke anak kanan {node.label}')
    return new_node

# cek empty
def empty():
    return root is None

# update node
def update(label, node):
    if root is None:
        print('Buat tree terlebih dahulu!')
    elif node is None:
        print("Node yang ingin diganti tidak ada!")
    else:
        old = node.label
        node.label = label
        print(f"Label node {old} berhasil diubah menjadi {label}")

# retrieve
def retrieve(node):
    if root is None:
        print("Buat tree terlebih dahulu!")
    elif node is None:
        print("Node tidak ada!")
    else:
        print("label node: ", node.label)

#  find node info
def find(node):
    if root is None:
        print("buat tree terlebih dahulu")
        return
    if node is None:
        print("Node tidak ada!")
        return
    
    print("=== INFORMASI NODE ===")
    print("label node : ", node.label)
    print("Root node : ", root.label)

    # parent
    if node.parent is None:
        print("parent node : (tidak punya orang tua)")
    else:
        print("parent node : ", node.parent.label)

    # sibling
    if node.parent:
        if node.parent.left == node and node.parent.right:
            print("saudara : ", node.parent.right.label)
        elif node.parent.right == node and node.parent.left:
            print('saudara : ', node.parent.left.label)
        else:
            print('saudara : (tidak punya saudara)')
    else:
        print('saudara : ridak punya saudra')

    # children
    print("anak kiri : ", node.left.label if node.left else "(tidak ada)")
    print('anak kanan : ', node.right.label if node.right else "(tidak ada)" )

# traversal
def pre_order(node):
    if node:
        print(node.label, end=', ')
        pre_order(node.left)
        pre_order(node.right)

def in_order(node):
    if node:
        in_order(node.left)
        print(node.label, end=', ')
        in_order(node.right)

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.label, end=', ')

#  delete tree (recursive)
def delete_tree(node):
    global root
    if node:
        delete_tree(node.left)
        delete_tree(node.right)
        if node == root:
            root = None

# delete subtree (left & right only)
def delete_sub(node):
    if root is None:
        print("Buat tree terlebih dahulu")
        return
    delete_tree(node.left)
    delete_tree(node.right)
    node.left = None
    node.right = None
    print(f'subtree node {node.label} berhasil dihapus')

# size
def size(node):
    if node is None:
        return 0
    return 1 + size(node.left) + size(node.right)



def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

# print caracterhistis
def characteristic():
    if root is None:
        print("tree kosong")
        return
    print('size tree : ',size(root))
    print("height tree : ", height(root))
    print('average node of tree : ', size(root)/height(root))


# main progrm
if __name__ == "__main__":
    
    create_new_tree('A')

    B = insert_left('B', root)
    C = insert_right('C', root)
    D = insert_left('D', B)
    E = insert_right("E", B)
    F = insert_left('F', C)
    G = insert_left('G', E)
    H = insert_right('H', E)
    I = insert_left('I', G)
    J = insert_right('J', G)

    print('tree empty : ', empty())

    update('Z', C)
    update('C', C)

    retrieve(C)
    find(C)

    print('\npre order : e ')
    pre_order(E)

    print('\nin order : E')
    in_order(E)

    print('\npost order : E')
    post_order(E)

    print('\n')
    characteristic()

    delete_sub(E)

    print('\npre order setelah menghapus subtree E: ')
    pre_order(root)

    print('\n')
    characteristic()