import sys
sys.setrecursionlimit(60)
#Clase Primeros
class Primeros(Lectores):
    primero=set()

    def __init__(self):
        Lectores.__init__(self)        #Lectores constructor
        self.terminals_=Lectores.get_terminals(self)
        self.non_terminals_=Lectores.get_nonterminals(self)
        self.productions_dict_=Lectores.get_productions_dict(self)
        self.alternatives=Lectores.get_alternatives(self)
        self.starting_symbol=Lectores.get_starting_symbol(self)

        self.FIRST = {}
        for self.non_terminal in self.non_terminals:
            self.FIRST[self.non_terminal] = set()
            self.FIRST[self.non_terminal] = self.FIRST[self.non_terminal] | first(self.non_terminal)
        #print("terminals from primeros"+str(self.terminals))
        #print("non-terminals from primeros"+str(self.non_terminals))
        #print("PD from primeros"+str(self.productions_dict_))


    #show funtion
    def showfirstof(self,string):
        return self.FIRST[string]


    #First Process
    def first(self,string):
        #print("first({})".format(string))
        self.first_ = set()
        if string in self.non_terminals:
            self.alternatives = self.productions_dict[string]

            for alternative in self.alternatives:
                self.first_2 = first(self,alternative)    #Recursive call
                self.first_ = self.first_ |self.first_2

        elif string in self.terminals:
            self.first_ = {string}

        elif string=='' or string=='@':
            self.first_ = {'@'}

        else:
            self.first_2 = self.first(string[0])
            if '@' in self.first_2:
                i = 1
                while '@' in self.first_2:
                    #print("inside while")

                    self.first_ = self.first_ | (self.first_2 - {'@'})
                    #print('string[i:]=', string[i:])
                    if string[i:] in self.terminals:
                        self.first_ = self.first_ | {string[i:]}
                        break
                    elif string[i:] == '':
                        self.first_ = self.first_ | {'@'}
                        break
                    self.first_2 = first(string[i:])
                    self.first_ = self.first_ | self.first_2 - {'@'}
                    i += 1
            else:
                self.first_ = self.first_ | self.first_2


        print("returning for first({})".format(string,self.first_))
        #self.primero=self.first_
        return self.first_
