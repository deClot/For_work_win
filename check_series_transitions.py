def delta_full_2(branch_1, branch_0, delta_type):
    # branch = one line in list, format line [Tr, I, J, Ka,Kc]
    if delta_type == 1:
        lenght, index = 6, 0
    elif delta_type == 2:
        lenght, index = 7, 6

    # if lenght of one of branch if less than index(list[index] to calculate delta)
    # then do nothing
    if len(branch_1) <= index or len(branch_0) <= index:
        return None

    # if list does not include delta, then add delta to list 
    if len(branch_1) == lenght:
        branch_1.append(branch_1[index]-branch_0[index])


def calculate_delta(branch, i, delta_type):
    if delta_type == 1:
        delta_index, lenght = 6, 7
    elif delta_type == 2:
        delta_index, lenght = 7, 8

    #if delta are exsists in both cases
    if len(branch[i]) == lenght and len(branch[i-1]) == lenght:
        return None
    
    # for one or for both transitions do not exist info
    if branch[i][1] != None and branch[i-1][1] != None:
        delta_full_2(branch[i], branch[i-1], delta_type=delta_type)
    else:
        return None


def fill_empties_delta (branch, i, k):
    # k - show in which propagation we go through file, +1 from beginning to end, -1 v.v.
    if len(branch[i]) != 8:
        #It's work but may be improved it
        try:
            # if there is next transitions - go to next and take it deltas
            delta1, delta2 = fill_empties_delta(branch, i+k, k)
        except IndexError:
            # if end of file
            if k == 1:
                #print ('End of file')
                try:
                    k = -1
                    delta1, delta2 = fill_empties_delta(branch, i+k, k)
                except:
                    #print ('Begin of file')
                    delta1 = None
        #print (branch[i])
                
        if delta1 is None:
            return None, None
        #############
        # if delta1 and delta2 exist
        if len(branch[i]) == 7:
            delta1 = branch[i][6]
            branch[i].append(delta2)
            return delta1, delta2

        # if only delta1 exsits
        if len(branch[i]) == 6:
            branch[i].append(delta1-delta2)
            branch[i].append(delta2)
            return delta1-delta2, delta2
    else:
        return branch[i][6], branch[i][7]

def calculate_None_transitions(branch, i):
    # calculate missing tr
    if branch[i][0] is None:
        try:
            branch[i][0] = branch[i-1][0] + branch[i-1][6] + branch[i-1][7]
        except IndexError:
            return None


def calculate_beginning_serie(branch):
    if branch[0][2] > branch[0][3] and branch[0][2] >= 0 : # J > Ka
        try:
            Tr = branch[0][0] - branch[0][6]
            I, J, Ka, Kc = None, branch[0][2]-1, branch[0][3], branch[0][4]-1
            delta1 = branch[0][6] - branch[0][7]
            delta2 = branch[0][7]
            branch.insert(0, [Tr, I, J, Ka, Kc,None,delta1, delta2])
            calculate_beginning_serie(branch)
        except IndexError:
            return None
    else:
        return None     
   
def calculate_end_serie(branch, count = 3):
    end = len(branch)-1
    
    #input()
    if count > 0:
        try:
            Tr = branch[end][0] + branch[end][6] + branch[end][7]
            I, J, Ka, Kc = None, branch[end][2]+1, branch[end][3], branch[end][4]+1
            delta1 = branch[end][6] + branch[end][7]
            delta2 = branch[end][7]
            branch.append([Tr, I, J, Ka, Kc, None,delta1, delta2])
            count -= 1
            calculate_end_serie(branch, count)
        except IndexError:
            return None
    else:
        return None     
    
def check_series_transitions_delta(branch):
    '''
    Check transitions; if there are None - calculate possibale value;
    calculate deltas for all transitions;
    '''

    print(branch)
    if len(branch) == 0:
        return None
    J, Ka = branch[0][2],branch[0][3]

    for i in range(len(branch)):
        if len(branch[i]) == 7: # include 'combination'
            branch[i][1] = 'c' + str(branch[i][1])
            branch[i].pop(-1)
    # calculate delta1 for excisting transitions
    for i in range(1, len(branch)):
        calculate_delta(branch, i, delta_type=1)
    # calculate delta2 for excisting transitions
    for i in range(1, len(branch)):
        calculate_delta(branch, i, delta_type=2)
    
    # calculate delta1 and delta2 for empty transitions
    for i in range(0, len(branch)):
        fill_empties_delta(branch, i, k=1)
        
    # calculate missing (None) transitions
    for i in range(0, len(branch)):
        calculate_None_transitions(branch, i)

        
    # calculate first transitions up to 0
    calculate_beginning_serie(branch)
    
    # calculate three next transitions
    calculate_end_serie(branch)

