
# def wrapper(f):
#     def fun(l):
#         f([f"+91 {i[-10:-5]} {i[-5:]}" for i in l])# complete the function
#     return fun

# @wrapper
# def sort_phone(l):
#     print(*sorted(l), sep='\n')

# if __name__ == '__main__':
#     #l = [input() for _ in range(int(input()))]
#     l = ['07895462130', '919875641230', '9195969878']
#     sort_phone(l) 

#########################
import operator

def person_lister(f):
    def inner(people):
        people.sort(key = lambda i: int(i[2]))
        return [f(i) for i in people]
    return inner

@person_lister
def name_format(person):
    #print(person)
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    #people = [input().split() for i in range(int(input()))]
    people = [['Mike', 'Thomson', '20', 'M'], ['Robert', 'Bustle', '32', 'M'], ['Andria', 'Bustle', '30', 'F']]
    print(*name_format(people), sep='\n')