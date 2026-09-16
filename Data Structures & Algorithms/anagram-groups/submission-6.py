class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap: dict[tuple[int,...], list[str]] = {}
        for string in strs:
            count = [0] * 26
            for word in string :
              value = ord(word) -ord("a")
              count[value] += 1
            key = tuple(count)
            if key not in hashmap:
               hashmap[key]=[]
            hashmap[key].append(string)
        return list(hashmap.values())


