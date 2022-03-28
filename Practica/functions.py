import csv
import literals as msg
import libreria

def omplir():
    cl = dict()
    cl['Curs'] = input(msg.MSG2)
    cl['Aula'] = input(msg.MSG3)
    cl['Nº alumnes'] = libreria.validate(msg.MSG4, 0, None)
    cl['Nº professors/es'] = libreria.validate(msg.MSG5, 0, None)
    month = libreria.validate(msg.MES, 1, 12)
    if month % 2 == 0 and month != 2:
        day = libreria.validate(msg.DIA, 1, 28)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day = libreria.validate(msg.DIA, 1, 30)
    else:
        day = libreria.validate(msg.DIA, 1, 31)
    year = libreria.validate(msg.ANY, 2021, 2025)
    cl['Dia'] = str(day) + '/' + str(month) + '/' + str(year)
    cl['Hora de classe'] = input(msg.MSG6)
    cl['Nom professor/a'] = input(msg.MSG7).capitalize()
    cl['Assignatura'] = input(msg.MSG8)
    return cl


def introduir(f_name, head, method):
    aux = 1
    try:
        with open(f_name, method, encoding='utf-8', newline='\n') as csvfile:
            fieldnames = ['Curs', 'Aula', 'Nº alumnes', 'Nº professors/es', 'Dia', 'Hora de classe', 'Nom professor/a',
                          'Assignatura']
            writecsv = csv.DictWriter(csvfile, fieldnames=fieldnames)
            lines = linecount(f_name)
            if head == 0 or method == 'w' or lines == 0:
                writecsv.writeheader()
            while aux == 1:
                cl = omplir()
                writecsv.writerow(cl)
                aux = libreria.validate(msg.AUX, 0, 1)
    except:
        print(msg.ERROR2)
    else:
        print(msg.NO_ERROR)

def omplir1():
    cl1 = dict()
    month = libreria.validate(msg.MES, 1, 12)
    if month % 2 == 0 and month != 2:
        day = libreria.validate(msg.DIA, 1, 28)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day = libreria.validate(msg.DIA, 1, 30)
    else:
        day = libreria.validate(msg.DIA, 1, 31)
    year = libreria.validate(msg.ANY, 2021, 2025)
    cl1['Dia'] = str(day) + '/' + str(month) + '/' + str(year)
    hour = libreria.validate(msg.HORA, 8, 14)
    min = libreria.validate(msg.MIN, 0, 45)
    while min % 15 != 0
        min = libreria.validate(msg.MIN, 0, 45)
    cl1['Hora'] = str(hour) + ":" + str(min)
    cl1['CO²'] = libreria.validate(msg.MSG18, 0, None)
    cl1['Temp'] = int(input(msg.MSG19))  
    cl1['Humitat'] = libreria.validate(msg.MSG20, 0, 100)
    return cl1

def introduir1(f_name, head, method):
    aux = 1
    try:
        with open(f_name, method, encoding='utf-8', newline='\n') as csvfile:
            fieldnames = ['Dia', 'Hora', 'CO²', 'Temp', 'Humitat']

            writecsv = csv.DictWriter(csvfile, fieldnames=fieldnames)
            lines = linecount(f_name)
            if head == 0 or method == 'w' or lines == 0:
                writecsv.writeheader()
            while aux == 1:
                cl1 = omplir2()
                writecsv.writerow(cl1)
                aux = libreria.validate(msg.AUX, 0, 1)
    except:
        print(msg.ERROR2)
    else:
        print(msg.NO_ERROR)

def omplir2():
    cl2 = dict()
    cl2['Porta principal oberta'] = libreria.validate(msg.MSG9, 1, 60)
    cl2['Porta principal tancada'] = libreria.validate(msg.MSG10, 1, 60 - log['Porta principal oberta'])
    aux = libreria.validate(msg.PORTA, 0, 1)
    if aux == 1:
        cl2['Porta secundària oberta'] = libreria.validate(msg.MSG11, 1, 60)
        cl2['Porta secundària tancada'] = libreria.validate(msg.MSG12, 1, 60 - log['Porta secundària oberta'])
    else:
        cl2['Porta secundària oberta'] = 0
        cl2['Porta secundària tancada'] = 0
    aux = libreria.validate(msg.FIN1, 0, 1)
    if aux == 1:
        cl2['Finestres externes oberta'] = libreria.validate(msg.MSG13, 1, 60)
        cl2['Finestres externes tancades'] = libreria.validate(msg.MSG14, 1, 60 - log['Finestres externes oberta'])
    else:
        cl2['Finestres externes oberta'] = 0
        cl2['Finestres externes tancades'] = 0
    aux = libreria.validate(msg.FIN2, 0, 1)
    if aux == 1:
        cl2['Finestres internes oberta'] = libreria.validate(msg.MSG15, 1, 60)
        cl2['Finestres internes tancades'] = libreria.validate(msg.MSG16, 1, 60 - log['Finestres internes tancades'])
    else:
        cl2['Finestres internes oberta'] = 0
        cl2['Finestres internes tancades'] = 0
    aux = libreria.validate(msg.MSG17, 0, 1)
    if aux == 1:
        cl2['Ventilació creuada'] = 'Sí'
    else:
        cl2['Ventilació creuada'] = 'No'
    return cl2

def introduir2(f_name, head, method):
    aux = 1
    try:
        with open(f_name, method, encoding='utf-8', newline='\n') as csvfile:
            fieldnames = ['Porta principal oberta', 'Porta principal tancada', 'Porta secundària oberta', 'porta secundària tancada',
                          'Finestres exteriors obertes', 'Finestres exteriors tancades', 'Finestres internes obertes',
                          'Finestres interiors tancades', 'Ventilació creuada']

            writecsv = csv.DictWriter(csvfile, fieldnames=fieldnames)
            lines = linecount(f_name)
            if head == 0 or method == 'w' or lines == 0:
                writecsv.writeheader()
            while aux == 1:
                cl2 = omplir2()
                writecsv.writerow(cl2)
                aux = libreria.validate(msg.AUX, 0, 1)
    except:
        print(msg.ERROR2)
    else:
        print(msg.NO_ERROR)

def verificar(file):
    try:
        with open(file, 'r'):
            return 1
    except FileNotFoundError:
        return 0


def crear(f_name, extension):
    if extension in f_name[-len(f_name):]:
        return msg.ROUTE + f_name
    else:
        return msg.ROUTE + f_name + extension


def contador(f_name):
    with open(f_name, encoding="utf8") as csvfile:
        row = 0
        readcsv = csv.DictReader(csvfile, delimiter=',')
        for x in readcsv:
            row = row + 1
        return row

