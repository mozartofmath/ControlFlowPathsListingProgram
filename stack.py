
class stack():
    def __init__(self):
        self.l = []
        
    def length(self):
        return len(self.l)
    
    def isEmpty(self):
        return len(self.l)==0

    def s_push(self,item):
        self.l.append(item)
        
    def s_pop(self):
        return self.l.pop()

    def s_peek(self):
        return self.l[-1]