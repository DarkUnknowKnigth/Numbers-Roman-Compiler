from Table import *
from Tokenize import *
from TableError import *
import sys
import os
class Compiler:
    path=None
    filename=None
    code=None
    symbols=symbolTable()
    errors=errorTable()
    tokenize=Tokenize()
    row=0
    col=0
    id=0
    idr=0
    def __init__(self,data):
        self.path=str(data[0])
        self.filename=str(data[1])
        print("::::::::::::::::::Welcome to the compiler :::::::::::::::\n\n:: I'm in: "+self.path+"\n:: I'll compile: "+self.filename+"\n\n:::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    def isPrepare(self):
        if self.path == None and self.filename == None:
            return False
        else:
            extension= self.filename.split(".")
            if extension[1] == "pyrx":
                return True
            else:
                print("(-_-) You should save your file with a .pyrx extension!")
                return False
    def start(self):
        try:
            file=open(self.filename,mode='r')
            self.code=file.read()
            file.close()
        except:
            print("(*-*) I can't open your file!")
            exit()
        if(self.code!=None and len(self.code)>0):
            lines=self.code.split('\n')
            for line in lines:
                self.row+=1
                words=line.split(' ')
                for word in words:
                    if(self.tokenize.isReserved(word)):
                        self.id+=1
                        self.col+=len(word)
                        self.symbols.add({
                            'id':self.id,
                            'col':self.col, 
                            'row':self.row,
                            'token':self.tokenize.reserved_values(word),
                            'lexema':word,
                            'type':type (word).__name__
                        })
                    elif(self.tokenize.isNumber(word)):
                        self.col+=len(word)
                        self.id+=1
                        self.symbols.add({
                            'id':self.id,
                            'col':self.col, 
                            'row':self.row,
                            'token':"number",
                            'lexema':int(word),
                            'type':type (int(word)).__name__
                        })
                    elif(self.tokenize.isRomanNumber(word)):
                        for letter in word:
                            self.col+=1
                            if(self.tokenize.isRoman(letter)):
                                self.id+=1
                                self.symbols.add({
                                    'id':self.id,
                                    'col':self.col, 
                                    'row':self.row,
                                    'token':self.tokenize.roman_values(letter),
                                    'lexema':letter,
                                    'type':type (letter).__name__
                                })
                    else:
                        self.idr+=1
                        self.col+=len(word)
                        self.errors.add({
                            'id':self.idr,
                            'col':self.col, 
                            'row':self.row,
                            'token':"ERROR",
                            'lexema':word,
                            'type':type (word).__name__,
                            'type_error':"(#_#) Invalid sintaxis error: "+line+" in line:"+str(self.row)+" in col:"+str(self.col),
                            'description':"(=_=) You code have this word: "+word+" and I don't know whats means...",
                            'etc':{
                                "line":line,
                                "word":word,
                            }
                        })
                    self.col+=1
                self.id+=1
                self.symbols.add({
                            'id':self.id,
                            'col':self.col, 
                            'row':self.row,
                            'token':"end",
                            'lexema':"end",
                            'type':type("end").__name__
                        })
                self.col=0
            self.errors.debug()
            self.symbols.show()
        else:
            print("(o_o) Come on, You must put some text on your file!")
romanify = Compiler(sys.argv)
if(romanify.isPrepare()):
    romanify.start()
else:
    print("(-_-) You should put a file name in the same dir of the compiler!")