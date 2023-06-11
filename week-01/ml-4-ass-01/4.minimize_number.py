
N = int(input())

numbers = []

for i in range(N):
    numbers.append(int(input()))

divisorCount = 0
all_even = True

while all_even:
    all_even = True
    for i in range(N):
        if numbers[i] % 2 != 0:
            all_even = False
            break
        numbers[i] //= 2
    if all_even:
        divisorCount += 1

print(divisorCount)
