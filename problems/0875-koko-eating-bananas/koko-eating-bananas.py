class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        if h == len(piles):
            return max(piles)

        lewo, prawo = 1, max(piles)
        banany = (lewo+prawo) // 2

        # for banany in range(1, max(piles)+1):
        while lewo <= prawo:
            kopki = piles.copy()
            banany = (lewo+prawo) // 2
            
            # obecna_kopka, dzien = 0, 0
            # while obecna_kopka != len(piles) and dzien < h:
            #     kopki[obecna_kopka] -= banany
            #     if kopki[obecna_kopka] <= 0:
            #         kopki[obecna_kopka] = 0
            #         obecna_kopka += 1
            #     dzien += 1

            obecna_kopka, dzien = 0, 0
            while obecna_kopka != len(piles) and dzien <= h:
                ilosc_dni = kopki[obecna_kopka] // banany + (1 if kopki[obecna_kopka]%banany != 0 else 0)

                obecna_kopka += 1
                dzien += ilosc_dni
            
            if dzien <= h:
                prawo = banany - 1

            else:
                lewo = banany + 1

        return lewo



        
