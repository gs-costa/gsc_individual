
def sumNumbers():
    num1 = input('num1:')
    num2 = input('num2:')
    soma = int(num1) + int(num2)
    print('A soma é:', soma)

def showNumber():
    number = input('Insira um número:')
    print('O número informado foi',number)

def avgGrades():
    grade1 = int(input('grade1:'))
    grade2 = int(input('grade2:'))
    grade3 = int(input('grade3:'))
    grade4 = int(input('grade4:'))
    averageGrades = (grade1 + grade2 + grade3 + grade4)/4
    print('Média das notas é:',averageGrades)

def calcSalary():
    hourearn = float(input('Ganho por hora:'))
    workhours = int(input('Horas trabalhadas no mês:'))
    salariobruto = hourearn*workhours
    if salariobruto <= 900:
        aliquota_ir = 0
    if salariobruto <= 1500:
        aliquota_ir = 5
    if salariobruto <= 2500:
        aliquota_ir = 10
    else:
        aliquota_ir = 20

    ir = aliquota_ir/100 * salariobruto
    inss = 0.1 * salariobruto
    sindicato = 0.03 * salariobruto
    FGTS = 0.11 * salariobruto
    salarioliquido = salariobruto - ir - inss
    print('Salário bruto:     R$', salariobruto)
    print(f'(-) IR ({aliquota_ir}%):      R$', ir)
    print('(-) INSS (10%):    R$', inss)
    print('Sindicato (3%):    R$', sindicato)
    print('FGTS (11%):        R$', FGTS)
    print('Total descontos:   R$', ir + inss)
    print('Salário líquido:   R$', salarioliquido)

def pesoIdeal():
    woman_man = input('Insira M para mulher e H para homens: ').upper()
    altura = float(input('Altura da pessoa: '))
    if woman_man == 'H':
        peso_ideal = (72.7 * altura) - 58
        print('O peso ideal é:',peso_ideal)
    elif woman_man == 'M':
        peso_ideal = (62.1 * altura) - 44.7
        print('O peso ideal é:',peso_ideal)
    else:
        print('Gênero inválido!')

def precoItens():
    qtditens = range(1,51)
    print('Loja Quase Dois - Tabela de preços')
    precoitens = [i * 1.99 for i in qtditens]
    for i in qtditens:
        print(i, '- R$',precoitens[i-1])

def caixaRegistradora():
    print()

if __name__ == '__main__':
    
    precoItens()