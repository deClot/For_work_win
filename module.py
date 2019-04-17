import separate_transitions
from replace_module import replace

from write_out import write_predictions, write_search


class Transition:
    def __init__(self, J=0, Ka=0, Kc=0):
        self.J = J
        self.Ka= Ka
        self.Kc = Kc
        self.R_a = []
        self.Q_a = []
        self.P_a = []
        self.R_b = []
        self.Q_b = []
        self.P_b = []
        self.R_c = []
        self.Q_c = []
        self.P_c = []
###########################################################

def main_function(src):
    #type_tr = input('a-type = 1, b-type = 2, c-type = 3')
    file_ini = open(src, 'r')
    file_search = open ('search', 'w')
      
    count = 0 # counter for series (for connected series like 440 and 441 together in one file)

    # Find first energy and create new object for correspinding series
    for str1 in file_ini:
       if str1.find('Sea')!=-1:
           file_search.write('   '+str1)
           
           str1=str1.split()
           _,J0,Ka0,Kc0,*_=str1 
           J0, Ka0, Kc0 =int(J0), int(Ka0), int(Kc0)

           Up_State1 = Transition(J0, Ka0, Kc0)
           Up = Transition(J0, Ka0, Kc0)
           count += 1  #+1 for first series
           ref = Up_State1
           break


    counter = 0
    
    # Go through all file_ini and find all energies for max two series 
    for str1 in file_ini:
       if str1.find('Sea',0,len(str1))!=-1:
           _,J0,Ka0,Kc0,*_ = str1.split()
           J0, Ka0, Kc0 =int(J0), int(Ka0), int(Kc0)

           #We registred next energy,so write info about previous energy in file
           write_search(Up,file_search)
           file_search.write('   '+str1)

           Up = Transition(J0, Ka0, Kc0)
           # stay in same series
           if abs(ref.J-J0) == abs(ref.Kc-Kc0) and ref.Ka == Ka0:
               continue
           #change series
           else:
               if count == 1: #if there is only one series than create new object for new series
                   Up_State2 = Transition(J0, Ka0, Kc0)
                   count += 1 # for series
                   ref = Up_State2
                   continue
               else: # if already exist 2 series -> change series
                   if ref == Up_State1:
                       ref = Up_State2
                   elif ref == Up_State2:
                       ref = Up_State1
       else:
           separate_transitions.Separate_transitions(J0,Ka0,Kc0,str1,\
                                                    ref,Up)
    write_search(Up,file_search)
    file_ini.close()
    file2 = open('RESULTS', 'w')

    if count > 1:
       name_list = [Up_State1, Up_State2]
    else: name_list = [Up_State1]

    for name in name_list:
        file2.write('\tR branch'+'\t'*19+'P branch'+'\t'*19+'Q branch\n')
        
        branches_a = [name.R_a, name.P_a, name.Q_a]
        branches_b = [name.R_b, name.P_b, name.Q_b]
        branches_c = [name.R_c, name.P_c, name.Q_c]
        
        for branches in (branches_a, branches_b, branches_c):
            write_predictions(branches, file2)
            
    file2.close()
    file_search.close()

#main_function('In/v12.RESULT')
