

class Node:
    """
    🍇 A classe *Node* é uma classe que representa
    um nó da lista.
    Nesse nó é onde estarão guardados os dados
    """
    def __init__(cls, data=None, next=None):
        cls.data = data
        cls.next = next

    def __str__(cls):
        return (
            f"Node {cls.data} \n"
            f"Next {cls.next}\n"
            )
