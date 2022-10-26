from math import sqrt, asin, degrees

def find_MBC(AB, BC):
    AC = sqrt(AB**2 + BC**2)
    beta = round(degrees(asin(AB/AC)))
    teta = 90-beta
    print(f'{beta}\xb0')

if __name__ == '__main__':
    # AB = int(input())
    # BC = int(input())
    AB = 15
    BC = 10

    find_MBC(AB, BC)