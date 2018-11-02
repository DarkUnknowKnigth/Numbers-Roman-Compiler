from Table import *
from Tokenize import *
import sys
import os
class Compiler:
    path=None
    filename=None
    code=None
    symbols=symbolTable()
    errors=symbolTable()
    tokenize=Tokenize()
    row=0
    col=0
    id=0
    def __init__(self,data):
        self.path=str(data[0])
        self.filename=str(data[1])
        print(":::::::::::::: Welcome to Compiler ::::::::::::\n:: I'm in: "+self.path+"\n:: I'll compile: "+self.filename)
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
                            'lexema':word
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
                                    'lexema':letter
                                })
                    else:
                        self.id+=1
                        self.symbols.add({
                            'id':self.id,
                            'col':self.col, 
                            'row':self.row,
                            'token':"ERROR",
                            'lexema':word
                        })
                    self.col+=1
            self.symbols.show()
        else:
            print("(o_o) Come on, You must put some text on your file!")
romanify = Compiler(sys.argv)
if(romanify.isPrepare()):
    romanify.start()
else:
    print("(-_-) You should put a file name in the same dir of the compiler!")