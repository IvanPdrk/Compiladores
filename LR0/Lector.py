
#Clase Lectores
class Lectores:
    gramatic=set()
    terminals=set()
    non_terminals=set()
    alternatives=""
    production_dict={}
    #Lee el archivo de entrada
    def __init__(self):
        self.txt=open('gramatic.txt','r')
        self.gramatic=self.txt.readlines()
        self.non_terminals=[]
        self.terminals=[]
        self.starting_symbol=""
        self.productions_dict={}
        self.alternatives=[]
        band=1
        for production in self.gramatic:
            for letter in production:
                if band==1:
                    self.starting_symbol=letter
                    self.non_terminals.append(letter)
                    band=0
                elif letter not in self.non_terminals and letter not in self.terminals:    
                    if letter.isupper():
                        self.non_terminals.append(letter)
                    elif letter.islower():
                        self.terminals.append(letter) 
        #print(self.non_terminals)
        #print(self.terminals)
        #Creacion Diccionario 
        #productions_dict={}
        for nT in self.non_terminals:
            self.productions_dict[nT] = []
        print(self.productions_dict)
        for production in self.gramatic:
            #print("production:"+production)
            nonterm_to_prod = production.split("->")
            #print(nonterm_to_prod)
            self.alternatives = nonterm_to_prod[1][:-1].split("/")
            #print(alternatives)
            for alternative in self.alternatives:
                self.productions_dict[nonterm_to_prod[0]].append(alternative)

        print(self.productions_dict)
            
    #print productions list
    def show(self):
        print(list(self.gramatic))
    
    def get_terminals(self):
        return self.terminals

    def get_nonterminals(self):
        return self.non_terminals

    def get_productions_dict(self):
        return self.productions_dict

    def get_starting_symbol(self):
        return self.starting_symbol
    
    def get_alternatives(self):
        return self.alternatives
