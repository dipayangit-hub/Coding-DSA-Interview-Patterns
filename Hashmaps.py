def wordPattern(pattern, s):
    map={}
    words=s.split(" ")
    if len(pattern)!=len(words):
        return False
    for i in range(len(pattern)):
        if pattern[i] not in map:
            if words[i] in map.values():
                return False
            map[pattern[i]]=words[i]
        
        else:
            if map[pattern[i]]!=words[i]:
                return False
    return True

def isAnagram(s, t):
    map={}
    if len(s)!=len(t):
        return False
    for i in s:
        map[i]=map.setdefault(i,0)+1
    
    for i in t:
        if i not in map or map[i]==0:
            return False
        map[i]=map.setdefault(i)-1
        
    return True

def groupAnagrams(strs):
    map={}
    for i in range(len(strs)):
        freq=[0]*26
        for c in strs[i]:
            freq[ord(c)-ord('a')]+=1
        s=str(freq)
        if s in map:
            map[s].append(strs[i])
        else:
            map[s]=[strs[i]]
    
    return list(map.values())


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))