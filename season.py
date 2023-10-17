#totalmente modificado por mim
mes = input('Diga em que mês você esta: ')
dia = input('Diga em que dia você esta: ')
if mes == ('1', '2' or '3') and dia >= '20':
    print('É verão')
else:
    if mes == ('4', '5' or '6') and dia >= '21':
        print('É outono')
    else:
        if mes == '7' or '8' or '9' and dia >= '23':
            print('É inverno')
        else:
            if mes == '10' or '11' or '12' and dia >= '22':
                print('É primavera')
            else:
                print('Esta data não existe')
