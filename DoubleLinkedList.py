class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def getValue(self):
        return self.value

    def setValue(self, new_value):
        self.value = new_value

    def getNext(self):
        return self.next

    def setNext(self, new_next):
        if isinstance(new_next, Node) or new_next is None:
            self.next = new_next
        else:
            raise Exception("New Next must be Node")

    def getPrev(self):
        return self.prev

    def setPrev(self, new_prev):
        if isinstance(new_prev, Node) or new_prev is None:
            self.prev = new_prev
        else:
            raise Exception("New Prev must be Node")

    def clear(self):
        self.value = None
        self.next = None
        self.prev = None

    def __str__(self):
        next = self.next
        return "Node(" + str(self.value) + ") -->" + ("x" if next is None else str(next))

    def __str__(self):
        return '(' + str(self.value) + ') -->' + str(self.next)


class DoubleLinkedList:
    def __init__(self, elements):
        self.head, self.tail = None, None
        for el in elements:
            self.reverse(el)

    def __str__(self):
        if self.isEmpty():
            return "[]"
        return "[" + str(self.head) + "]"

    def __init__(self, data=[]):
        self.head, self.tail, self.len = None, None, 0
        for e in data:
            self.append(e)

    def __len__(self):
        return self.len

    def append(self, value):
        # Insertar un nuevo elemento
        new_node = Node(value)
        if len(self) == 0:
            self.head = new_node
            self.setTail(new_node)
        else:
            current_tail = self.tail
            current_tail.setNext(new_node)
            new_node.setPrev(current_tail)
            self.setTail(new_node)
        self.len = self.len + 1

    def search(self, value):
        current = self.head
        while current is not None and current.getValue() != value:
            current = current.getNext()
        return current

    def getHead(self):
        return self.head

    def setHead(self, new_head):
        if new_head is not None:
            new_head.setPrev(None)
            self.head = new_head
        else:
            self.head = None

    def getTail(self):
        return self.tail

    def setTail(self, new_tail):
        if new_tail is not None:
            new_tail.setNext(None)
            self.tail = new_tail
        else:
            self.tail = None

    def update(self, old_value, new_value):
        node_origin = self.search(old_value)
        node_origin.setValue(new_value)

    def slice(self, value, n=1):
        ld = DoubleLinkedList()
        node_origin = self.search(value)
        if node_origin is not None:
            current, index = node_origin, 0
            while current is not None and index < n:
                ld.append(current.getValue())
                current = current.getNext()
                index += 1
        return ld

    def isEmpty(self):
        return len(self) == 0

    def merge(self, list_b):
        # Unir dos listas
        if self.isEmpty():
            return list_b
        if list_b.isEmpty():
            return self
        self.tail.setNext(list_b.getHead())
        self.setTail(list_b.getTail())

    def delete(self, value):
        # Eliminar un elemento dado su valor
        value_node = self.search(value)
        if value_node is not None:
            if len(self) == 1:  # Soy el único               #Si es el único valor
                self.head, self.tail = None, None
            else:
                if value_node == self.getHead():  # Si el valor es el mismo que el valor de la cabeza
                    self.head = value_node.getNext()
                    self.head.setPrev(None)
                else:
                    # Buscar el previo a value_node
                    prev = value_node.getPrev()
                    if value_node == self.getTail():  # Si el valor es el mismo que el valor de la cola
                        self.setTail(prev)
                    else:
                        nxt = value_node.getNext()
                        prev.setNext(nxt)  # Si el valor es cualquier otro valor
                        if nxt is not None:
                            nxt.setPrev(prev)  # El anterior tiene que no ser vacio para que pueda ser cola

            value_node.clear()  # borra el valor del nodo
            self.len -= 1  # cambia la longitud al eliminae el valor
        else:
            raise Exception("Element not found.")

    def deleteDuplicates(self):
        # Eliminar elementos duplicados
        s = []
        node = self.getHead()
        while node is not None:
            if node.getValue() not in s:
                s.append(node.getValue())
                node = node.getNext()
            else:
                self.delete(node.getValue())
                node = node.getNext()
        return self

    def reverse(self, element):
        if element is not None:
            newNode = Node(element)
            if self.isEmpty():
                self.head = newNode
                self.tail = newNode
            else:
                current = self.head
                current.setPrev(newNode)
                newNode.setNext(current)
                self.head = newNode


class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, e):
        self.data.append(e)  # Punto de referencia cómo el inicio

    def dequeue(self):  # como punto de referencia el inicio
        element = self.data[0]
        self.data.pop(0)
        return element

    def __str__(self):
        return "Queue(" + str(self.data[0]) + ")"

    def __len__(self):
        return len(self.data)


# Implementación LIFO
class Stack:
    def __init__(self):
        self.data = []

    def push(self, e):
        # self.data.append(e) #Punto de referencia cómo el final
        self.data.insert(0, e)  # Punto de referencia cómo el inicio

    def pop(self):
        element = self.data[0]
        self.data.pop(0)
        return element
        # self.data.pop(0) Punto de referencia es el inicio

    def __str__(self):
        return "Stack(" + str(self.data[0]) + ")"

    def __len__(self):
        return len(self.data)


def main():
    list = DoubleLinkedList([3, 4, 5, 6])
    print(list)


main()
