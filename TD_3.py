# -*- coding: utf-8 -*-



class Tree : 
    
    def __init__(self, label, *children):
        """create a Tree"""
        self.__label=label
        self.__children=children
    
    def label (self):
        """return the label of the Tree"""
        return self.__label
    
    def children (self):
        """return all the children of the Tree"""
        return self.__children
    
    def nb_direct_children (self):
        """return the number of direct children of the Tree"""
        under_Tree=self.children()
        return len(under_Tree)
    
    def nb_children (self):
        """return the number of all the nodes and leafs of the Tree"""
        counter=0
        for child in self.children():
            if child.nb_direct_children()==0:
                counter += 1
            else :
                counter=counter+1+child.nb_children()
        return counter
    
    def child(self, i):
        """return the ith child of the Tree""" 
        if i>self.nb_children()-1:
            raise ValueError('The index corresponds to a child that does not exist')
        under_Tree=self.children()
        return under_Tree[i]
    
    def is_leaf(self):
        """return True if the Tree is a leaf"""
        if self.nb_direct_children()==0:
            return True
        else :
            return False
        
    def depth (self):
        """return the maximum depth of the Tree"""
        max_depth=0
        for child in self.children():
            depth=1
            if not child.is_leaf():
                depth+=child.depth()
            if depth>max_depth:
                max_depth=depth
        return max_depth 
    
    def __eq__ (self, other):
        """define the '==' symbol for the Trees"""
        test=True
        
        if self.label()!=other.label() or self.nb_direct_children()!=other.nb_direct_children():
            test=False
        
        counter=self.nb_direct_children()
        if test :
            for i in range(counter):
                if self.child(i)!=other.child(i):
                    test=False
        return test
    
    def __str__ (self):
        """allows you to display a Tree"""
        if not self.is_leaf():
            children=""
            for child in self.children():
                children=children+child.__str__()+","
            return f"{self.label()}({children[:-1]})"
        return f"{self.label()}"
    
    
    def deriv(self,var):
        """derivate a polynom wrote as a Tree"""
        var_tree=Tree(var)
        if self.label()=='*':
            constant=1
            for term in self.children():                
                if term.is_leaf():
                    if term.label() != var:
                        constant=int(term.label())
            var_power=self.depth()
            constant=constant*var_power
            if var_power-1==0:
                return Tree(str(constant))
            elif var_power-1==1:
                return Tree('*',Tree(str(constant)),var_tree)
            else :
                power_tree=Tree('*',var_tree,var_tree)
                for i in range(var_power-3):
                    power_tree=Tree('*',var_tree,power_tree)
                return Tree('*',Tree(str(constant)),power_tree)
            
        if self.label()=='+':
            
            term_1=self.child(0)
            
            if term_1.is_leaf() and term_1.label()!=var:
                term_1_derivate=Tree('0')
            elif term_1.label()==var:
                term_1_derivate=Tree('1')
            else:
                term_1_derivate=term_1.deriv(var)
                
            term_2=self.child(1)
            
            if term_2.is_leaf() and term_2.label()!=var:
                term_2_derivate=Tree('0')
            elif term_2.label()==var:
                term_2_derivate=Tree('1')
            else:
                term_2_derivate=term_2.deriv(var)            
                
            return Tree('+',term_1_derivate,term_2_derivate)
                
                
                        
                    
        
        
        
        
        


if __name__=='__main__':
    a=Tree('1')
    b=Tree('2',a)
    bbis=Tree('2',a)
    c=Tree('c',a,b)
    assert c.nb_children()==3
    assert b==bbis
    assert c.child(1)==b
    assert a.is_leaf()
    polynom=Tree('+',Tree('*',Tree('3'),Tree('*',Tree('X'),Tree('X')))
                 ,Tree('+',Tree('*',Tree('5'),Tree('X')),Tree('7')))
    polynom_derivate=Tree('+',Tree('*',Tree('6'),Tree('X')),
                          Tree('+',Tree('5'),Tree('0')))
    assert polynom.deriv('X')==polynom_derivate
    polynom_2=Tree('+',Tree('*',Tree('3'),Tree('*',Tree('X'),Tree('*',Tree('X'),Tree('X'))))
                 ,Tree('+',Tree('*',Tree('5'),Tree('X')),Tree('7')))
    polynom_2_derivate=Tree('+',Tree('*',Tree('9'),Tree('*',Tree('X'),Tree('X'))),
                          Tree('+',Tree('5'),Tree('0')))
    assert polynom_2.deriv('X')==polynom_2_derivate