import sys

def q1(num):
    if (num % 2 == 0) and ((num >= 2 and num < 5) or (num > 20)):
        print("O")
    else:
        print("X")

if __name__ == '__main__':
    q1(sys.argv[1])