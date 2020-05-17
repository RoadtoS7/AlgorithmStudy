import sys
input = list(map(int,sys.stdin.readline().rstrip('\n')))
input.sort(reverse=True)
print(''.join(str(x) for x in input))
