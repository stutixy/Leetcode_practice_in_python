class Solution:
    def countGoodNumbers(self, n: int) -> int:
        evenPositions = 0
        oddPositions = 0
        mod = (10**9 + 7)
        if n%2 :
            oddPositions = math.floor(n/2)
            evenPositions = math.ceil(n/2)
        else:
            evenPositions = oddPositions = n//2 
        return (self.power(5,evenPositions,mod) * self.power(4,oddPositions,mod)) % mod
        
    
    def power(self, base, power, mod):
        if power == 0:
            return 1
        half = self.power((base*base)%mod, power //2, mod)
        half %= mod
        return (base * half)%mod if power % 2 else half
        