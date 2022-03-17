# triggered by algo-is_prime snippet text
def is_prime(n: int) -> bool:
    """
    Return True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    else:
        for i in range(5, int(n**0.5)+1, 6):
            if n % i == 0 or n % (i+2) == 0:
                return False
        return True

# triggered by algo-fast_expo snippet text
def fast_power(x: float, y: int) -> int:
    """
    Return x^y with O(log(n)) Time Complexity.
    """
    if y == 0:
        return 1
    elif y == 1:
        return x
    elif y == -1:
        return 1/x
    else:
        ans = fast_power(x, y//2)
        if y % 2 == 0:
            return ans*ans
        else:
            return ans * ans * x

def greatest_common_divisor(a: int, b: int) -> int:
    """
    Euclid's Lemma :  d divides a and b, if and only if d divides a-b and b
    Euclid's Algorithm

    >>> greatest_common_divisor(7,5)
    1

    Note : In number theory, two integers a and b are said to be relatively prime,
        mutually prime, or co-prime if the only positive integer (factor) that divides
        both of them is 1  i.e., gcd(a,b) = 1.

    >>> greatest_common_divisor(121, 11)
    11
    """
    if a < b:
        a, b = b, a

    while a % b != 0:
        a, b = b, a % b

    return b
