N = int(input())
numbers = list(map(int, input().split()))



def first(numbers):
    count = 0

    for number in numbers:
        if number == 1:
            continue
        for i in range(2, number):
            if number % i == 0:
                break
        count += 1
    print(count)

print('numbers: ', first(numbers))