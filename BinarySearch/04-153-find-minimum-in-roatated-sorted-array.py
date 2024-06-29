ex = 'https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/m'

class Solution:
    def findMin(self, a: List[int]) -> int:
        #approccio solo con <, perche non sappiamo bene definire guess == target
        
        #contesto (routare means prendi un pezzo e mettilo davanti)
        #[1,2,3,4,5]
        #[1,2] [3,4,5]
        #malo swap
        #[3, 4, 5, 1, 2]

        #dal fatto che swappiamo avremmo due array sortati nel nostro array
        #se mid finisce nel primo array e right nel'altro il sub array mid-right non e' sort
        #mentre e' garantito che il resto e' sort
        
        #ex: 5 < 2 (da 5 a 2 no sorted) ma (da 3 5 si sorted)
        # 3 4 5 1 2
        #     /
        #   /     /
        # /     /
       
        #se consideriamo normale approch bs with left, mid, right
        #abbiamo 3 situazioni possibili
        
        # mid > right:
        #[3, 4, 5, 1, 2]
            #il minimo sara per forza tra mid + 1 e right essendo che right e' piu piccolo di mid
            #un numero piu piccolo di right deve stare alla sua destra
            #essendo che la parte destra e' unsorted c'e' la rotazione e quindi il continuo di right starta#
            #a left e quindi se vuoi un numero piu piccolo di right vai a right di right oddio si e' capito
            #(left = mid + 1)


        # mid < right
        #[5, 1, 2, 3, 4]
            #sai che da mid a right so tutti sorted, e mid e quindi il piu piccolo da mid a right
            #quindi sai che tutti i numeri dopo mid non servono, mentre mid portebbe essere 
            #(right = mid)

        # mid == right
        #[1, 2, 3, 3, 3]
            #stesso ragionamento di spora tutti i numeri saranno uguali, te ne basta uno quello di mid
            #(right = mid)

        #spiegazione assurda per un codice piccolissimo(ma serve per capire bene find target in rotated
        #sorted array)

        left, right = 0, len(a) - 1

        while left < right:
            mid = (left + right) // 2

            if a[mid] > a[right]:
                left = mid + 1
            else:
                right = mid

        return a[left]



