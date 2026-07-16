class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(char for char in s if char.isalnum())
        final = word.lower()
        if final[::-1] == final:
            return True
        return False
