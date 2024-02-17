
def read_file():
    file = open("emd.csv", "r", encoding="utf-8", newline="")
    data = []
    for line in file:
        row = line.strip().split(",")
        data.append(row)
    return data


def sort_data(data, oi):
    data.sort(key=lambda x: x[oi])
    return data

def getModalidades(data):
    modalidades = []
    for i in range(len(data)-1):
        if data[i+1][8] not in modalidades:
            modalidades.append(data[i+1][8])
        
    print(sorted(modalidades))

def percentagem(data):
    cont = 0
    for i in range(len(data)):
        if data[i][12] == "true":
            cont += 1
    
    percentagem = (cont / (len(data)-1)) * 100
    print(percentagem)

def printEscaloes(escaloes):
    for key in escaloes:
        if escaloes[key] != 0:
            print(f"{key}: {escaloes[key]}")


def escaloes(data):
    escaloes = {'0-4': 0, '5-9': 0, '10-14': 0, '15-19': 0, '20-24': 0, '25-29': 0, '30-34': 0, '35-39': 0, '40-44': 0, '45-49': 0, '50-54': 0, '55-59': 0, '60-64': 0, '65-69': 0, '70-74': 0, '75-79': 0, '80-84': 0, '85-89': 0, '90-94': 0, '95-99': 0, '100+': 0}

    for i in range(len(data)-1):
        if int(data[i+1][5]) <= 4:
            escaloes['0-4'] += 1
        elif int(data[i+1][5]) <= 9:
            escaloes['5-9'] += 1
        elif int(data[i+1][5]) <= 14:
            escaloes['10-14'] += 1
        elif int(data[i+1][5]) <= 19:
            escaloes['15-19'] += 1
        elif int(data[i+1][5]) <= 24:
            escaloes['20-24'] += 1
        elif int(data[i+1][5]) <= 29:
            escaloes['25-29'] += 1
        elif int(data[i+1][5]) <= 34:
            escaloes['30-34'] += 1
        elif int(data[i+1][5]) <= 39:
            escaloes['35-39'] += 1
        elif int(data[i+1][5]) <= 44:
            escaloes['40-44'] += 1
        elif int(data[i+1][5]) <= 49:
            escaloes['45-49'] += 1
        elif int(data[i+1][5]) <= 54:
            escaloes['50-54'] += 1
        elif int(data[i+1][5]) <= 59:
            escaloes['55-59'] += 1
        elif int(data[i+1][5]) <= 64:
            escaloes['60-64'] += 1
        elif int(data[i+1][5]) <= 69:
            escaloes['65-69'] += 1
        elif int(data[i+1][5]) <= 74:
            escaloes['70-74'] += 1
        elif int(data[i+1][5]) <= 79:
            escaloes['75-79'] += 1
        elif int(data[i+1][5]) <= 84:
            escaloes['80-84'] += 1
        elif int(data[i+1][5]) <= 89:
            escaloes['85-89'] += 1
        elif int(data[i+1][5]) <= 94:
            escaloes['90-94'] += 1
        elif int(data[i+1][5]) <= 99:
            escaloes['95-99'] += 1
        else:
            escaloes['100+'] += 1

    printEscaloes(escaloes)


data = read_file()
escaloes(data)