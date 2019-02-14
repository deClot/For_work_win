def delta_full_2(branch_1, branch_0, delta_type):
    # branch = one line in list, format line [Tr, I, J, Ka,Kc]
    if delta_type == 1:
        lenght, index = 5, 0
    elif delta_type == 2:
        lenght, index = 6, 5

    if len(branch_1) <= index or len(branch_0) <= index:
        return None
    
    if len(branch_1) == lenght:
        branch_1.append(branch_1[index]-branch_0[index])  
    else:
        return None


def delta_empty_full(empty, full, delta, delta_type):
    if delta_type == 1:
        lenght = 5
    elif delta_type == 2:
        lenght = 6
        
    if empty[2] < full[2]:  # if empty-full sequence
        empty[0] = full[0] - delta # Calculate tr for empty
        empty.append(delta)
        # Write info for other
        if len(full) == lenght:
            full.append(delta)
    elif empty[2] > full[2]: # if full-empty sequence
        empty[0] = full[0] + delta # Calculate tr for empty
        empty.append(delta)
        # Write info for other
        if len(full) == lenght:
            full.append(delta)
    else:
        raise ValueError('2 transitions have the same valus of J')

    
def calculate_delta(branch, i, delta_type):
    if delta_type == 1:
        delta_index, lenght = 5, 6
    elif delta_type == 2:
        delta_index, lenght = 6, 7

    # for one or for both transitions do not exist info
    if branch[i][1] != None and branch[i-1][1] != None:
        delta_full_2(branch[i], branch[i-1], delta_type=delta_type)

    #
    elif len(branch[i]) == lenght or len(branch[i-1]) == lenght:
        if len(branch[i-1]) == lenght:
            delta_empty_full(branch[i], branch[i-1], branch[i-1][delta_index],delta_type)
        elif len(branch[i]) == lenght:
            delta_empty_full(branch[i-1], branch[i], branch[i][delta_index],delta_type)
    else:
        #if i+1 >= len(branch):
        calculate_delta(branch, i+1, delta_type)
        if len(branch[i+1]) == lenght:
            delta = branch[i+1][delta_index]
            delta_empty_full(branch[i-1], branch[i], delta, delta_type)
   
   
def check_series_transitions_delta1(name):
    '''
    Check transitions; if there are None - calculate possibale value;
    calculate deltas for all transitions;
    name - Transition()
    '''

    branches = [name.R_a, name.Q_a, name.P_a,\
               name.R_b, name.Q_b, name.P_b]

    for branch in branches:
        if len(branch) == 0:
            continue
        J, Ka = branch[0][2],branch[0][3]

        for i in range(1, len(branch)):
            calculate_delta(branch, i, delta_type=1)

        for i in range(1, len(branch)):
            calculate_delta(branch, i, delta_type=2)

        '''if J > Ka:
            for i in range(J,Ka,-1):
                print (branch)
'''

