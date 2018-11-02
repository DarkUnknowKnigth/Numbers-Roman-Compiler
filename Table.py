class symbolTable:
    Table={}    
    def add(self,data):
        self.Table[data['id']]={ 
            'col':data['col'], 
            'row':data['row'],
            'token':data['token'],
            'lexema':data['lexema'],
            'type':data['type']
            }
    def show(self):
        values=self.Table.values()
        for value in values:
            print(value)
