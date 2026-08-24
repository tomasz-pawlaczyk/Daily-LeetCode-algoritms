class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        wynik = []

        def backtrack(aktualny, otwarte, zamkniete):
            if len(aktualny) == 2 * n:
                wynik.append(aktualny)
                return
            if otwarte < n:
                backtrack(aktualny + "(", otwarte + 1, zamkniete)
            if zamkniete < otwarte:
                backtrack(aktualny + ")", otwarte, zamkniete + 1)

        backtrack("", 0, 0)
        return wynik

        
        