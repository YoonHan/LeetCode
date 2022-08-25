class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1: return 0
        
        is_prime = [True for num in range(n)]
        is_prime[0], is_prime[1] = False, False # 0, 1 is not a prime number
        
        i = 2
        while i * i < n:
            if is_prime[i] == False: 
                i += 1
                continue
            for j in range(i * i, n, i):
                is_prime[j] = False
            i += 1
        
        return is_prime.count(True)