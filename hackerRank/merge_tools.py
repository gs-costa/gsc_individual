from math import ceil

def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    linhas = ceil(n/ k)
    cont = 1
    for i in range(linhas):
        inicio = 0 if i == 0 else fim
        fim = k*cont if i != 0 else k
        ui = ''
        for letra in string[inicio: fim]:
            if letra not in ui:
                ui += letra
        print(ui)
        cont += 1
    #print(u)


if __name__ == '__main__':
    #string, k = input(), int(input())
    string = 'AAABCADDE'
    k = 3
    merge_the_tools(string, k)