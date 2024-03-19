# -*- coding: utf-8 -*-

dico=open("frenchssaccent.dic",'r')

lexique=[]
for ligne in dico:
    lexique.append(ligne[0:len(ligne)-1])
    

def exercice_1(tirage):
    mot_possible=[]
    réponse=[]
    len_max=0
    for mot in lexique:
        if len(mot)<=len(tirage):
            utilisation_lettre=[1]*len(tirage)
        for lettre in mot:
            Test=False
            for m in range(len(tirage)):
                if not Test and lettre == tirage[m]*utilisation_lettre[m] :
                    Test = True
                    utilisation_lettre[m]=0
            if not Test :
                break
        if Test :
            mot_possible.append(mot)
            
            if len(mot)==len_max:
                réponse.append(mot)
            if len(mot)>len_max:
                len_max=len(mot)
                réponse=[mot]
    print('mot possible:',mot_possible,'\nréponse:',réponse)
    return None


#ex_2
# tirage = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']
# exercice_1(tirage)
            

#pour l'exercice 3, la structure de donnée à utiliser est le dictionnaire



point={}
point['a']=point['e']=point['i']=point['l']=point['n']=point['o']=point['r']=point['s']=point['t']=point['u']=1
point['d']=point['g']=point['m']=2
point['b']=point['c']=point['p']=3
point['f']=point['h']=point['v']=4
point['j']=point['q']=8
point['k']=point['w']=point['x']=point['y']=point['z']=10

def score(mot):
    somme=0
    for lettre in mot:
        somme +=point[lettre]
    return somme

def max_score(liste):
    scor_max=0
    mot_max=''
    for mot in liste:
        if score(mot)>scor_max:
            scor_max=score(mot)
            mot_max=mot
    return mot_max,scor_max



def exercice_3(tirage):
    mot_possible=[]
    réponse=[]
    score_max=0
    for mot in lexique:
        if len(mot)<=len(tirage):
            utilisation_lettre=[1]*len(tirage)
        for lettre in mot:
            Test=False
            for m in range(len(tirage)):
                if not Test and lettre == tirage[m]*utilisation_lettre[m] :
                    Test = True
                    utilisation_lettre[m]=0
            if not Test :
                break
        if Test :
            mot_possible.append(mot)
            
            if score(mot)==score_max:
                réponse.append(mot)
            if score(mot)>score_max:
                score_max=score(mot)
                réponse=[mot]
    print('mot possible:',mot_possible,'\nréponse:',réponse,'\npoints:',score_max)
    return None

#test ex_3    
# tirage = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']
# exercice_3(tirage)

                    
def exercice_4(tirage):
    mot_possible=[]
    réponse=[]
    score_max=0
    for mot in lexique:
        if len(mot)<=len(tirage):
            utilisation_lettre=[1]*len(tirage)
        for lettre in mot:
            Test=False
            for m in range(len(tirage)):
                if not Test and lettre == tirage[m]*utilisation_lettre[m] :
                    Test = True
                    utilisation_lettre[m]=0
                    
            if not Test :
                
                for i in range(len(tirage)):
                    
                    if tirage[i]=='?'*utilisation_lettre[i]:
                        utilisation_lettre[i]=0
                        Test=True
                        
                if not Test:
                    break
                
        if Test :
            mot_possible.append(mot)
            
            if score(mot)==score_max:
                réponse.append(mot)
            if score(mot)>score_max:
                score_max=score(mot)
                réponse=[mot]
    print('mot possible:',mot_possible,'\nréponse:',réponse,'\npoints:',score_max)
    return None

#test ex_4    
# tirage = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j','?']
# exercice_4(tirage)