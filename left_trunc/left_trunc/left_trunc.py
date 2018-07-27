from primetest import miller_rabin

list = [2]
#n is the current number, k is the length of the current number
def check_grow(n, k=1):
    if(miller_rabin(n,10)==False):
        return 
    list.append(n)
    for i in range(1,10):
        new = n + i * pow(10, k)
        check_grow(new, k+1)
check_grow(3)
check_grow(5)
check_grow(7)

print("These are all the left-truncatable primes, where every suffix is prime and no digits are zero. \n")

for el in sorted(list):
    print("%d" %el)

print("\n There are a total of %d left-truncatable primes." % len(list))
