#coding=utf-8

import csv

def loadCSV(filename, dtype='int64'):
    dataset = {'order':[], 'variables':{}}
    
    with open(filename, 'rU') as f:
        reader = csv.reader(f)
                
        varDeclareRow = reader.next()
        varDefineRow = reader.next()
                
        # 1,2行目から、各変数の定義を読み取る
        for i, v in enumerate(varDeclareRow):
            if v:
                var = v
                dataset['order'].append(var)

            dataset['variables'].setdefault(var, {'factors':[]})
            dataset['variables'][var]['factors'].append(varDefineRow[i])

        for var in dataset['variables']:
            dataset['variables'][var]['dim'] = len(dataset['variables'][var]['factors'])

        DATA = numpy.matrix([row for row in reader], dtype=dtype)

        ps = 0
        for var in dataset['order']:
            dataset['variables'][var]['DATA'] = DATA[:,ps:ps+dataset['variables'][var]['dim']]
            ps = dataset['variables'][var]['dim']

#         for key, val in  dataset['variables'].items():
#             print key, val

    return dataset

def loadTXT(filename, delimiter=None, format=None):
    DATA =  numpy.loadtxt(filename, delimiter=delimiter)
    print DATA

    # format must be following style "{'y':(0,2), 'x':(2,12)}"
    for key,val in format.items():
        print key, DATA[:,val[0]:val[1]]

    return DATA
