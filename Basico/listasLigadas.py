class node:
    def __init__(self, data = None): #self es la instancia de la clase = this, __init__ = constructor
        self.data = data
        self.next = None #apuntador al siguiente nodo (none = null)

class linked_list:
    def __init__(self):
        self.head = node() #cabeza de la lista

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def lenght(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    
    def display(self):
        elems = [] #lista de elementos que existe en la lista ligada
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        if index >= self.lenght():
            print ("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == index:
                return cur_node.data
            cur_idx += 1

    def erase(self, index):
        if index >= self.lenght():
            print ("ERROR: 'Get' Index out of range!")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            lastNode = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                lastNode.next = cur_node.next
                return
            cur_idx += 1


my_list = linked_list()

my_list.append(2)
my_list.append(5)
my_list.append(1)
my_list.append(7)

my_list.display()

print("Element at 2nd index: ", my_list.get(1))

my_list.erase(1)

print("Lista despues de eleminar el segundo elemento: ", my_list.display())
