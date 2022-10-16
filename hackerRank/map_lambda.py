# cube = lambda x: x**3 # complete the lambda function 

# def fibonacci(n):
#     if n < 2:
#         return [lista_fibonacci for lista_fibonacci in range(n)]
#     else:
#         lista_fibonacci = [0,1]
#         for i in range(2,n):
#             novo = lista_fibonacci[i-2] + lista_fibonacci[i-1]
#             lista_fibonacci.append(novo)
#         return lista_fibonacci# return a list of fibonacci numbers

# if __name__ == '__main__':
#     #n = int(input())
#     n= 1
#     print(list(map(cube, fibonacci(n))))


############## Validating email
import re

regex = re.compile("^[a-z0-9A-Z_-]+[@]\w[a-zA-Z0-9]+[.]([a-zA-Z]){1,3}$")

def fun(s):
    if regex.search(s):
        return True
    else: 
        return False
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    # n = int(input())
    # emails = []
    # for _ in range(n):
    #     emails.append(input())
    
    emails = [
        'lara@hackerrank.com',
        'mike13445@yahoomail9.server', 
        'rase23@ha_ch.com', 
        'daniyal@gmail.coma',
        'thatisit@thatisit']

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)