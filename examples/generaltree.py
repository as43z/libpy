from libpy.ds.tree import GTNode, repr_gt_node

# Make a tree
root = GTNode()

for i in range(5):
    root.children.append(GTNode(parent = root))

root.children[1].children.append(GTNode(parent = root.children[1]))
root.children[1].children.append(GTNode(parent = root.children[1]))
root.children[1].children.append(GTNode(parent = root.children[1]))

root.children[2].children.append(GTNode(parent = root.children[2]))
root.children[2].children.append(GTNode(parent = root.children[2]))

repr_gt_node(root)
repr_gt_node(root, span=False)

