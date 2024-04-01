# -*- coding: utf-8 -*-
from math import pi


def pgcd(a, b):
    """returns the greatest common divisor of a and b"""
    if b>a:
        a,b=b,a
    if b==0:
        return a 
    r=a%b
    return pgcd(b,r)

def ppcm(a,b):
    """returns the smallest common multiplier of a and b"""
    return a*b/pgcd(a,b)
    


class Fraction:
    def __init__(self,numerator,denominator):
        """create a fraction"""
        if type(numerator)!=int or type(denominator)!=int:
            raise ValueError('Denominator and numerator must be integrer')
        else:
            if denominator==0:
                raise ValueError('Denominator must be nonzero')
            self.__num=numerator
            self.__den=denominator
            
    def __eq__(self,other):
        """test if two fractions are equal"""
        frac1=Fraction(self.num(),self.den())
        frac2=Fraction(other.num(),other.den())
        frac1.simplify()
        frac2.simplify()
        return frac1.show()==frac2.show()
        
    def num(self):
        """returns the numerator"""
        return self.__num
    
    def den(self):
        """returns the denominator"""
        return self.__den
        
    def show(self):
        """display a fraction"""
        return f"({self.num()}/{self.den()})"
    
    def simplify(self):
        """simplify the fraction"""
        diviseur=pgcd(self.num(),self.den())
        self.__num=int(self.num()/diviseur)
        self.__den=int(self.den()/diviseur)
        
    
    def __add__(self,other):
        """add two fractions"""
        frac_den=int(ppcm(self.den(),other.den()))
        frac_num=int(self.num()*frac_den/self.den()+other.num()*frac_den/other.den())
        rep=Fraction(frac_num,frac_den)
        rep.simplify()
        return rep
    
    def __mul__(self, other):
        """multiply two fractions"""
        frac_den=int(self.den()*other.den())
        frac_num=int(self.num()*other.num())
        rep=Fraction(frac_num,frac_den)
        rep.simplify()
        return rep
    

    
    def __str__ (self):
        """defines the 'print' command for a fraction"""
        return self.show()
        
    
        
    

        
    

def H(n) :
    """calculates the term n of the harmonic series"""
    sum_H=Fraction(1,1)
    for i in range (2,n+1):
        sum_H=sum_H+Fraction(1,i)
    return sum_H
    
def Leibniz(n) :
    """calculates the term n of the Leibniz series"""
    sum_leibniz=Fraction(1,1)
    for i in range (1,n+1):
        sum_leibniz=sum_leibniz+Fraction((-1)**i,2*i+1)
    return sum_leibniz
      
    
        
    
if __name__=='__main__':
    frac1=Fraction(5,4)
    frac1_bis=Fraction(10,8)
    frac2=Fraction(9,14)
    frac3=Fraction(53,28)
    frac4=frac1+frac2
    frac5=Fraction(28,14)
    frac5.simplify()
    frac6=Fraction(2,1)
    frac7=Fraction(45,56)
    frac8=frac1*frac2
    assert frac3==frac4
    assert frac5==frac6
    assert frac7==frac8
    assert frac1==frac1_bis
    harmo=H(10000)
    assert abs(harmo.num()/harmo.den()-9.7876)<0.0001
    leib=Leibniz(10000)
    assert abs(leib.num()/leib.den()-pi/4)<0.001     
        
        
