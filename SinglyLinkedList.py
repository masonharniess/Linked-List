# Class for node creation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Class for list creation and node management
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Insert node at beginning
    def add_to_start(self, data):
        new_node = Node(data)
        # 1. Set the inserted node's next to point to the previous head
        new_node.next = self.head
        # 2. Set the head as the inserted node
        self.head = new_node

    # Insert node at end
    def add_to_end(self, data):
        new_node = Node(data)
        # 1. If list empty, set head to be inserted node
        if self.head is None:
            self.head = new_node
            return

        # 2. Get the last node
        #    Iterate until the last node is reached
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        # 3. Set the previous last node's next to be new node
        current_node.next = new_node

    def insert_at_index(self, data, index):
        if index < 0:
            raise IndexError(f"Index {index} out of bounds.")

        # 1. If the index is the head, call add_to_start()
        if index == 0:
            self.add_to_start(data)
            return

        # 2. Get the node before insertion point
        #    Iterate until the node before insertion point is obtained
        prev_node = self.head
        for _ in range(index - 1):
            # 2.2 If prev_node becomes None, the last node has been passed
            #     The list was shorter than index - 1
            if prev_node is None:
                raise IndexError(f"Index {index} is out of range.")
            prev_node = prev_node.next

        # 3. Check if final assignment in loop changed prev_node to None
        if prev_node is None:
            raise IndexError(f"Index {index} is out of range.")

        # 4. Splice in the new node
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node


    def update_node_at_index(self, data, index):
        if index < 0:
            raise IndexError(f"Index {index} is out of bounds.")

        # 1. Get the node to be updated
        current_node = self.head
        for _ in range(index):
            if current_node is None:
                raise IndexError(f"Index {index} is out of bounds.")
            current_node = current_node.next

        # 2. Check if final assignment in loop changed node to None
        if current_node is None:
            raise IndexError(f"Index {index} out of range.")

        # 3. Update node
        current_data = data

    def remove_first_node(self):
        if self.head is None:
            return

        self.head = self.head.next

    def remove_last_node(self):
        # 1. If list is empty, no action needed
        if self.head is None:
            return

        # 2. If only 1 element, clear the head
        if self.head.next is None:
            self.head = None
            return

        # 3. Get the node just before the last node
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next

        # 4. Remove last node by updating previous node's next
        current_node.next = None

    def remove_node_at_index(self, index):
        if index < 0:
            raise IndexError(f"Index {index} out of range.")

        # 1. If list is empty, no action needed
        if self.head is None:
            return

        # 2. If index points to head, update head
        if index == 0:
            self.head = self.head.next
            return

        # 3. Get the node before removal node
        prev_node = self.head
        for _ in range(index - 1):
            # 3.3 If final node is about to be stepped into, index is too large
            if prev_node.next is None:
                raise IndexError(f"Index {index} out of range.")
            prev_node = prev_node.next

        # 4. Check if final assignment in loop changed node to None
        if prev_node.next is None:
            raise IndexError(f"Index {index} out of range.")

        # 5. Remove node by updating previous node's next
        prev_node.next = prev_node.next.next

    def remove_node(self, data):
        # 1. If list is empty, no action needed
        if self.head is None:
            return

        # 2. If head holds the data, drop it
        if self.head.data == data:
            self.head = self.head.next
            return

        # 3. Iterate while looking one step ahead
        prev_node, current_node = self.head, self.head.next
        while current_node:
            if current_node.data == data:
                # 4. Remove node by severing connection
                prev_node.next = current_node.next
                return

            prev_node, current_node = current_node, current_node.head

        # 5. Raise ValueError if node not found
        raise ValueError(f"{data} not found in list.")

    def get_size(self):
        count = 0
        current_node = self.head
        while current_node:
            count += 1
            current_node = current_node.next
        return count

    def print_list(self):
        output = []
        current_node = self.head
        while current_node:
            output.append(current_node.data)
            current_node = current_node.next
        print(output)

# ----- EXAMPLE USE -----

# create a linked list
ll = SinglyLinkedList()

ll.add_to_start(1)
ll.add_to_end(2)
ll.insert_at_index(3, 1)

ll.print_list()                         # [1, 3, 2]

ll.update_node_at_index(16, 2)
ll.remove_first_node()
ll.remove_last_node()

ll.print_list() # [3]
print(ll.get_size()) # 4
