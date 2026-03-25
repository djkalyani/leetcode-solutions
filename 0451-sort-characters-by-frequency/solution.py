class Solution:
    def frequencySort(self, s: str) -> str:

        char_count = Counter(s) 
        #returns {'e':2,'r':1,'t':1}

        sorted_char = sorted(char_count,key=char_count.get,reverse=True)
        # sorted(item,key=,reverse=) 

        result_string = ''
        for c in sorted_char:
            result_string += c * char_count[c]

        return result_string
        
        
        
