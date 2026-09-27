class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Input: A string s containing letters, numbers, sopaces, punctyations, et.c

        Output: rteurn True if the string is a palindrone after
            - converting uppercase letters to lowercase
            - removing all non-alphanumeric characters

        Otherwise return False

        For example

        "A man, a plan, a canal: Panama"
                        ⬇
               amanaplanacanalpanama
                        ⬇
                Palondrone -> True

        Goal: We ned to compare the characters from the beginning and the end after ignoring characters that aren't letters or numbers.

        Realistic edge cases:
        1. " " -> everything gets removed -> "" -> return True
        2. "a" -> one character -> return True
        3. "ab" -> different characters -> return False
        4. "a." -> becomes -> "a" -> return True
        5. "0p" -> becomes "0p" -> return False

        - - -

        Brute-Force Approach
        The straightforward idea is: clean the string and then check whether the cleaned string is the same forward and backward

        For example:
        "A man, a plan, a canal: Panama"
        
        "amanaplanacanalpanama"
        "amanaplanacanalpanama"

        They're equal ?> return True

        Algorithm
        1. Create an empty string called cleaned
        2. Loop through every character in s
        3. If the character is alphanumeric, add lowercase version to string
        4. compare cleaned string to the reversed string
        5. return the result

        Pseudocode:
        cleaned = ""

        for char in s:
            if char is alphanuymerice:
                add cha to cleaned

            if cleaned is equal to reveresed cleaned:
                return True

        Time compexity: O(n) because we loop though every characre in the string
        Space complexity; O(n) because we cteated cleaned; an etra data structure

        - - -

        Optimized Approach(Two pointers)
        instead of creating a cleaned string, we can examine the original string from both ends simultaneously

        so, we'll initiate two pointers called left and right

        left = 0
        right = len(s) -1

        Then:
        - left moves toward the right
        - right moves toward the left
        - Skip any non-alphanumeric characters
        - Compare the characters when both pointers are on valid characters
        - If they differ -> False
        - if they match -> move inward

        Walkthrough:
        s = " A man, a plan, a canal: Panama"
              ↑                            ↑
              L                            R

        L -> A
        R -> a

        Both are same after conversion to lowercase characters.
        We skip punctuations ans spaces, and move both pointers inward

        s = " A man, a plan, a canal: Panama"
                ↑                         ↑
                L                         R

        We continue like that ooo until:

        left >= right

        If we never find a mismatch, it's a palindrome.

        Algorithm:
        1. Create a pointer Left that starts from zero
        2. Create a pointer Right that starts from len(s) - 1; the end of the list
        3. While left < right:
            - if left[s] is not alphanumeric, move left forward
            - if right is not alphanumeric, move right backward
            - otherwise, compare the lowercase versions
            - if they are different, return False
            - Move both pointers inwards
        4. return True

        Pseudocode:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and s[left] is not alphanumeric:
                left += 1
            
            while left < right and s[right] is not alphanumeric:
                right -= 1

            if lowercase(s[left]) != lowercase(s[right]):
                retuen False

            left += 1
            right -= 1

        retyrn True

        Time complexity: O(n) because we still loop through each character in s
        Space complexity: O(1) because we didn't create any extra data structure
        """
        # # Brute Force Approach
        # cleaned = ""
        
        # for char in s:
        #     if char.isalnum():
        #         cleaned += char.lower()
            
        #     cleaned_reversed = cleaned[::-1]
            
        # return cleaned == cleaned_reversed

        # Optimized Approach
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not self.alphaNum(s[left]):
                left += 1

            while left < right and not self.alphaNum(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


    def alphaNum(self, char):
        return (
            ord('A') <= ord(char) <= ord('Z') or
            ord('a') <= ord(char) <= ord('z') or
            ord('0') <= ord(char) <= ord('9')
        )
