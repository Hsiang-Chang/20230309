import sys

def q2(string):

    counter = dict()

    for i in string.replace(" ", ""):
        counter[i.upper()] = counter[i.upper()] + 1 if i.upper() in counter else 1
    
    sorted_counter = dict(sorted(counter.items()))
    print('\n'.join(k+" "+str(v) for k, v in sorted_counter.items()))

if __name__ == '__main__':
    q2(sys.argv[1])