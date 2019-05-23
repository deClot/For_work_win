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
            list_branch_allowed = []
            list_branch_forbidden= []
            for k in branch.keys():
                d_ka, d_kc = k
                if abs(d_ka) <= 1 and abs(d_kc) <= 1:
                    list_branch_allowed = add_to_list_line(branch[k], list_branch_allowed)
                else:
                    list_branch_forbidden = add_to_list_line(branch[k], list_branch_forbidden)
            lines_allowed.append(list_branch_allowed)
            lines_forbidden.append(list_branch_forbidden)
                    
        #print('a', lines_allowed)
        #print('f', lines_forbidden)

        lines_allowed = preparing_line_list(lines_allowed)
        if lines_allowed == 1:  # if  it's empty
             continue
        write_line_from_three_tr(lines_allowed, file_search)

        file_search.write('\n')
        lines_forbidden = preparing_line_list(lines_forbidden)
        if lines_forbidden == 1:  # if  it's empty
            continue
        print('f', lines_forbidden)
        lines_forbidden = additional_preparind(lines_forbidden)
        print('fa', lines_forbidden)
        a=input()
        write_line_from_three_tr(lines_forbidden, file_search, band='a')
        
def additional_preparind(lines):
    max_len = len(lines[0])
    for i in range(len(lines)):
        if len(lines[i]) == 1:
            continue
        for line in lines[i]:
            if line == '':
                lines[i].pop(lines[i].index(''))
            else:
                break
        if len(lines[i]) != max_len:
            lines[i] += ['']
                
    return lines
            

def write_line_from_three_tr(lines, file_search, band='a'):
    max_len = len(max(lines, key=len))
    if band == 'a':
        for i in range(max_len):
            temp_list = [el[i] for el in lines]
            #if R an d Q lines do not exist
            if temp_list[0] == '' and temp_list[1] == '':
                continue
            file_search.write('   {:>37}{:>40}\n'.format(*temp_list))
        for i in range(max_len):
            file_search.write('{:>81}\n'.format(lines[-1][i]))
        return 1
    elif band == 'f':
        copy_lines = lines.copy()
        print('c', copy_lines)
        temp_list = []
            
        for i in range(len(copy_lines)):
            flag = False
            for line in copy_lines[i]:
                if line != '':
                    temp_list.append(line)
                    copy_lines[i].pop(copy_lines[i].index(line))
                    flag = True
                    continue
            if flag is False:
                temp_list.append('')
            print(copy_lines)
            print(temp_list)
            a=input()
            
        
    
'''
        # if only R line exists
        if temp_list[-1] == '':# and temp_list[1] == '':
            file_search.write('   {:>37}\n\n'.format(*temp_list))
            return 1
        # if R an Q lines exist
        if temp_list[-1] == '':
            file_search.write('   {:>37}{:>41}\n\n'.format(*temp_list))
            return 1



        
        # if only P line exists
        if temp_list[0] == '' and temp_list[1] == '':
            file_search.write('{:>81}\n\n'.format(temp_list[-1]))
            return 1
        
        # if R and P lines exist
        if temp_list[1] == '':
            file_search.write('   {:>37}\n{:>81}\n\n'.format(temp_list[0], \
                                                             temp_list[-1]))
            return 1
        # if (R,Q and P)  or (Q and P) lines exist       
        file_search.write('   {:>37}{:>40}\n{:>81}\n\n'.format(*temp_list))
'''


def preparing_line_list(lines):
    max_len = len(max(lines, key=len))
    # add empty lines for Q branch b-type
    for branch in lines:
        if len(branch) < max_len:
            #  0 - R, 1 - Q, 2 - P
            # check that fist two lines do not exist
            if lines[0][0] == '' and lines[-1][0] == '' and lines[-1][1] == '':
               lines[1] = ['',''] + lines[1]  # adding empty for corresponding lines of Q branch
    for i in range(max_len-1,-1, -1):
        temp_list = [el[i] for el in lines]
        if check_for_line_existence(temp_list, 3) == 1:
            for j in range(len(lines)):
                lines[j].pop(i)
    #if all lines was empty and deleted
    for branch in lines:
        if len(branch) == 0:
            return 1
    return lines
    

def check_for_line_existence(lines_list, total_tr):
    count = 0
    for el in lines_list:
        if el == '':   # empty line
            count += 1
    if count == total_tr:
        #print('there are not transitions')
        return 1
