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

    # def print(self):
        # if self.head is None:
            # print('Empty List!')
            # return
# 
        # result = ''
        # node = self.head
# 
        # while node.next:
            # result += str(node.data) + '-->'
            # node = node.next
# 
        # print(result + str(node.data))
        # return
# 
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


if __name__== '__main__':
    l = LinkedList()

    l.insert_at_begining(1)
    l.insert_at_begining(3)
    l.insert_at_end(45)

    l.insert_values(['apple','orange','strawberry', 'lemons', 'grapes'])

    l.remove_at(5)

    print(l)