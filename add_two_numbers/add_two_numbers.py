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
    while l1.next is not None or l2.next is not None:
        if l1 and l2:
            # casual sum
        elif l1.next:
            # l1 + carry from prev pair
        elif l2.next: