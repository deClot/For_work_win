import quan_number

def check_list_to_append(branch,Trans,I,J,Ka,Kc):
    '''
    Check lenght of list on losted transitions. If it exists - add empty line for corresponding quantum numbers
    '''
    if len(branch)>=1:
        while (branch[-1][2]+1 != J and branch[-1][4]+1 != Kc):
            branch.append([None,None,\
                           branch[-1][2]+1,branch[-1][3],\
                           branch[-1][4]+1])
        branch.append([Trans,I,J,Ka,Kc])
    else:
        branch.append([Trans,I,J,Ka,Kc])
        

def check_branch(J0,J,Ka0,Ka,Kc0,Kc,Trans,I,E,Tr):
    '''
    Chech branch on series name; add transition on corresponding quantum numbers;\
if there are the emptities in list, add empty transitions for it
    '''
    
    J,Ka,Kc,Trans,I,E=quan_number.Quantum_numbers (J,Ka,Kc,Trans,I,E) #transform to int and float
    if abs(Ka-Ka0)<2 and abs(Kc-Kc0)<2:    # allowed transitions
        if J==J0:                                        # Q branch
            if   abs(Ka-Ka0) == 0 and abs(Kc-Kc0) == 1:  # a type
                check_list_to_append(Tr.Q_a,Trans,I,J,Ka,Kc)
            elif abs(Ka-Ka0) == 1 and abs(Kc-Kc0) == 1:  # b type
                check_list_to_append(Tr.Q_b,Trans,I,J,Ka,Kc)
        elif J<J0:
            if   abs(Ka-Ka0) == 0 and abs(Kc-Kc0) == 1:  # a type
                check_list_to_append(Tr.R_a,Trans,I,J,Ka,Kc)
            elif abs(Ka-Ka0) == 1 and abs(Kc-Kc0) == 1:  # b type
                check_list_to_append(Tr.R_b,Trans,I,J,Ka,Kc)
        elif J>J0:
            if   abs(Ka-Ka0) == 0 and abs(Kc-Kc0) == 1:  # a type
                check_list_to_append(Tr.P_a,Trans,I,J,Ka,Kc)
            elif abs(Ka-Ka0) == 1 and abs(Kc-Kc0) == 1:  # b type
                check_list_to_append(Tr.P_b,Trans,I,J,Ka,Kc)
    
