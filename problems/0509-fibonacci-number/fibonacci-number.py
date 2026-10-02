class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        poprzedni, wynik = 1, 1
        for i in range(3, n + 1):
            poprzedni, wynik = wynik, poprzedni + wynik  # ciekawy trik
        return wynik