from Table import *
class parser:
    TOKENS={}
    TREES={}
    SYNTAXIS={}
    idSyntacis=0
    GRAMMAR={
        'units':{
            'generation':["I","II","III","IV","V","VI","VII","VIII","IX"],
            'lex':""
        },
        'tens':{
            'generation':["X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
            'lex':""
        },
        'hundreds':{
            'generation':["C","CC","CCC","CD","D","DC","DCC","DCC","CM"],
            'lex':""
        },
        'thousands':{
            'generation':["M","MM","MMM"],
            'lex':""
        },
        'dn':{
            'generation':[],
            'lex':""
        },
        'cn':{
            'generation':[],
            'lex':""
        },
        'mn':{
            'generation':[],
            'lex':""
        },
        'type':{
            'generation':["bin","hex","oct","rom","dec"],
            'lex':""
        },
        'conversion':{
            'generation':[],
            'lex':""
        }
    }
    def __init__(self):
        self.GRAMMAR['dn']['generation']=self.generateDN()
        self.GRAMMAR['cn']['generation']=self.generateCN(self.GRAMMAR['dn']['generation'])
        self.GRAMMAR['mn']['generation']=self.generateMN(self.GRAMMAR['cn']['generation'])
        self.GRAMMAR['conversion']['generation']=self.generateConversion()
        print("(U-U) Grammar has been created")
    def analize(self):
        print("(U-U) Parsing and analyzing syntaxis!")
        lines=self.TREES.values()
        print(lines)
        nline=0;
        for line in lines:
            tokens=line['instruction']
            if(tokens[0]== "begin"):
                print("First")
            elif(tokens[0]=="beginln" and tokens[1]=="convert" and tokens[2]=="rbgn"):
                roman=""
                i=3
                while tokens[i] != "rend":
                    roman+=tokens[i]
                    i+=1
                if self.isRoman(roman) and tokens[i]=="rend" and tokens[i+1]=="to":
                    i+=2
                    if(self.isType(tokens[i])):
                        self.idSyntacis+=1
                        self.addSyntaxis({
                            'id':self.idSyntacis,
                            'tokens':tokens
                        })
                    else:
                        print("(X_X) you have a syntaxis erro in "+" ".join(map(str,tokens)))
            elif(tokens[0]== "end"):
                print("Last")
    def treeParse(self,tableTokens):
        self.TOKENS=tableTokens
        if(self.TOKENS!= None and self.TOKENS!= {}):
            keys=self.TOKENS.keys()
            row=0
            instruction=[]
            for key in keys:
                if(row==self.TOKENS[key]['row']):
                   instruction.append(self.TOKENS[key]['token'])
                else:
                    self.addTree({
                        "id":self.TOKENS[key]['row'],
                        'instruction':instruction
                    })
                    row=self.TOKENS[key]['row']
                    instruction=[]
                    instruction.append(self.TOKENS[key]['token'])
            self.addTree({
                "id":self.TOKENS[key]['row'],
                'instruction':instruction
            })
            return True
        else:
            print("(-_-) I had a problem, I lose my TOKENS!!!")    
            return False
    def generateDN(self):
        dn=[]
        tens=self.GRAMMAR['tens']['generation']
        units=self.GRAMMAR['units']['generation']
        for unit in units:
            dn.append(unit)
        for ten in tens:
            dn.append(ten)
            for unit in units:
                dn.append(ten+unit)
        return dn
    def generateCN(self,dns):
        cn=[]
        hundreds=self.GRAMMAR['hundreds']['generation']
        for dn in dns:
            cn.append(dn)
        for hundred in hundreds:
            cn.append(hundred)
            for dn in dns:
                cn.append(hundred+dn)
        return cn
    def generateMN(self,cns):
        mn=[]
        thousands=self.GRAMMAR['thousands']['generation']
        for cn in cns:
            mn.append(cn)
        for thousand in thousands:
            mn.append(thousand)
            for cn in cns:
                mn.append(thousand+cn)
        return mn
    def generateConversion(self):
        conversion=[]
        gen=[]
        gen.append("convert")
        gen.append(self.GRAMMAR['mn']['generation'])
        gen.append('to')
        gen.append(self.GRAMMAR['type']['generation'])
        conversion.append(gen)
        gen=[]
        gen.append("convert")
        gen.append("number")
        gen.append('to')
        gen.append(self.GRAMMAR['type']['generation'])
        conversion.append(gen)
        gen=[]
        gen.append(self.GRAMMAR['mn']['generation'])
        gen.append(self.GRAMMAR['type']['generation'])
        conversion.append(gen)
    def isRoman(self,value):
        romans=self.GRAMMAR['mn']['generation']
        for roman in romans:
            if(value== roman):
                return True
        return False
    def isType(self,value):
        types=self.GRAMMAR['type']['generation']
        for _type in types:
            if(_type==value):
                return True
        return False
    def addTree(self,tree):
        self.TREES[tree['id']]={  
            'instruction':tree['instruction'],#array of tokens
            }
    def addSyntaxis(self,tokens):
        self.SYNTAXIS[tokens['id']]={  
            'tokens':tokens['tokens'],#array of tokens
            }

