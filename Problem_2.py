def prime_factorization(n):
    factors=[]
    c=0
    while n%2==0:
        n//=2
        c+=1
        
    if c>0:
        factors.append((2, c))
    for odd_factor in range(3, int(n**0.5) + 1, 2):
        count=0
        while n%odd_factor==0:
            n//=odd_factor
            count+=1
        if count>0:
            factors.append((odd_factor, count))
    if n>2:
        factors.append((n, 1))
    return factors

# Main Function
number = 100
result = prime_factorization(number)
print(result)