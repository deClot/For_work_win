file = open('v12.RESULT', 'r')

class Transition:
    def __init__(self, J, Ka, Kc):
        self.J = J
        self.Ka= Ka
        self.Kc = Kc
        self.R_a = []
        self.Q_a = []
        self.P_a = []
        self.R_b = []
        self.Q_b = []
        self.P_b = []
        '''
        self.R_Tr_f1 = []
        self.Q_Tr_f1 = []
        self.P_Tr_f1 = []
        self.R_Tr_f2 = []
        self.Q_Tr_f2 = []
        self.P_Tr_f2 = []
        '''
