from check_series_transitions import check_series_transitions_delta1
from quan_number import correction_info_tr, format_for_output

def write_predictions(branches, file2):
    for branch in branches:
        if len(branch) == 0:
            branches.remove(branch)
  
    #calculete all possible transitions and deltas
    for branch in branches:
        check_series_transitions_delta1(branch)
    
    max_len = max(list(map(lambda x:len(x),branches)))
    #for writing out by 1 type of transitions
    for i in range(max_len):
        for branch in branches:               
        #for i in range(len(branch)):
            try:
                correction_info_tr(branch[i])
                branch[i] = format_for_output(branch[i])
                
                file2.write('{:<41}'.format(branch[i])+'|| ')
            except IndexError:
                file2.write('{:>41}'.format('')+' || ')

            
        file2.write('\n')
    file2.write('-'*(45*len(branches))+'\n'*2)

