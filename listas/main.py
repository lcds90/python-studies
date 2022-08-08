from node import Node


leonardo = Node("Leonardo")
fabio = Node("Fabio")
grimes = Node("Grimes")

leonardo.next = fabio
leonardo.next.next = grimes

print(f"Leonardo: {leonardo}")
print(f"Fabio: {fabio}")
print(f"Grimes: {grimes}")
