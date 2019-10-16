"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next
        return self.next;

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
        return self.prev;

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        if(self.head):
            n = self.head.insert_before(value);
        else:
            n = ListNode(value, None, None);
            self.tail = n;
        self.head = n;
        self.length += 1;
        return n;

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if(not self.head): 
            return None;
        a = self.head.value;
        if(self.tail == self.head):
            self.tail = None;
            self.head = None;
            self.length = 0;
            return a;
        b = self.head;
        self.head = self.head.next;
        b.delete();
        self.length -= 1;
        
        return a;
    """Wraps the given value in a ListNode and inserts it
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        if(self.tail):
            n = self.tail.insert_after(value);
        else:
            n = ListNode(value);
            self.head = n;
        self.tail = n;
        self.length += 1;
        return n;

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if(not self.tail):
            return None;
        a = self.tail.value;
        if(self.tail == self.head):
            self.tail = None;
            self.head = None;
            self.length = 0;
            return a;
        b = self.tail;
        self.tail = self.tail.next;
        b.delete(); #delete only removes relations doesnt actually remove object from memory
        self.length -= 1;
        return a;

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        #unlink me from the spot im at
        if(node.prev):
            node.prev.next = node.next;
            if(node == self.tail and len(self) > 1):
                self.tail = node.prev;
        if(node.next):
            node.next.prev = node.prev;
                
        
        #add me to the front
        self.head.prev = node;
        node.next = self.head;
        node.prev = None;
        
        #reset head
        self.head = node;


    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        #unlink me from the spot im at
        if(node.prev):
            node.prev.next = node.next;
        if(node.next):
            node.next.prev = node.prev;
            if(node == self.head and len(self) > 1):
                self.head = node.next
        
        #add me to the back
        self.tail.next = node;
        node.prev = self.tail;
        node.next = None;
        
        #reset tail
        self.tail = node;

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        n = self.head;
        if(node == self.head): #special case when the len = 1 so handle the head first to save on time
            self.head.delete;
            self.head = self.head.next;
            self.tail = self.tail.next if self.tail == node else self.tail;
            self.length -= 1;
            return;
        n = self.head;
        while(n.next): #does index 1...N
            n = n.next;
            if(n == node):
                node.delete;
                self.length -= 1; #remember to only lower the length if we found a value.
                break; #we only need to find one
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        h = self.head.value;
        
        n = self.head;
        while(n.next): #does 1...N
            n = n.next;
            if(h < n.value):
                h = n.value;
        return h;
    
    def __str__(self):
        if(not self.head):
            return "[ ]";
        a = "[ ";
        n = self.head;
        while(n.next):
            a += " "+ str(n.value)+","
            n = n.next;
        return a + str(n.value) + " ]";
