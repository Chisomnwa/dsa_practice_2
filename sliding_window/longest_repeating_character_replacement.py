class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Input: 
            - s: a sring containing only uppercase English characters
            - k: maximum number of characters we are allowed to replace

        Output: To return the length of the longest contiguos substring that can be turned into all the same character using at most k replacements

        The important word is substring so the characters must be next to each other

        Goal: To loop through the string and find the length of the longest substring that contains the same characters after replacing other characters at most k times

        Example: 
        s = "ABAB"

        We could replace both As with Bs and we'll have: "BBBB"

        We could also replace both Bs with As and we'll have: "AAAA"

        Output for both = 4

        The key idea:
        We ask "How many replacement does a substring need?"

        Suppose we are examining: "AABA"

        Character counts
        A -> 3
        B -> 1

        If we want all characters to be the same, which character should we keep?
        It's A because it already occurs most frequently.

        We only need to replace B with A.

        So:

        Substring length = 4
        Most frequent character count = 3

        Replacements needed = 4 - 3 = 1

        This gives us the importat formula:

        replacements needed = substring length - frequency of the most common character

        A substring is valid when: replacements needed <= k

        For example:
        substring = "AABB"
        k = 2

        length = 4

        A - 2
        B -> 2

        repacements needed = 4 - 2 = 2
        2 < = k

        Sp "AABB" can become "AAAA" or "BBBB"

        Edge Cases:
        1. when k = 0
            e.g s = "AABBB", k = 0
            - We can't replace anything
            - We return the longest substring in that string which is "BBB"
            - Output = 3

        2. When string already contains one repeated character
            e.g s = "AAAA", k = 2
            - No replacements are necessary
            - output = 4

        3. When we have enough replacements for the entire string
            e.g s = "ABCD", k = 3
            - Keep one character and replace the other three
            - e.g longest substring could be "AAAA"
            - output = 4

        4. when we have one character
            e.g s = "a", k = 0
            - Kukuma return 1

        Walkthrough:
        s = "AABABBA"
        k = 1

        string: A A B A B B A
        index:  0 1 2 3 4 5 6

        Because we are doing brute force, we'll consider substrings stareting at different positions.

        Starting at index 0:

        "A"

        A -> 1

        length = 1
        max frequency = 1
        replacement = 1 -1 = 0

        Valid

        Extend

        "AA"

        length = 2
        max frequency = 2
        replacement = 2 - 2 = 0

        Valid 

        Extend

        "AAB"

        A -> 2
        B -> 1

        length = 3
        max frequencey = 2
        replacement = 3 - 2 = 1

        Valid

        Extend 

        "AABA"

        A -> 3
        B -> 1

        length = 4
        max frequencey = 3
        replacement = 4 - 3. = 1

        Valid 

        Extend

        "AABAB"

        A -> 3
        B -> 2

        length = 5
        max frequencey = 3
        replacement = 5 - 3 = 2

        2 > K : Not Valid

        So, this substring cannot be made all the same with one replacement.

        The brute-force approach will eventually examine other starting positions too.
        
        For example, starting at index 2:

        And say, we built up to this substring: "BABB"

        B -> 3
        A -> 1

        length = 4
        max frequency = 3
        replacement = 4 - 3 = 1

        Valid. So, the longest substring here is 4.

        - - -

        Brute Force Approach
        Intuition:
        - Start a substring at every possible position and keep extending it to the right.
        - As we keep extending the substring, we will count how many character occurs.
        - For every substring, calculate:

        replacement = substring_length - highestt_frequencey

        if replacement needed <= k, then that substring is valid. So, update max_length.

        Algorithm:
        1. Initialize max_length = 0
        2. Loop through every index i as the starting position of a substring
        3. Create an empty frequency dictionary for that starting position
        4. Loop though every index j from i to the end of the substring
        5. Add s[j] to the frequency dictionary
        6. Find the frequency of the most common character in the current substring
        7. Calculate the current substring length using j - i + 1
        8. Calculate the replacements needed using:
            current_length - max_frequencey
        9. If the replacements needed are at most k, update max_length
        10. Continue until all possible substrings have been examined.
        11. Return max_length

        Pseudocode:
        max_length = 0

        for i in range(len(s)):

            frequency = {}

            for j in range(i, len(s)):
                char = s[j]

                if char in frequency:
                    frequency[char] += 1
                else:
                    frequency[char] = 1

                max_frequency = max(frequency.values())

                current_length = j - i - 1

                replacements_needed = current_length - max_frequency

                if replacements_needed ><= k:
                    max_length = max(max_length, current_length)

        return max_length

        Space complexity: O(n^2) because we loop through the characters of the string twice to build substrings
        Time complexity O(20) -> O(1) because the frequncey dictionary can contain at most 26 uppercae English letters        
        """
        max_length = 0

        for i in range(len(s)):

            frequency = {}

            for j in range(i, len(s)):

                char = s[j]

                if char in frequency:
                    frequency[char] += 1
                else:
                    frequency[char] = 1

                max_freq = max(frequency.values())

                current_length = j - i + 1

                replacements_needed = current_length - max_freq

                if replacements_needed <= k:
                    max_length = max(max_length, current_length)

        return max_length
        