import quan_number

def check_list_to_append(branch,Trans,I,J,Ka,Kc,E):
    '''
    Check lenght of list on losted transitions. If it exists - add empty line for corresponding quantum numbers
    '''
    if len(branch)>=1:    # if in series 1 transitions already exists
        if branch[-1][2] == J and branch[-1][0] == Trans:   # for double equal lines
            return None

        if branch[-1][2] == J: # if lines are equeal but have differen transitions
            #Calculate mean and replace last line on new one
            Trans = (Trans + branch[-1][0])/2
            E = (E + branch[-1][-1])/2
            branch.pop(-1)
            branch.append([Trans,I,J,Ka,Kc,E,'comb'])
            return None
            
        # If current transitions is not uniform continuation of last transitions. Compare J and Ka
        while (branch[-1][2]+1 < J and branch[-1][4]+1 < Kc):  
            # Create new line for lapse
            branch.append([None,None,\
                           branch[-1][2]+1,branch[-1][3],\
                           branch[-1][4]+1, None])
        branch.append([Trans,I,J,Ka,Kc,E])
    else:
        branch.append([Trans,I,J,Ka,Kc,E])
           
def check_branch(J0,J,Ka0,Ka,Kc0,Kc,Trans,I,E,Tr,Up):
    '''    Check branch on series name; add transition on corresponding quantum numbers;\
if there are the emptities in list, add empty transitions for it
    '''
    
    J,Ka,Kc,Trans,I,E=quan_number.Quantum_numbers(J,Ka,Kc,Trans,I,E) #transform to int and float
    delta_Ka, delta_Kc = Ka - Ka0, Kc - Kc0

    if J<J0:                                         # R branch
        if   abs(Ka-Ka0)%2 == 0 and abs(Kc-Kc0)%2 == 1:  # a type
            check_list_to_append(Tr.a.R[(delta_Ka,delta_Kc)],Trans,I,J,Ka,Kc,E)
            check_list_to_append(Up.a.R[(delta_Ka,delta_Kc)],Trans,I,J,Ka,Kc,E)
        elif abs(Ka-Ka0)%2 == 1 and abs(Kc-Kc0)%2 == 1:  # b type
            check_list_to_append(Tr.b.R[(delta_Ka,delta_Kc)],Trans,I,J,Ka,Kc,E)
            check_list_to_append(Up.b.R[(delta_Ka,delta_Kc)],Trans,I,J,Ka,Kc,E)
        elif abs(Ka-Ka0)%2 == 1 and abs(Kc-Kc0)%2 == 0:  # c type
             check_list_to_append(Tr.c.R[(delta_Ka,delta_Kc)],Trans,I,J,Ka,Kc,E)
             check_list_to_append(Up.c.R[(delta_Ka,delta_Kc)],Trans,I,J,Ka,Kc,E)
    
    elif J==J0:                                      # Q branch
        if   abs(Ka-Ka0)%2 == 0 and abs(Kc-Kc0)%2 == 1:  # a type
            if (delta_Ka,delta_Kc) not in Tr.a.Q.keys():
                check_list_to_append(Tr.a.Q[(-delta_Ka,-delta_Kc)],Trans,I,J,Ka,Kc,E)
                check_list_to_append(Up.a.Q[(-delta_Ka,-delta_Kc)],Trans,I,J,Ka,Kc,E)
            else:
                check_list_to_append(Tr.a.Q[(delta_Ka,delta_Kc)],Trans,I,J,Ka,Kc,E)
                check_list_to_append(Up.a.Q[(delta_Ka,delta_Kc)],Trans,I,J,Ka,Kc,E)
        elif abs(Ka-Ka0)%2 == 1 and abs(Kc-Kc0)%2 == 1:  # b type
            check_list_to_append(Tr.b.Q[(delta_Ka,delta_Kc)],Trans,I,J,Ka,Kc,E)
            check_list_to_append(Up.b.Q[(delta_Ka,delta_Kc)],Trans,I,J,Ka,Kc,E)
        elif abs(Ka-Ka0)%2 == 1 and abs(Kc-Kc0)%2 == 0:  # c type
            if (delta_Ka,delta_Kc) not in Tr.c.Q.keys():
                check_list_to_append(Tr.c.Q[(-delta_Ka,-delta_Kc)],Trans,I,J,Ka,Kc,E)
                check_list_to_append(Up.c.Q[(-delta_Ka,-delta_Kc)],Trans,I,J,Ka,Kc,E)
            else:
                check_list_to_append(Tr.c.Q[(delta_Ka,delta_Kc)],Trans,I,J,Ka,Kc,E)
                check_list_to_append(Up.c.Q[(delta_Ka,delta_Kc)],Trans,I,J,Ka,Kc,E)
            
    elif J>J0:                                       # P branch
        if   abs(Ka-Ka0)%2 == 0 and abs(Kc-Kc0)%2 == 1:  # a type
            check_list_to_append(Tr.a.P[(delta_Ka,delta_Kc)],Trans,I,J,Ka,Kc,E)
            check_list_to_append(Up.a.P[(delta_Ka,delta_Kc)],Trans,I,J,Ka,Kc,E)
        elif abs(Ka-Ka0)%2 == 1 and abs(Kc-Kc0)%2 == 1:  # b type
            check_list_to_append(Tr.b.P[(delta_Ka,delta_Kc)],Trans,I,J,Ka,Kc,E)
            check_list_to_append(Up.b.P[(delta_Ka,delta_Kc)],Trans,I,J,Ka,Kc,E)
        elif abs(Ka-Ka0)%2 == 1 and abs(Kc-Kc0)%2 == 0:  # c type
            check_list_to_append(Tr.c.P[(delta_Ka,delta_Kc)],Trans,I,J,Ka,Kc,E)
            check_list_to_append(Up.c.P[(delta_Ka,delta_Kc)],Trans,I,J,Ka,Kc,E)
