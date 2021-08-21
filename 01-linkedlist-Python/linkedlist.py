"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        # Your code goes here
        temp = self.head
        while(temp):
            temp = temp.next
        temp = new_element
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        i = 1
        temp = self.head
        while(i <= position):
            temp = temp.next
            i += 1
        return temp
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        i = 1
        temp = self.head
        while(i <= position):
            temp = temp.next
            i += 1
        if(temp):
            nxt = temp.next
            temp.next = new_element
            new_element.next = nxt
        else:
            temp = new_element
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        temp = self.head
        prev = None
        while(temp.value != value):
            perv = temp
            temp = temp.next
        prev.next = temp.next