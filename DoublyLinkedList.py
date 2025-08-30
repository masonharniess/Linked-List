# Class for node creation
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

# Class for list creation and node management
class DoublyLinkedList:
    def __init__(self):
        self.head = Node() # dummy head
        self.tail = Node() # dummy tail
        # Head’s next points to tail sentinel
        self.head.next = self.tail
        # Tail’s prev points to head sentinel
        self.tail.prev = self.head

    # Insert node after head (beginning)
    def add_to_start(self, data):
        new_node = Node(data)

        # 1. Get the head sentinel and the node after the head
        prev_node = self.head
        next_node = self.head.next
        # 2. Link the new node in between them
        new_node.prev = prev_node
        new_node.next = next_node
        # 3. Stitch the neighbours back to point at the new node
        prev_node.next = new_node
        next_node.prev = new_node

    # Insert node before tail (end)
    def add_to_end(self, data):
        new_node = Node(data)

        # 1. Get the last real node and the tail sentinel
        prev_node = self.tail.prev
        next_node = self.tail
        # 2. Link the new node in between them
        new_node.prev = prev_node
        new_node.next = next_node
        # 3. Splice in the new node
        prev_node.next = new_node
        next_node.prev = new_node

    def insert_at_index(self, data, index):
        if index < 0:
            raise IndexError(f"Index {index} is out of bounds.")

        # 1. Get the node before insertion point
        #    Iterate until the node before insertion point is obtained
        prev_node = self.head
        for i in range(index):
            # 1.1 If tail is about to be stepped-in-to, index is too large
            if prev_node.next is self.tail:
                raise IndexError(f"Index {index} is out of bounds.")
            prev_node = prev_node.next

        # 2. Get the node that will become the next node
        next_node = prev_node.next

        # 3. Splice in the new node
        new_node = Node(data)
        new_node.prev = prev_node
        new_node.next = next_node
        prev_node.next = new_node
        next_node.prev = new_node

    def update_node_at_index(self, data, index):
        if index < 0:
            raise IndexError(f"Index {index} is out of bounds.")

        # 1. Get the node to be updated
        #    Iterate until the node is reached
        current_node = self.head.next # first real node
        for _ in range(index):
            if current_node is self.tail:
                raise IndexError(f"Index {index} is out of bounds.")
            current_node = current_node.next

        # 2. If landed on the tail sentinel, index is out of range
        if current_node is self.tail:
            raise IndexError(f"Index {index} out of range.")

        # 3. Overwrite target node's data
        current_node.data = data

    def remove_first_node(self):
        prev_node = self.head
        next_node = self.head.next.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def remove_last_node(self):
        prev_node = self.tail.prev.prev
        next_node = self.tail
        prev_node.next = next_node
        next_node.prev = prev_node

    def remove_node_at_index(self, index):
        if index < 0:
            raise IndexError(f"Index {index} out of range.")

        # 1. Get the node before removal node
        prev_node = self.head
        for i in range(index):
            # 1.1 If tail is about to be stepped-in-to, index is too large
            if prev_node.next is self.tail:
                raise IndexError(f"Index {index} is out of bounds.")
            prev_node = prev_node.next

        # 2. Get the node after removal node
        next_node = prev_node.next.next

        # 3. Remove the intended node by severing the connection
        prev_node.next = next_node
        next_node.prev = prev_node

    # Remove first instance of data
    def remove_node(self, data):
        current_node = self.head.next

        # 1. Iterate through the nodes
        while current_node is not self.tail:
            # 2. Perform action when data is found
            if current_node.data == data:
                # 3. Get the previous and next node
                prev_node = current_node.prev
                next_node = current_node.next
                # 4. Remove the intended node by severing the connection
                prev_node.next = next_node
                next_node.prev = prev_node
                return

            current_node = current_node.next

        # 4. Return value error if data not matched
        raise ValueError(f"{data} not found in list.")

    def get_size(self):
        count = 0
        current_node = self.head.next
        while current_node is not self.tail:
            count += 1
            current_node = current_node.next
        return count

    def print_list(self):
        output = []
        current_node = self.head.next # skip dummy head
        while current_node is not self.tail: # stop before dummy tail
            output.append(current_node.data)
            current_node = current_node.next
        print(output)

# ----- EXAMPLE USE -----

ll = DoublyLinkedList()

ll.add_to_start(4)
ll.print_list()                             # [4]
ll.add_to_end(3)
ll.print_list()                             # [4, 3]
ll.insert_at_index(7, 1)
ll.print_list()                             # [4, 7, 3]
ll.update_node_at_index(1, 2)
ll.print_list()                             # [4, 7, 1]
ll.remove_first_node()
ll.print_list()                             # [7, 1]
ll.remove_last_node()
ll.print_list()                             # [7]
ll.remove_node_at_index(0)
ll.print_list()                             # []
list_size = ll.get_size()
print(list_size)                            # 0
