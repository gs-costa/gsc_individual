#!/bin/python3
import re

lista = [
    "Francois XXIV",
    "Francois XXV",
    "Bruce XLI",
    "Bruce XVIII",
    "Maru XVIII",
    "Maru XXXIV",
    "Francois XXI",
    "Francois XXII",
    "Francois XL",
    "Francois VI",
    "Louis XV",
    "Louis XXIX",
    "Louis XLI",
    "Louis XLIII",
    "Luka I",
    "Luka XVII",
    "Bruce XXVI",
    "Bruce XXVII",
    "Luka XXII",
    "Luka XXXVII",
    "Luka XLII",
    "Paul XX",
    "Maru XXXV",
    "Maru XLI",
    "Mary XXIV",
    "Mary XXVIII",
    "Mary XXX",
    "Mary XXXV",
    "Mary XLII",
    "Mimino XXXVIII",
    "Paul VI",
    "Paul VIII",
    "Paul XVII",
    "Tomek MIX",
    "Paul XLIX",
    "Petrzlen I",
    "Rasto XV",
    "Petrzlen XVI",
    "Petrzlen XX",
    "Petrzlen XXXIV",
    "Petrzlen XXXVII",
    "Philippe VII",
    "Philippe XV",
    "Philippe XXXVIII",
    "Philippe L",
    "Tomek V",
    "Tomek VIII"
    ]

# Complete the 'sortRoman' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY names as parameter.
#
romanos_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}

def changeRomanToDecimal(nome_romano):

    n = nome_romano[nome_romano.find(' ')+1:]
    decimal=0
    entrou = False

    for i in range(len(n)):
        if entrou == True:
            entrou = False
            continue
        try:
            prox_num = romanos_dict[n[i+1]]
        except:
            prox_num = romanos_dict[n[len(n)-1]]
        if romanos_dict[n[i]] < prox_num:
            decimal = prox_num - romanos_dict[n[i]] + decimal
            entrou = True
        else:
            decimal += romanos_dict[n[i]]
    
    nome_decimal = nome_romano[:nome_romano.find(' ')] \
        + ' ' + str(decimal)

    return nome_decimal
        

def sortRoman(names):
    # Write your code here
    nomes_decimais = []
    nomes_dict = {}
    for n in names:
        nome_decimal = changeRomanToDecimal(n)
        nomes_dict[n] = nome_decimal
        nomes_decimais.append(nome_decimal)
    
    lista_ordenada = []
    for key, value in nomes_dict.items():
        temp1 = re.findall(r'([A-z]+) (\d+)', value)
        nomes_dict[key] = (temp1[0][0], int(temp1[0][1]))
    lista_ordenada = sorted(nomes_dict.items(), key = lambda kv:(kv[1], kv[0]))

    sortedRoman = []
    for item in lista_ordenada:
        sortedRoman.append(item[0])
        #print(item[1][0], item[1][1])
    
    return sortedRoman

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # names_count = int(input().strip())

    names = lista

    # for _ in range(names_count):
    #     names_item = input()
    #     names.append(names_item)

    result = sortRoman(names)

    print('\n'.join(result))
    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()