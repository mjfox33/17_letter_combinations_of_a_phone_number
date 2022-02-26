from code_17_letter_combinations_of_a_phone_number import Solution

def test_example_1():
    s = Solution()
    digits = "23"
    output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert s.letterCombinations(digits) == output