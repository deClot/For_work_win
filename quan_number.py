def Quantum_numbers (J,Ka,Kc,Trans,I,E):
    J=int(J)
    Ka=int(Ka)
    Kc=int(Kc)
    Trans = float(Trans)
    I = float (I)
    E = float (E)

    return J,Ka,Kc,Trans,I,E

def correction_tr_pred(branch):
    if branch[0] is None:
        branch[0] = ''
    #    branch[1] = ''
    else:
        branch[0] = round(branch[0], 5)

    if branch[1] != None:
        branch[1] = round(branch[1], 1)
    else:
        branch[1] = ''
        
    for i in (6,7):
        try:
            branch[i] = round(branch[i],3)
        except IndexError:
            return None


def correction_tr_search(branch):
    #print(branch)
    branch[0] = round(branch[0], 5)  # transiriona value
    branch[1] = round(branch[1], 1)  # transmition/absorption
    branch[5] = round(branch[5], 5)  # energy of upper state

    new = [branch[2],branch[3],branch[4],branch[0],branch[1],branch[5]]
             #J        Ka       Kc         Tr       I          E
    template = '{:>3}{:>3}{:>3}{:>12}{:>5}{:>12}'.format(*new)

    if len(branch) == 7:  # for line with comments
        template += '   ' + branch[-1]
    return template
    

def format_for_output(branch):
    template = '{:<10}{:>6}{:>4}{:>3}{:>3} |'.format(*branch)
    for i in (6,7):
        try:
            template_delta = '{:<6} '.format(*branch[i:])
            template += template_delta
        except IndexError:
            return template

    return template
    
