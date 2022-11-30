# version 1
def even_odd_sums(sequence):
    odd_sum = 0
    even_sum = 0
    for n in range(len(sequence)):
        if n % 2 == 0:
            even_sum = even_sum + sequence[n]
        else:
            odd_sum = odd_sum + sequence[n]
    return [even_sum, odd_sum]

print(even_odd_sums((10, 20, 30, 40, 50, 60)))


# version 2
def even_odd_sums1(sequence):
    
    odd_sum =  [n for n in sequence if sequence.index(n) % 2 != 0]
    even_sum =  [n for n in sequence if sequence.index(n) % 2 == 0]
    return [sum(even_sum), sum(odd_sum)]

print(even_odd_sums1([10, 20, 30, 40, 50, 60]))

# version 3
def even_odd_sums2(sequence):
    
    odd_sum =  []
    even_sum =  []
    for number in sequence:
        if not sequence.index(number) % 2:
            even_sum.append(number)
        else:
            odd_sum.append(number)
    return [sum(even_sum), sum(odd_sum)]

print(even_odd_sums2([10, 20, 30, 40, 50, 60]))

