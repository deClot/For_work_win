from check_series_transitions import check_series_transitions_delta
from quan_number import correction_tr_pred, format_for_output, correction_tr_search

def write_predictions(branches, file2):
    for branch in branches:
        if len(branch) == 0:
            branches.remove(branch)
    print(branches)
    #calculete all possible transitions and deltas
    for branch in branches:
        check_series_transitions_delta(branch)
    
    max_len = max(list(map(lambda x:len(x),branches)))
    #for writing out by 1 type of transitions
    for i in range(max_len):
        for branch in branches:               
        #for i in range(len(branch)):
            try:
                correction_tr_pred(branch[i])
                branch[i] = format_for_output(branch[i])
                
                file2.write('{:<41}'.format(branch[i])+'|| ')
            except IndexError:
                file2.write('{:>41}'.format('')+' || ')

            
        file2.write('\n')
    file2.write('-'*(45*len(branches))+'\n'*2)

def add_to_list_line(branch, list_branch):
    try:
        list_branch.append(correction_tr_search(branch[-1]))
    except IndexError:   # errors will be if branch is empty
        list_branch.append('')
        
    return list_branch

def write_search(name,  file_search):
    #branches_a = [name.R_a, name.Q_a, name.P_a]
    #branches_b = [name.R_b, name.Q_b, name.P_b]
    #branches_c = [name.R_c, name.Q_c, name.P_c]

    types = [name.a, name.b, name.c]
    #types = [name.c]
    
    for t in types:
        branches = [t.R, t.Q, t.P]

        templates = []

        lines_allowed = []
        lines_forbidden = []
        for branch in branches:
            print('Strat branhch')
            list_branch_allowed = []
            list_branch_forbidden= []
            for k in branch.keys():
                d_ka, d_kc = k
                print(k, d_ka, d_kc)
                if abs(d_ka) <= 1 and abs(d_kc) <= 1:
                    print('Allowed')
                    list_branch_allowed = add_to_list_line(branch[k], list_branch_allowed)
                else:
                    print('Forbidden')
                    list_branch_forbidden = add_to_list_line(branch[k], list_branch_forbidden)
            lines_allowed.append(list_branch_allowed)
            lines_forbidden.append(list_branch_forbidden)
                    
        #print( lines_allowed)
        #print(lines_forbidden)
        
        #check that transitions for type are exist
        count = 0
        for el in lines_allowed:
            if el == '':   # empty line
                count += 1
        if count == 3:
            continue

        '''
        #check number of P-lines
        if len(lines_allowed)
        if templates[-1] == '' and templates[1] == '':
            file_search.write('   {:>37}\n\n'.format(*templates))
            continue
        if templates[0] == '' and templates[1] == '':
            file_search.write('{:>81}\n\n'.format(templates[-1]))
            continue
        if templates[-1] == '':
            file_search.write('   {:>37}{:>41}\n\n'.format(*templates))
            continue
        if templates[1] == '':
            file_searchs.write('   {:>37}\n{:>81}\n\n'.format(templates[0], \
                                                             templates[-1]))
            continue
            
        file_search.write('   {:>37}{:>40}\n{:>81}\n\n'.format(*templates))

        '''    
            
            
