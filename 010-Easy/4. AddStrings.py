class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        
        carry = 0
        t1_cnt = len(num1) - 1
        t2_cnt = len(num2) - 1
        
        while t1_cnt >= 0 or t2_cnt >= 0:
            n1 = ord(num1[t1_cnt]) - ord('0') if t1_cnt >= 0 else 0
            n2 = ord(num2[t2_cnt]) - ord('0') if t2_cnt >= 0 else 0
            
            value = (n1 + n2 + carry) % 10
            carry = (n1 + n2 + carry) // 10
            
            result.append(value)
            
            t1_cnt -= 1
            t2_cnt -= 1
        
        if carry > 0:
            result.append(carry)
            
        return "".join([str(r) for r in result[::-1]])
