
#Clase Siguiente
class Follows(Lectores):
    siguiente=set()
    def __init__(self,terminales):
        self.non_terminals_=Lectores.get_nonterminals(self)
        self.terminals_=Lectores.get_terminals(self)
        self.productions_dict_=Lectores.get_productions_dict(self)
        self.starting_symbol_=Lectores.get_starting_symbol(self)
    def follow(self,nT):
        follow_ = set()
        prods = self.productions_dict.items()
        if nT==self.starting_symbol:
            follow_ = follow_ | {'$'}
        for nt,rhs in prods:
            #print("nt to rhs", nt,rhs)
            for alt in rhs:
                for char in alt:
                    if char==nT:
                        following_str = alt[alt.index(char) + 1:]
                        if following_str=='':
                            if nt==nT:
                                continue
                            else:
                                follow_ = follow_ | follow(nt)
                        else:
                            follow_2 = first(following_str)
                            if '@' in follow_2:
                                follow_ = follow_ | follow_2-{'@'}
                                follow_ = follow_ | follow(nt)
                            else:
                                follow_ = follow_ | follow_2
        #print("returning for follow({})".format(nT),follow_)
        siguiente=follow_
        return siguiente
