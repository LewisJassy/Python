# Initializing a Node
class Node:
    def __init__(self, data):
        self.data = data # assing data to node
        self.next = None # initialize next as null
# initialize the linked list class
class LinkedList:
    def __init__(self):
        self.head = None # Here we are stating that the head of the linked list is Noneat the beginning
    
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data) # create a new node
        new_node.next = self.head # link the new node to the current head
        self.head = new_node # make the new node the head of the linked list

    def insertAtEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None: # check if the new node is empty
            self.head = new_node # if it is empty, make it the head
            return
        last = self.head # start from the head
        while last.next: # move to the end of the list
            last = last.next # move to the next node
        last.next = new_node # link the new node to the last node

    def find_data(self, data):
        temp = self.head # start from the head
        while temp:
            if temp.data == data:
                return f"{data}"
            temp = temp.next
        print("Data not found in the list")

    def delteFromBeginning(self):
        if self.head is None: # check if the list is empty
            return "the list is empty"
        self.head = self.head.next # move to the next node and make it the head

    def deleteFromEnd(self):
        if self.head is None:
            return "The list is empty" 
        if self.head.next is None:
            self.head = None  # If there's only one node, remove the head by making it None
            return
        temp = self.head
        while temp.next.next:  # Otherwise, go to the second-last node
            temp = temp.next
        temp.next = None  # Remove the last node by setting the next pointer of the second-last node to None

    def search(self, value):
        current = self.head # start from the head
        position = 0 # initialize position to 0
        while  current: # move to the end of the list
            if current.data == value: # check if the value is found
                return f"Value {value} found at position {position}" # return the position of the value
            current = current.next # move to the next node
            position += 1 # increment the position
        return f"Value {value} not found in the list"
    
    def deleteAtPosition(self, postion):
        if self.head is None:
            return "The list is empty"
        new_node = self.head
        
        

    def print_list(self):
        temp = self.head  #start from the head
        while temp:
            print(temp.data, "") # print the data of the node
            temp = temp.next # move to the next node
        print() # print a new line

if __name__ == '__main__':
    # Create a new LinkedList instance
    llist = LinkedList()

    # Insert each letter at the beginning using the method we created
    llist.insertAtBeginning('fox') 
    llist.insertAtBeginning('brown') 
    llist.insertAtBeginning('quick')  
    llist.insertAtBeginning('the')  

    llist.insertAtEnd('jumps') 
    
    llist.find_data("fox")

    # Print the list before deletion
    # llist.print_list()

    # llist.delteFromBeginning()
    # llist.deleteFromEnd()

    print(llist.search(1))

    # Now 'the' is the head of the list, followed by 'quick', then 'brown' and 'fox'

    # Print the list
    llist.print_list()