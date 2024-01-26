# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# initilaizing the list nodes
head = ListNode(x=1)
n2 = ListNode(x=2)
n3 = ListNode(x=3)
n4 = ListNode(x=4)

# link the list node
head.next = n2
n2.next = n3
n3.next = n4


def print_list(head: ListNode) -> None:
    print(f"val: {head.val}, next node: {head.next}")
    # add your logic here to print out the content of the link list


print_list(n2)



