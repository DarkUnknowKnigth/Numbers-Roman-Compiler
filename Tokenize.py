
import re
class Tokenize:
    ROMAN ={
        'I':{
            "lex":"I",
            "regex":r'\bI\b',
            "decimal":"1"
        },  
        'V':{
            "lex":"V",
            "regex":r'\bV\b',
            "decimal":"5"
        },
        'X':{
            "lex":"X",
            "regex":r'\bX\b',
            "decimal":"10"
        },  
        'L':{
            "lex":"L",
            "regex":r'\bL\b',
            "decimal":"50"
        },
        'C':{
            "lex":"C",
            "regex":r'\bC\b',
            "decimal":"100"
        },   
        'D':{
            "lex":"D",
            "regex":r'\bD\b',
            "decimal":"500"
        },    
        'M':{
            "lex":"M",
            "regex":r'\bM\b',
            "decimal":"1000"
        }  
    }
    RESERVED={
        'convert':{
            "lex":"convert",
            "regex":"convert",
        },
        'to':{
            "lex":"to",
            "regex":r'\bto\b',
        },
        'dec':{
            "lex":"dec",
            "regex":r"\bdec\b",
        },
        'oct':{
            "lex":"oct",
            "regex":r"\boct\b",
        },
        'bin':{
            "lex":"bin",
            "regex":r"\bbin\b",
        },
        'hex':{
            "lex":"hex",
            "regex":r"\bhex\b"
        },
        'rom':{
            'lex':'rom',
            'regex':r"\brom\b"
        }
    }
    NUMBER={
        'number':{
            "regex":r"^[0-9]"
        }
    }
    romaKeys = ROMAN.keys()
    reservedKeys=RESERVED.keys()    
    ##METODOS 
    def isRomanNumber(self,word):
        for letter in word:
            if letter == 'I' or letter =="V" or letter == "X" or letter == 'L' or letter =="C" or letter == "D" or letter == 'M' :
                None   
            else:
                return False
        return True        
    def isRoman(self,charter):#si es romano?
        for key in self.romaKeys: #iteramos las llaves del diccionario
            if(re.match(self.ROMAN[key]['regex'],charter)): #si la expresion regular de la llave conicide
                return True    #si conicide return true
        return False #no conicide nunca no es romano retunr false
    def roman_values(self,charter):
        if(self.isRoman(charter)):
            for key in self.romaKeys:
                if(re.match(self.ROMAN[key]['regex'],charter)):
                    return self.ROMAN[key]['lex']
        else:
            return "ERROR"
    def isReserved(self,charter):
        for key in self.reservedKeys: 
            if(re.match(self.RESERVED[key]['regex'],charter)): 
                return True    
        return False
    def reserved_values(self,charter):
        if(self.isReserved(charter)):
            for key in self.reservedKeys:
                if(re.match(self.RESERVED[key]['regex'],charter)):
                    return (self.RESERVED[key]['lex'])
        else:
            return ("Invalid Reserved Token","the charter: "+charter+" is invalid")
    def isNumber(self,charter):
        if(re.match(self.NUMBER['number']['regex'],charter)):
            return True
        else:
            return False



