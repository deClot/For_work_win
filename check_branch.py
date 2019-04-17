import quan_number
#from module import ref_e

def check_list_to_append(branch,Trans,I,J,Ka,Kc,E):
    '''
    Check lenght of list on losted transitions. If it exists - add empty line for corresponding quantum numbers
    '''
    if len(branch)>=1:
        while (branch[-1][2]+1 != J and branch[-1][4]+1 != Kc):
            branch.append([None,None,\
                           branch[-1][2]+1,branch[-1][3],\
                           branch[-1][4]+1, None])
        branch.append([Trans,I,J,Ka,Kc,E])
    else:
        branch.append([Trans,I,J,Ka,Kc,E])
        

def check_branch(J0,J,Ka0,Ka,Kc0,Kc,Trans,I,E,Tr,Up):
    '''
    Chech branch on series name; add transition on corresponding quantum numbers;\
if there are the emptities in list, add empty transitions for it
    '''
    
    J,Ka,Kc,Trans,I,E=quan_number.Quantum_numbers (J,Ka,Kc,Trans,I,E) #transform to int and float
    if abs(Ka-Ka0)<2 and abs(Kc-Kc0)<2:    # allowed transitions
        if J==J0:                                        # Q branch
            if   abs(Ka-Ka0) == 0 and abs(Kc-Kc0) == 1:  # a type
                check_list_to_append(Tr.Q_a,Trans,I,J,Ka,Kc,E)
                check_list_to_append(Up.Q_a,Trans,I,J,Ka,Kc,E)
            elif abs(Ka-Ka0) == 1 and abs(Kc-Kc0) == 1:  # b type
                check_list_to_append(Tr.Q_b,Trans,I,J,Ka,Kc,E)
                check_list_to_append(Up.Q_b,Trans,I,J,Ka,Kc,E)
            elif abs(Ka-Ka0) == 1 and abs(Kc-Kc0) == 0:  # c type
                check_list_to_append(Tr.Q_c,Trans,I,J,Ka,Kc,E)
                check_list_to_append(Up.Q_c,Trans,I,J,Ka,Kc,E)
        elif J<J0:
            if   abs(Ka-Ka0) == 0 and abs(Kc-Kc0) == 1:  # a type
                check_list_to_append(Tr.R_a,Trans,I,J,Ka,Kc,E)
                check_list_to_append(Up.R_a,Trans,I,J,Ka,Kc,E)
            elif abs(Ka-Ka0) == 1 and abs(Kc-Kc0) == 1:  # b type
                check_list_to_append(Tr.R_b,Trans,I,J,Ka,Kc,E)
                check_list_to_append(Up.R_b,Trans,I,J,Ka,Kc,E)
            elif abs(Ka-Ka0) == 1 and abs(Kc-Kc0) == 0:  # c type
                check_list_to_append(Tr.R_c,Trans,I,J,Ka,Kc,E)
                check_list_to_append(Up.R_c,Trans,I,J,Ka,Kc,E)
        elif J>J0:
            if   abs(Ka-Ka0) == 0 and abs(Kc-Kc0) == 1:  # a type
                check_list_to_append(Tr.P_a,Trans,I,J,Ka,Kc,E)
                check_list_to_append(Up.P_a,Trans,I,J,Ka,Kc,E)
            elif abs(Ka-Ka0) == 1 and abs(Kc-Kc0) == 1:  # b type
                check_list_to_append(Tr.P_b,Trans,I,J,Ka,Kc,E)
                check_list_to_append(Up.P_b,Trans,I,J,Ka,Kc,E)
            elif abs(Ka-Ka0) == 1 and abs(Kc-Kc0) == 0:  # c type
                check_list_to_append(Tr.P_c,Trans,I,J,Ka,Kc,E)
                check_list_to_append(Up.P_c,Trans,I,J,Ka,Kc,E)
    
