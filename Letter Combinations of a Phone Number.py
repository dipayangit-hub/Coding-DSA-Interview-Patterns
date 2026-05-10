class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        map={
            "1":[],
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        res=[]

        def backtrack(digits,map,index,l):
            if index==len(digits):
                res.append("".join(l))
                return

            
            for ch in map[digits[index]]:
                l.append(ch)
                backtrack(digits,map,index+1,l)
                l.pop()
        
        backtrack(digits,map,0,[])
        return res

print(Solution().letterCombinations("23"))