# -*- coding: utf-8 -*-
"""14 assignment

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KgGznIRZzQoOZIqDzL8WQ1R32wvLknsB
"""

#1solution

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeLoop(head):
    if head is None or head.next is None:
        return head

    slow = head
    fast = head

    # Detect loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # If no loop is present
    if slow != fast:
        return head

    # Find the node just before the starting point of the loop
    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    # Remove the loop
    fast.next = None

    return head

#2solution



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reverseLinkedList(head):
    prev = None
    current = head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next

    return prev

def addOne(head):
    if head is None:
        return head

    # Reverse the linked list
    head = reverseLinkedList(head)

    # Add 1 to each digit
    current = head
    carry = 1

    while current:
        current.value += carry
        carry = current.value // 10
        current.value %= 10
        previous = current
        current = current.next

    # Add the remaining carry as a new node if it exists
    if carry > 0:
        previous.next = Node(carry)

    # Reverse the linked list again
    head = reverseLinkedList(head)

    return head

#3solution

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.bottom = None

def mergeSortedLists(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.value <= head2.value:
        new_head = head1
        head1 = head1.bottom
    else:
        new_head = head2
        head2 = head2.bottom

    current = new_head

    while head1 and head2:
        if head1.value <= head2.value:
            current.bottom = head1
            head1 = head1.bottom
        else:
            current.bottom = head2
            head2 = head2.bottom
        current = current.bottom

    if head1:
        current.bottom = head1
    if head2:
        current.bottom = head2

    return new_head

def flattenLinkedList(head):
    if head is None or head.next is None:
        return head

    # Merge the sub-linked lists one by one
    current = head
    while current.next:
        current.next = mergeSortedLists(current.bottom, current.next.bottom)
        current = current.next

    return head.bottom

#4solution

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.random = None

def copyRandomList(head):
    if head is None:
        return None

    # Create a dictionary to store the mapping between original and copied nodes
    node_map = {}

    # Create the copied nodes
    current = head
    while current:
        new_node = Node(current.val)
        node_map[current] = new_node
        current = current.next

    # Set the next and random pointers of the copied nodes
    current = head
    while current:
        copied_node = node_map[current]
        copied_node.next = node_map.get(current.next)
        copied_node.random = node_map.get(current.random)
        current = current.next

    return node_map[head]

#5solution

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def oddEvenList(head):
    if head is None or head.next is None:
        return head

    odd_head = head
    even_head = head.next
    odd = odd_head
    even = even_head

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head

    return odd_head

#6solution

class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

def leftShiftLinkedList(head, k):
    if head is None or head.next is None:
        return head

    # Find the length of the linked list
    list_length = 0
    current = head
    while current:
        list_length += 1
        current = current.next

    # Calculate the effective number of shifts
    k = k % list_length

    if k == 0:
        return head

    new_head = head
    last_node = head

    # Traverse to the position of the new head
    for _ in range(list_length - k - 1):
        new_head = new_head.next

    last_node = new_head

    # Traverse to the last node of the original list
    while last_node.next:
        last_node = last_node.next

    # Perform the left-shift by updating pointers
    new_head, last_node.next = new_head.next, None
    last_node.next = head

    return new_head

