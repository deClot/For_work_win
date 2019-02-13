def check_series_transitions(name):
    '''
    Check transitions; if there are None - calculate possibale value;
    calculate deltas for all transitions; join to string
    '''

    branches = name.R_a, name.Q_a, name.P_a,\
               name.R_b, name.Q_b, name.P_b

    for branch in branches:
        if len(branch) == 0:
            continue

        if branch[0][2] > branch[0][3]:


