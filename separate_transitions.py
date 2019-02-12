import re

import check_branch

def Separate_transitions (J0,Ka0,Kc0,str1,transitions,Tr):
    sample = '3  0  3  3663.43740 13.9  3710.59730    5  0  5  3597.93318 16.5  3710.59711 -r'
    
    template_comment1 = r'\A[a-zA-Z-!+]+' #comment in the beginin of line
    template_comment2 = r'[a-zA-Z-!]+$'  #comment in the end of line

    comment1 = re.findall(template_comment1, sample)
    if len(comment1) > 1:
        print ('Two or more comments in begining of line')
        return 0
        
    comment2 = re.findall(template_comment2, sample)

    template_transition = r'\d+\s+\d+\s+\d+\s+\d+\.\d+\s+\d+\.\d+\s+\d+.\d+'
    blocks = re.findall(template_transition, sample))
    for block in blocks:
        transitions.append(blok)
        J,Ka,Kc,Trans,I,E = block.split()
        check_branch.Check_Branch (J0,J,Ka0,Ka,Kc0,Kc,Trans,I,E,Tr)      
    
    '''
    if len(str1)==6:
        J,Ka,Kc,Trans,I,E=str1
        check_branch.Check_Branch (J0,J,Ka0,Ka,Kc0,Kc,Trans,I,E,Tr)

    elif len(str1)>6 and len(str1)<12:
        J,Ka,Kc,Trans,I,E, *_=str1
        check_branch.Check_Branch (J0,J,Ka0,Ka,Kc0,Kc,Trans,I,E,Tr)
    elif len(str1) == 12:
        J,Ka,Kc,Trans,I,E,*_=str1
        check_branch.Check_Branch (J0,J,Ka0,Ka,Kc0,Kc,Trans,I,E,Tr)

        *_, J,Ka,Kc,Trans,I,E =str1
        check_branch.Check_Branch (J0,J,Ka0,Ka,Kc0,Kc,Trans,I,E,Tr)
    '''

#
#    print (Tr.R_Tr, Tr.R_I,Tr.Q_Tr, Tr.Q_I,Tr.P_Tr, Tr.P_I)
Separate_transitions(5,5,5,'ooooooo',5)
