#!/usr/bin/python
import sys

def repeat(s, times, exclaim):
    if exclaim:
        return (s + '! ') * times
    return (s + ' ') * times

def main():
    if len(sys.argv) > 3:
        print(repeat(sys.argv[1], int(sys.argv[2]), True))
        return 0
    elif len(sys.argv) > 2:
        print(repeat(sys.argv[1], int(sys.argv[2]), False))
        return 0
    else:
        print('no u')
        return 0
    
if __name__ == '__main__':
    main()
