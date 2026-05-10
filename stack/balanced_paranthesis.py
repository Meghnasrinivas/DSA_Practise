class BalancedParanthesis:
    def __init__(self):
        self.stack=[]
        self.opening='({['
        self.closing=')}]'
        self.mapping={')':'(', '}':'{', ']':'['}

    def is_balanced(self,exp):
        for char in exp:
            if char in self.opening:
                self.stack.append(char)
            elif char in self.closing:
                if not self.stack or self.stack[-1]!=self.mapping[char]:
                    return False
                else:
                    self.stack.pop()
        return len(self.stack)==0
    
bp=BalancedParanthesis()
print(bp.is_balanced('(){}[]')) #True
print(bp.is_balanced('({[)]}')) #False

