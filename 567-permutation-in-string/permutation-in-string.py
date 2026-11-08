class Solution(object):
    def checkInclusion(self, s1, s2):
        freq1={}
        freq2={}
        n1=len(s1)
        n2=len(s2)

        if n1>n2:
            return False
        
        for ch in s1:
            freq1[ch]= freq1.get(ch,0)+1

        for i in range(0,n1):
            freq2[s2[i]] = freq2.get(s2[i],0)+1

        if freq1 == freq2 :
            return True

        l =0 
        for r in range (n1, n2):
            freq2[s2[r]] = freq2.get(s2[r],0)+1
            freq2[s2[l]]-=1
            if freq2[s2[l]]==0:
                del freq2[s2[l]]
            l+=1

            if freq1== freq2:
                return True
        

        return False
        
        
       
        