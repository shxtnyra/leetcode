"""
https://leetcode.com/problems/add-two-numbers/

Вам даны два связанных списка, представляющие два неотрицательных целых числа.
Цифры хранятся в обратном порядке, и каждый из их узлов содержит одну цифру.
Сложите два числа и верните сумму в виде связанного списка.

Вы можете предположить, что эти два числа не содержат ведущих нулей, кроме самого числа 0.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def add_two_numbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        mod = 0

        while l1 or l2 or mod:
            sum = mod
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            cur.next = ListNode(sum % 10)
            mod = sum // 10
            cur = cur.next

        return dummy.next



def print_list_node(l):
    while l is not None:
        print(l.val, end=' ')
        l = l.next
    print("")

def return_data_one():
    l13 = ListNode(3)
    l12 = ListNode(4, l13)
    l11 = ListNode(2, l12)

    l23 = ListNode(4)
    l22 = ListNode(6, l23)
    l21 = ListNode(5, l22)

    return l11, l21

def return_data_two():
    l1 = ListNode(0)
    l2 = ListNode(0)
    return l1, l2

def return_data_three():
    l17 = ListNode(9)
    l16 = ListNode(9, l17)
    l15 = ListNode(9, l16)
    l14 = ListNode(9, l15)
    l13 = ListNode(9, l14)
    l12 = ListNode(9, l13)
    l11 = ListNode(9, l12)

    l24 = ListNode(9)
    l23 = ListNode(9, l24)
    l22 = ListNode(9, l23)
    l21 = ListNode(9, l22)

    return l11, l21

sol = Solution()

data = return_data_one()
print_list_node(data[0])
print_list_node(data[1])
print_list_node(sol.add_two_numbers(data[0], data[1]))

print("----")

data = return_data_two()
print_list_node(data[0])
print_list_node(data[1])
print_list_node(sol.add_two_numbers(data[0], data[1]))

print("----")

data = return_data_three()
print_list_node(data[0])
print_list_node(data[1])
print_list_node(sol.add_two_numbers(data[0], data[1]))

