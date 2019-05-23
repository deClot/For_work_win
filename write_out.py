from check_series_transitions import check_series_transitions_delta
from quan_number import correction_tr_pred, format_for_output, correction_tr_search

def void_type_checking(branches):
    for branch in branches:
        if sum([len(el) for el in branch.values()]) == 0:
            continue
        else:
            return 0
    return 1

def prepare_branch_list(branches):
    res = []
    for branch in branches:
        for k,v in branch.items():
            if abs(k[0]) <= 1 and abs(k[1]) <= 1:
                if len(v) == 0:
                    continue
                res.append(v)
    return res
    
    

def write_predictions(branches, file2):
    if void_type_checking(branches) == 1:
        return None
    
    branches = prepare_branch_list(branches)

    #calculete all possible transitions and delta
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

 
def write_line_from_three_tr(lines, file_search):
    max_len = len(max(lines, key=len))
    for i in range(max_len):
        temp_list = [el[i] for el in lines]
        #if R an d Q lines do not exist
        if temp_list[0] == '' and temp_list[1] == '':
            continue
        file_search.write('   {:>37}{:>40}\n'.format(*temp_list))
    for i in range(max_len):
        file_search.write('{:>40}{:>41}\n'.format('', lines[-1][i]))
    return 1
            

def separate_lines(t):
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

    return lines_allowed, lines_forbidden  



def write_search(name,  file_search):
    types = [name.a, name.b, name.c]
    
    for t in types:
        lines_allowed, lines_forbidden = separate_lines(t)
        # cleaning  and write allowed transitions
        lines_allowed = preparing_line_list(lines_allowed)
        if lines_allowed == 1:  # if  it's empty
             continue
        write_line_from_three_tr(lines_allowed, file_search)

        file_search.write('\n')

        # clean and write forbidden transitions
        lines_forbidden = preparing_line_list(lines_forbidden)
        if lines_forbidden == 1:  # if  it's empty
            continue
        lines_forbidden = additional_preparind(lines_forbidden)
        write_line_from_three_tr(lines_forbidden, file_search)
        
