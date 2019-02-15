def delta_full_2(branch_1, branch_0, delta_type):
    # branch = one line in list, format line [Tr, I, J, Ka,Kc]
    if delta_type == 1:
        lenght, index = 5, 0
    elif delta_type == 2:
        lenght, index = 6, 5

    # if lenght of one of branch if less than index(list[index] to calculate delta)
    # then do nothing
    if len(branch_1) <= index or len(branch_0) <= index:
        return None

    # if list does not include delta, then add delta to list 
    if len(branch_1) == lenght:
        branch_1.append(branch_1[index]-branch_0[index])


def calculate_delta(branch, i, delta_type):
    if delta_type == 1:
        delta_index, lenght = 5, 6
    elif delta_type == 2:
        delta_index, lenght = 6, 7

    #if delta are exsists in both cases
    if len(branch[i]) == lenght and len(branch[i-1]) == lenght:
        return None
    
    # for one or for both transitions do not exist info
    if branch[i][1] != None and branch[i-1][1] != None:
        delta_full_2(branch[i], branch[i-1], delta_type=delta_type)
    else:
        return None


def fill_empties_delta (branch, i, k):
    if len(branch[i]) != 7:
        ##############
        #It's work but may be can improve it
        try:
            print (branch[i], k)
            delta1, delta2 = fill_empties_delta(branch, i+k, k)
        except IndexError:
            if k == 1:
                print ('End of file')
                try:
                    k = -1
                    delta1, delta2 = fill_empties_delta(branch, i+k, k)
                except:
                    print ('Begin of file')
                    delta1 = None
        print (branch[i])
                
        if delta1 is None:
            return None, None
        #############
        
        if len(branch[i]) == 6:
            delta1 = branch[i][5]
            branch[i].append(delta2)
            return delta1, delta2

        if len(branch[i]) == 5:
            branch[i].append(delta1-delta2)
            branch[i].append(delta2)
            return delta1-delta2, delta2
    else:
        return branch[i][5], branch[i][6]

def calculate_transitions(branch, i):
    # calculate missing tr
    if branch[i][1] is None:
        try:
            branch[i][0] = branch[i-1][0] + branch[i-1][5] + branch[i-1][6]
        except IndexError:
            return None


def check_series_transitions_delta1(name):
    '''
    Check transitions; if there are None - calculate possibale value;
    calculate deltas for all transitions;
    name - Transition()
    '''

    branches = [name.Q_b, name.Q_a,name.R_a, name.P_a,\
               name.R_b, name.P_b ]

    for branch in branches:
        if len(branch) == 0:
            continue
        J, Ka = branch[0][2],branch[0][3]

        # calculate delta1 for excisting transitions
        for i in range(1, len(branch)):
            calculate_delta(branch, i, delta_type=1)
            
        # calculate delta2 for excisting transitions
        for i in range(1, len(branch)):
            calculate_delta(branch, i, delta_type=2)

        # calculate delta1 and delta 2 for empty transitions
        for i in range(0, len(branch)):
            fill_empties_delta(branch, i, k=1)
            #input()
            

        # calcalate missing, first*3 and last*3 transitions
        for i in range(0, len(branch)):
            calculate_transitions(branch, i)

        '''
        if J > Ka:
            for i in range(J,Ka,-1):
                
                print (branch)
        '''

