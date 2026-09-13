### 242. Valid Anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Input: two strings `s` and `t` (both contains lowercase English letters)
        
        Output: return
        - True if both strings are anagram
        - False otherwise

        Goal: here is to determine whether both strings contain the same
        characters with the same frequencies, regardless of their order.

        Edge cases:
        - When both strings are not of the same length -> return False
            e.g s = "abc"
                t = "ab"
        - When both strings does not contain same number of characters -> return False
            e.g s = "aab"
                t = "abb"
        - When both strings have exactly one and same character -> return True
            e.g s = "b"
                t = "b"

        - When both strigs has exactly one but different characters -> return False
            e.g s = "a"
                t = "b"

        Walkthrough:
        What would I naturally do to determine whether these two strings are anagrams?

        Example 1:
        s = "r a c e c a r"
             0 1 2 3 4 5 6

        t = "c a r r a c e"
             0 1 2 3 4 5 6

        Because the letters in both strings are placed in different positions, we can't compare s[0] with t[0], so what can we do?

        Let me count and keep track of how many times each letter appear in string s:

        s = "r a c e c a r"
            0 1 2 3 4 5 6
                        ↑  

        r -> 1
        a -> 1
        c -> 1
        e -> 1
        c -> 1
        a -> 1
        r -> 1

        So, when we aggregate it:
        r -> 2
        a -> 2
        c -> 2
        e -> 1

        We do same for  string t:

        t = "c a r r a c e"
             0 1 2 3 4 5 6
             ↑

        c -> 1
        a -> 1
        r -> 1
        r -> 1
        a -> 1
        c -> 1
        e -> 1

        So, we aggregate it:
        c -> 2
        a -> 2
        r -> 2
        e -> 1

        So, the counts are exactly same, and we return True

        - - - 

        Brute Force Approach
        One thing I could do is to sort both strings and compare them.

        Example 1:

        s = "racecar"
        sorted_s = "aaccerr"

        t = "carrace"
        sorted_t = "aaccerr"

        Both are identical and will return True

        Example 2:

        s = "jar"
        sorted_S = "ajr"

        t = "jam"
        sorted_t = "ajm"

        Both aren't identical so we return False

        Algorithm:
        1. if the two strings do not have same length, return False
        2. sort s
        3. sort t
        4. compare sorted strings
        5. if they're equal, return True
        6. Otherwise, we return False

        Pseudocode:
        if len(s) != len(t)
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s == sorted_t
            return True

        Retrun False

        Time complexity: O(n log n) because sorted under the hood is O(n log n)
        sorted_s = O(n log n)
        sorted_t = O(n log n)
        i.e O(n logn n) + O(n logn n) = O(n logn n)

        Space complexity: sorted uses an additional extra space which is O(n)

        - - -

        Optimized Approach

        Sorting can solve an anagram problem, but sorting takes extra time.
        A hash map approach counts characters in each string and compares the counts.

        i.e we will have count = {}

        Then for s = "racecar"

        r -> 2
        a -> 2
        c -> 2
        e -> 1
        r -> 2

        Then as we process t, we can substract from those counts.

        Algorithm:
        1. If both strings have different length, return False
        2. Create a hash map, called count
        3. Go through s and add 1 to the count of each character
        4. Go through t and substract 1 from the count of each character
        5. If both counts all end at zero, the strings are anagram
        6. Otherwise, they are not

        Pseudocode:
        if len(s) != len(t):
            return False

        count = {}

        for each char in s
            increase count[char] by 1

        for each char in t
            decrease count[char] by 1

        for each character in count
            if count[character] != 0
                return False

        return True
        
        Time Complexity: O(n) because we loop through each character in both strings exactly once
        Space complexity: O(1) because the the number of characters can never pass 26 which is the number of English letters.

        But if the input contain unicode cahracters, using a hash map stiil works, because Python dictionary still support 
        unicode characters as keys, so the same frequencey counting algorithm works without modification. I would avoid a
        fixed-sized array of 26 elements because that assumes only lowercase English letters.
        """
        # # Brute Force Approach (Using Sorted)
        # if len(s) != len(t):
        #     return False

        # sorted_s = sorted(s)
        # sorted_t = sorted(t)

        # if sorted_s == sorted_t:
        #     return True

        # return False

        ######################################

        # Optimized Approach (Using a Hash Map)
        # Check if both strings have same length
        if len(s) != len(t):
            return False

        count = {}

        # Building the map with string s
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1

        # Check if characters in t are same characters in s
        for char in t:
            if char in count:
                count[char] -= 1
            else:
                return False

        # confirming character ferquency
        for char in count:
            if count[char] != 0:
                return False

        return True
