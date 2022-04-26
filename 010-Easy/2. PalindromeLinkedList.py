# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def length(head: ListNode = None):
    cnt = 1
    curr = head
    # print(curr)
    while curr.next != None:
        curr = curr.next
        cnt += 1
    return cnt

class Solution:
    def isPalindrome(self, head: ListNode = None) -> bool:
        cnt = length(head)
        firstHalfList: [ListNode] = []
        secondHalfList: [ListNode] = []
        i = 0
        if cnt % 2 == 0:
            while head != None:
                n = head
                if i <= ((cnt / 2) - 1):
                    firstHalfList.append(n)
                else:
                    secondHalfList.append(n)
                head = head.next
                i += 1
        else:
            while head != None:
                n = head
                if i < ((cnt / 2) - 1):
                    firstHalfList.append(n)
                elif i < (cnt / 2) and i > ((cnt / 2) - 1):
                    pass
                else:
                    secondHalfList.append(n)
                head = head.next
                i += 1
        cnt = len(firstHalfList)
        # print("F", firstHalfList)
        # print("S", secondHalfList)
        j = cnt - 1
        for i in range(cnt):
            # print(i, firstHalfList[i].val)
            # print(j, secondHalfList[j].val)
            if firstHalfList[i].val != secondHalfList[j].val:
                return False
            j -= 1
        return True
