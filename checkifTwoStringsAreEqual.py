def arrayStringsAreEqual(word1, word2) -> bool:
    stringOne = ''
    finalFirstString = stringOne.join(word1)
    stringTwo = ''
    finalSecondString = stringTwo.join(word2)
    if(finalFirstString == finalSecondString):
        return True
    else:
        return False


#leetcode link https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/