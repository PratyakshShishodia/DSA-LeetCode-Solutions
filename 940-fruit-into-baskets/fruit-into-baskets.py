class Solution(object):
    def totalFruit(self, fruits):
        l = 0
        freq = {}
        max_len = 0
        for r in range (len(fruits)):
            freq[fruits[r]] = freq.get(fruits[r],0)+1

            while len(freq)>2:
                freq[fruits[l]]-=1

                if freq[fruits[l]]==0:
                    del freq[fruits[l]]
                l+=1
            max_len = max(max_len,r-l+1)
        return max_len
            
          
      