# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def test(sum):
            carry=0
            if sum>=10:
                carry = sum//10
                sum = sum%10
            a=ListNode()
            a.val=sum
            return (a,carry)
        res=[]
        carry=0
        while True:
            
            # all possible case:
            # if last l1.ele
            # if both elements are last: break

            # if (l1 and l2 and l1.next is None and l2.next is None):
            #     print('l1.next is None and l2.next is None')
            #     sum = l1.val+l2.val+carry
            #     a,carry = test(sum)
            #     if res: res.append(a) 
            #     else:
            #         res[-1].next=a
            #         res.append
            #     if carry>0:
            #         b=ListNode(val=carry)
            #         res[-1].next=b
            #         res.append(b)
            #     break

            if l1 and l2:
                sum=l2.val+l1.val+carry
                l1=l1.next
                l2=l2.next
            elif l1 is None and l2 is None:
                # print('final carry:',carry)
                if carry>0:
                    b=ListNode(val=carry)
                    res[-1].next=b
                    res.append(b)
                return res[0]
            elif l1 is None:
                sum = l2.val+carry
                l2 = l2.next
            elif l2 is None:
                sum = l1.val + carry
                l1 = l1.next
            a,carry = test(sum)
            # print('sum:',a.val,' carry:',carry)
            if res:
                res[-1].next=a
                res.append(a)
            else:
                res.append(a)