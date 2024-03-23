class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return 'Empty list!'

        result = '' 

        node = self.head

        while node.next:
            result += str(node.data) + '<->'
            node = node.next

        return result + str(node.data)

    def __len__(self):
        count = 0
        node = self.head

        while node:
            count += 1
            node = node.next
        
        return count 

    def insert_at_begining(self, data):
        node = Node(None, data, self.head)

        if self.head is None:
            self.head = node
            return

        self.head.prev = node
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(None, data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next
        
        node = Node(itr, data, None)
        itr.next = node

    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    def remove_at_begining(self):
        if self.head is None:
            return
        
        self.head = self.head.next

        if self.head is not None:
            self.head.prev = None

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

        if node.next is not None:
            node.next.prev = node

    def insert_at(self, index, data):
        if index < 0 or index > len(self):
            raise Exception('Index out of range!')
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head

        while count != index - 1:
            count += 1
            itr = itr.next

        node = Node(itr, data, itr.next)
        
        if itr.next is not None:
            itr.next.prev = node

        itr.next = node

    def insert_after_value(self, value, data_to_insert):
        if self.head is None:
            raise Exception('Empty list!')

        itr = self.head

        while itr:
            if itr.data == value:
                node = Node(itr, data_to_insert, itr.next)
                
                if itr.next is not None:
                    itr.next.prev = node
                
                itr.next = node
                return
            itr = itr.next

        raise Exception(f'Value <{value}> not found!')

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.remove_at_begining()
            return        

        itr = self.head 

        while itr:
            if itr.data == data:
                if itr.prev is not None:
                    itr.prev.next = itr.next
                if itr.next is not None:
                    itr.next.prev = itr.prev
                return
            itr = itr.next
    
    def print_forward(self):
        if self.head is None:
            print('Empty list!')
            return
        
        result = ''
        itr = self.head

        while itr.next:
            result += str(itr.data) + '-->'
            itr = itr.next

        print(result + str(itr.data))
        return

    def print_backward(self):
        if self.head is None:
            print('Empty list!')
            return
        
        result = str(self.head.data)
        itr = self.head.next

        while itr:
            result = str(itr.data) + '-->' + result
            itr = itr.next
        
        print(result)
        return

l = DoublyLinkedList()
l.insert_values(['banana', 'mango']) #'apple', 'orange', 'lemon', 'melon'])
print(l)
l.print_backward()
l.print_forward()