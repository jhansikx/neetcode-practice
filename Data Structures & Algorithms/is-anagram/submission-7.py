class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) :
          return False
        input1 = dict ()
        input2 = dict ()
        for char in s :
          input1[char] = input1.get(char,0) +1 

        for char in t :
          input2[char] = input2.get(char,0) +1
              
        for key in input1 :
          if input1[key] != input2.get(key, 0) :
           return False
        return True

           

