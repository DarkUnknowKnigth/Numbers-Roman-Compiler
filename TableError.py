from colorama import Fore,Style,Back
class errorTable:
    Table={}    
    def add(self,data):
        self.Table[data['id']]={ 
            'col':data['col'], 
            'row':data['row'],
            'token':data['token'],
            'lexema':data['lexema'],
            'type':data['type'],
            'type_error':data['type_error'],
            'description':data['description'],
            'etc':data['etc']
            }
    def show(self):
        values=self.Table.values()
        for value in values:
            print(value)
    def debug(self):
        keys=self.Table.keys()
        for key in keys:
            print(self.Table[key]['type_error'])
            print(self.Table[key]['description'])
            example=self.Table[key]['etc'].values()
            print("('-') Here:\n"+"\n\t"+example[0])
            print('\t>'+example[1])

