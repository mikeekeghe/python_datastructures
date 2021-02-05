class Node:
    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def print_list(self):
        cur_node = self.head
        while cur_node: # while current node is not null
            print (cur_node.data)
            cur_node = cur_node.next


    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head= new_node
            return

        last_node = self.head
        while last_node.next:
            last_node= last_node.next
        last_node.next=new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        # check if prev node given is in list
        if not prev_node:
            print ("previous node is not in the list")
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def len_iterative(self):
        count = 0
        cur_node = self.head

        while cur_node:
            count += 1
            cur_node = cur_node.next

        return count

    def delete_node_at_pos(self, pos):

        cur_node = self.head

        if pos == 0:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        count = 1
        while cur_node and count != pos:
            prev = cur_node
            cur_node = cur_node.next
            count += 1

        if cur_node is None:
            return

        prev.next = cur_node.next
        cur_node = None

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def is_palindrome(self):
            # Method 3
            p = self.head
            q = self.head
            prev = []

            i = 0
            while q:
                prev.append(q)
                q = q.next
                i += 1
            q = prev[i - 1]

            count = 1

            while count <= i // 2 + 1:
                if prev[-count].data != p.data:
                    return False
                p = p.next
                count += 1
            return True

    # Example palindromes:
    # RACECAR, RADAR

    # Example non-palindromes:
    # TEST, ABC, HELLO


lList = LinkedList()
lList.append("A")
lList.append("B")
lList.append("C")
lList.append("D")

# lList.insert_after_node(lList.head.next, "E")
# lList.prepend("E")
# lList.print_list()
print(lList.len_iterative())

