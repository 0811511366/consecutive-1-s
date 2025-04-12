def longest_consecutive_ones(num):
    binary_str = bin(num)[2:]
    print(f"Binary representation of {num} is: {binary_str}")
    
    max_ones = max(len(part) for part in binary_str.split('0'))
    return max_ones
    
number = int(input("Enter a number: "))
result = longest_consecutive_ones(number)
print(f"Longest consecutive 1's: {result}")
