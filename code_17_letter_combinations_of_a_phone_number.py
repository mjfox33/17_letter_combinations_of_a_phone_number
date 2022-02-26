from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        rosetta = {
            '2':['a','b','c'], 
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r', 's'],
            '8':['t','u','v'],
            '9':['w','x','y', 'z']
        }

        result = [''] if digits else []
        for d in digits:
            result = [i + j for i in result for j in rosetta[d]]
        return result
