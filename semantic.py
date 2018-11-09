from Parser import *
class semantic:
    parser=parser()
    STACK_OPERATING=[]
    STACK_OPERATOR=[]
    def addStackOperator(self,operator):
        if(len(self.STACK_OPERATOR)>0):
            if(self.STACK_OPERATOR[0]=="convert"):
                self.cuadrupo()
            self.STACK_OPERATOR.append(operator)
    def addStackOperating(self,operating):
        self.STACK_OPERATING.append({
            'operating':str(operating),
            'type':type(operating).__name__
        })
    def topStackOperator(self):
        return self.STACK_OPERATOR[len(self.STACK_OPERATOR)]
    def topStackOperating(self):
        return self.STACK_OPERATING[len(self.STACK_OPERATING)]
    def popStakOperator(self):
        self.STACK_OPERATOR.pop()
    def popStakOperating(self):
        self.STACK_OPERATING.pop()
    def addSyntaxis(self,tokens):
        print(tokens)
        for token in tokens:
            if token=="convert":
                self.addStackOperator(token)
            elif self.parser.isRoman(token):
                self.addStackOperating(token)
            elif self.parser.isType(token):
                self.addStackOperating(token)
    def cuadrupo(self):
        print("op: "+self.topStackOperator()+" op1: "+self.topStackOperating()+" op2: "+self.topStackOperating())
        self.popStakOperator()
        self.popStakOperating()
        self.popStakOperating()
        
         
    
