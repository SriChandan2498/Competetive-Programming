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
        current = self.head
        node = Element(new_element)
        if self.head:
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # Your code goes here
        current = self.head
        count = 1
        while (current):
            if (count == position):
                return current.value
            count += 1
            current = current.next
        return None
                           
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # Your code goes here
        current = self.head

        if position == 1:
            newNode = Element(new_element)
            newNode.next = current
            current = newNode          
        else:        
            while position != 0:          
                position -= 1
                if (position == 1):  
                    newNode = Element(new_element)
                    newNode.next = current.next
                    current.next = newNode
                    break
                
                current = current.next
                if current == None:
                    break 
    
    
    def delete(self, value):
        """Delete the first node with a given value."""
        # Your code goes here
        current = self.head
        if current:
            if current.value == value:
                self.head = current.next
                current = None
                return
        while current:
            if current.value == value:
                break
            current = current.next 
        if(current == None):
            return 
        current = None