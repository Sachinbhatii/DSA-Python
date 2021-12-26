
class Node:
    def __init__(self,data):
        self.data = data
        self.ref = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def Traversing(self):
        if self.head == None:
            print("Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

# --------------- ADDITION IN SINGLE LINKED LIST ----------------


    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head == None:
            new_node = self.head
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("No such Node Found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self,data,x):
        new_node = Node(data)
        if self.head == None:
            print("Linked List is Empty Sorry cann't add this Node")
            return
        if self.head == x:
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref
        if n.ref is None:
            print("No such Node find to add")
        else:
            new_node.ref = n.ref
            n.ref = new_node


    def search(self, key):
        n = self.head
        while n is not None:
            if n.data == key:
                return True
            n = n.ref
        return False


# ----------------DELETION IN SINGLE LINKED LIST--------------------


    def delete_begin(self):
        if self.head == None:
            print(" Linked list is Empty , Cann't delete ")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head == None:
            print(" Linked list is Empty , Cann't delete")
        else:
            n = self.head
            while (n.ref.ref != None):
                n = n.ref
            n.ref = None

    def delete_by_value(self,x):
        if self.head == None:
            print("Linked List is Empty")
            return
        if x == self.head.data:
            self.head =  self.head.ref
        else:
            n = self.head
            while n.ref is not None:
                if x == n.ref.data:
                    break
                n =  n.ref
            if n.ref is None:
                print("NO such Node Found")
            else:
                n.ref = n.ref.ref

obj =  SingleLinkedList()
obj.add_begin(11)
obj.add_begin(22)
obj.add_end(33)
obj.add_end(44)
obj.add_after(133,11)
obj.add_before(121,44)
obj.delete_begin()
obj.delete_end()
obj.Traversing()
print("---------------------------------------")
obj.delete_by_value(11)
obj.Traversing()
