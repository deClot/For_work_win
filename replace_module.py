def replace(file):
    file = file.replace('+',' ')
    file = file.replace('-',' ')
    file = file.replace('?',' ')
    file = file.replace('shum',' ')
    file = file.replace('out of range',' ')
    file = file.replace('vr',' ')
    file = file.replace('w',' ')
    file = file.replace('I',' ')
    file = file.replace('no line',' ')
    file = file.replace('_',' ')
    file = file.replace('cd',' ')
    file = file.replace('p',' ')
    file = file.replace('forbidden',' ')
    file = file.replace('sliplis',' ')
    #print(type(file))
    
    return file
