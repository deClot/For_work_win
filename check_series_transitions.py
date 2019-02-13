def delta_full_2(branch_1, branch_0):
    # branch = one line in list, format line [Tr, I, J, Ka,Kc]
            if len(branch_1) == 5:
                branch_1.append(branch_1[0]-branch_0[0])
            else:
                return None


def delta_empty_full(empty, full, delta):
    if empty[2] < full[2]:  # if empty-full sequence
        empty[0] = full[0] - delta # Calculate tr for empty
        empty.append(delta)
        # Write info for other
        if len(full) == 5:
            full.append(delta)
    elif empty[2] > full[2]: # if full-empty sequence
        empty[0] = full[0] + delta # Calculate tr for empty
        empty.append(delta)
        # Write info for other
        if len(full) == 5:
            full.append(delta)
    else:
        raise ValueError('2 transitions have the same valus of J')

    
def calculate_delta(branch, i):
    # branch = like name.R_a
        # there are two transitions
    #print(branch[i-1],branch[i])
    if branch[i][0] != None and branch[i-1][0] != None:
        #print('1')
        delta_full_2(branch[i], branch[i-1])
        #print('1')

    # for one or for both transitions do not exist info
    #elif delta != 0:
    elif len(branch[i]) == 6 or len(branch[i-1]) == 6:
        #print('2')
        if branch[i-1][0] != None:
            #print ('2-1')
            #print (branch[i-1], branch[i])
            delta_empty_full(branch[i], branch[i-1], branch[i-1][5])
        elif branch[i][0] != None:
            #print ('2-2')
            delta_empty_full(branch[i-1], branch[i], branch[i][5])
    else:
        #print ('3')
        calculate_delta(branch, i+1)
        if len(branch[i+1]) == 6:
        #    print('4')
            delta = branch[i+1][5]
            #print(branch[i+1])
            #print(branch[i-1], branch[i])
            delta_empty_full(branch[i-1], branch[i], delta)
            
    

def check_series_transitions(name):
    '''
    Check transitions; if there are None - calculate possibale value;
    calculate deltas for all transitions; join to string

    '''

    branches = [name.R_a, name.Q_a, name.P_a,\
               name.R_b, name.Q_b, name.P_b]

    for branch in branches:
        if len(branch) == 0:
            continue
        J, Ka = branch[0][2],branch[0][3]

        print ('branch_to_calculate')
        print (branch)

        delta = 0
        for i in range(1, len(branch)):
            calculate_delta(branch, i)
            #input()
            

            
        print('branch')
        print (branch)

        '''if J > Ka:
            for i in range(J,Ka,-1):
                print (branch)
'''
