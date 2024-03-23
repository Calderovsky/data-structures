class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return 'Empty list!'
        result = ''

        node = self.head

        while node.next:
            result += str(node.data) + '-->'
            node = node.next
        
        return result + str(node.data)

    def __len__(self):
        length = 0
        itr = self.head

        while itr:
            length += 1
            itr = itr.next
        
        return length
 
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = node

    def insert_values(self, data_list):
        self.head = None

        for element in data_list:
            self.insert_at_end(element)

    def remove_at_begining(self):
        if self.head is None:
            raise Exception('Cannot remove items from an empty list!')
        
        self.head = self.head.next
        
    def remove_at(self, index):
        if index < 0 or index >= len(self):
            raise Exception('Index out of range!')

        if index == 0:
            self.remove_at_begining()
            return

        count = 0
        node = self.head

        while count != index - 1:
            count += 1
            node = node.next
        
        node.next = node.next.next 

    def insert_at(self, index, data):
        if index < 0 or index > len(self):
            raise Exception('Invalid index!')

        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        prev_node = self.head

        while count != index - 1:
            count += 1
            prev_node = prev_node.next
        
        node = Node(data, prev_node.next)
        prev_node.next = node

    def insert_after_value(self, value, data_to_insert):
        if self.head is None:
            raise Exception('Empty list!')
        
        current_node = self.head
        
        while current_node:
            if current_node.data == value:
                node = Node(data_to_insert, current_node.next)
                current_node.next = node
                return

            current_node = current_node.next
        
        raise Exception(f'Value <{value}> not found!')

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.remove_at_begining()
            return

        prev_node = self.head
        while prev_node.next:
            if prev_node.next.data == data:
                prev_node.next = prev_node.next.next
                return

            prev_node = prev_node.next

        return



if __name__== '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    print(ll)
    ll.remove_by_value("orange") # remove orange from linked list
    print(ll)
    ll.remove_by_value("figs")
    print(ll)
    ll.remove_by_value("banana")
    print(ll)
    ll.remove_by_value("mango")
    print(ll)
    ll.remove_by_value("apple")
    print(ll)
    ll.remove_by_value("grapes")
    print(ll)