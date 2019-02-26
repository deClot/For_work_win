def Quantum_numbers (J,Ka,Kc,Trans,I,E):
    J=int(J)
    Ka=int(Ka)
    Kc=int(Kc)
    Trans = float(Trans)
    I = float (I)/100-0.005
    E = float (E)

    return J,Ka,Kc,Trans,I,E

def correction_info_tr(branch):
    if branch[0] is None:
        branch[0] = ''
        branch[1] = ''
        return None
    branch[0] = round(branch[0], 5)
    if branch[1] != None:
        branch[1] = round(branch[1]*100, 1)
    else:
        branch[1] = ''
        
    for i in (6,7):
        try:
            branch[i] = round(branch[i],3)
        except IndexError:
            return None

def format_for_output(branch):
    template = '{:<10}{:>6}{:>4}{:>3}{:>3} |'.format(*branch)
    for i in (6,7):
        try:
            template_delta = '{:<6} '.format(*branch[i:])
            template += template_delta
        except IndexError:
            return template

    return template

def format_for_search(ref,counter):
    branches = (ref.R_a, ref.Q_a, ref.P_a,\
                ref.R_b, ref.Q_b, ref.P_b)
    print(counter)
    try:
        print(ref.R_a[counter])
    except IndexError:
        pass
    
