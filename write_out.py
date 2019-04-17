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

def write_search(name,  file_search):
    branches_a = [name.R_a, name.Q_a, name.P_a]
    branches_b = [name.R_b, name.Q_b, name.P_b]
    branches_c = [name.R_c, name.Q_c, name.P_c]

    for types in (branches_a, branches_b, branches_c):
        template = []
        for branch in types:
            try:    
                template.append(correction_tr_search(branch[-1]))
            except IndexError:
                template.append('')

        #check that transitions for type exist
        count = 0
        for el in template:
            if el == '':
                count += 1
        if count == 3:
            continue

        #check P branch
        if template[-1] == '' and template[1] == '':
            file_search.write('   {:>37}\n\n'.format(*template))
            continue
        if template[0] == '' and template[1] == '':
            file_search.write('{:>81}\n\n'.format(template[-1]))
            continue
        if template[-1] == '':
            file_search.write('   {:>37}{:>41}\n\n'.format(*template))
            continue
        if template[1] == '':
            file_search.write('   {:>37}\n{:>81}\n\n'.format(template[0], \
                                                             template[-1]))
            continue
            
        file_search.write('   {:>37}{:>40}\n{:>81}\n\n'.format(*template))

            
            
            
