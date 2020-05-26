"""
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }


 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
"""
def addTwoNumbers(l1, l2):
    # Go down both lists at the same time, sum the elements, store the result in a new node
    # if sum is bigger than 9 (cause ech entry must be a digit) take the extra 1 and add it to the next sum
    carry = 0
    prev_node = None
    while l1 is not None or l2 is not None:
        if l1 and l2:
            # casual sum
            sum = l1.value + l2.value + carry
            l1 = l1.next
            l2 = l2.next
        elif l1:
            # l1 + carry from prev pair
            sum = l1.value + carry
            l1 = l1.next
        elif l2:
            sum = l2.value + carry
            l2 = l2.next
        if not prev_node:
            # setting up the return value, since we need to return the list of the same format as inputs
            new_head = ListNode(sum%10, prev_node)
            prev_node = new_head
        else:
            prev_node = ListNode(sum%10, prev_node)
        carry = sum//10
    return new_head