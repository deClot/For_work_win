import re

import check_branch

def Separate_transitions(J0,Ka0,Kc0,str1,transitions,Tr,Up):
    #str1 = '3  0  3  3663.43740 13.9  3710.59730    5  0  5  3597.93318 16.5  3710.59711 -r'
    
    template_comment1 = r'\A[a-zA-Z-!+]+' #comment in the beginin of line
    template_comment2 = r'[a-zA-Z-!]+$'  #comment in the end of line

    comment1 = re.findall(template_comment1, str1)
    if len(comment1) > 1:
        print ('Two or more comments in the begining of line')
        return 0
        
    comment2 = re.findall(template_comment2, str1)
    
    #                       J     Ka     Kc   Tr . Tr      I I       E . E
    template_transition = r'\d+\s+\d+\s+\d+\s+\d+\.\d+\s+\d+\.\d+\s+\d+.\d+'
    blocks = re.findall(template_transition, str1)
    for block in blocks:
        transitions.append(block)
        J,Ka,Kc,Trans,I,E = block.split()
        check_branch.check_branch (J0,J,Ka0,Ka,Kc0,Kc,Trans,I,E,Tr,Up)
    return 1
