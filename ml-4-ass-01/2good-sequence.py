def minimum_removal(N, a):
    freq = [0] * (N + 1)
    print(freq)
    # Count the occurrences of each element in the sequence
    for num in a:
        freq[num] += 1
        print
    print(freq)
    removals = 0
    
    # Check if each element violates the good sequence condition
    for i in range(1, N + 1):
        if freq[i] > i:
            removals += freq[i] - i
            print(freq[i])
    
    return removals


# Read input from standard input
N = int(input())
a = list(map(int, input().split()))

print(a[2])

# Call the function and print the result
print(minimum_removal(N, a))
