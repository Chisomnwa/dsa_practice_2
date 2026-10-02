class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Input: a string
        - Can include printable ASCII characters like letters, digits, symbols and spaces

        e.g s = "abcabcbb"

        Output: To return the length of the longest substring without repeating characters

        Goal: Loop through the string and print out the length of the longest substring without any duplicate characters

        What is a substring? A substring must be continous in the original string

        E.g s = "pwwew"

        "wke" is a substring

        But "pwke" is not a substring because we are skipping characters

        That's s ubsequence, not a substring.

        Edge cases:
        1. When the string is empty ->. return 0
            - Because there is no substring to build
            - e.g ""

        2. When the string contsins one character -> return 1
            - e.g s = "b"

        3. When all characters are identical -> return 1
            - e.g s = "bbbb"

        4. When there are no duplicates -> return the length of the string
            - e.g s = "abcd"
            - return 4

        2. When strings contain digits, symbols or sopaces -> include them in the substrings
            - e.g s = "hel123❤️ol"
            - return "hel123❤️o"

        Walkthrough:
         s = "abcabcbb"

        Some valid substrings are:
        "a"
        "ab"
        "abc" -> length 3
        "bca" -> length 3
        "cab" -> length 3

        So, output = 3

        - - -

        Brute force Solution (Nested Loop and Set)
        The simplest idea is: start at every character and build a substring until you encounter a duplicate

        For example:

        s = "a b c a b c b b"
             0 1 2 3 4 5 6 7

        Starting at index 0:
        "a" - valid
        "ab" - valid
        "abc" - valid
        "abca" ❌

        So, from index 0, our longest substring has a length of 3

        Move to index 1:
        "b" - valid
        "bc" - valid
        "bca" - valid
        "bcab" ❌

        From index 1, our longest substring is 3

        Move to index 2:
        "c" - valid
        "ca" - valid
        "cab" - valid
        "cabc" ❌

        From index 2, our longest sbstring is 3

        We repeat this for every starting position

        Algorithm:
        1. Initialize max_length to 0
        2. Loop through every index i as the starting point of a substring
        3. Create an empty set called seen to remember characters already in a substring
        4. Starting from index i, loop forward using j
        5. if s[j] is already in seen, stop extending this substring
        6. Otherwise, add s[j] to seen
        7. Calculate the current substring length
        8. Update max_length if this substring is longer
        9. Repeat from the next starting position
        10. Return amx_length

        Pseudocode:
        max_length = 0

        for i, from 0 to len(s) - 1

            seen = set()

            for j, from i + 1 to len(s) - 1
                if s[j] in seen
                    break
                
                seen.add(s[j])

                ccurrent_length = j - i + 1

                max_length = max(max_length, current_length

        return max_length

        How the formular works:
        current_length = j - i + 1

        e.g 

        s = a b c
            0 1 2
            ↑   ↑
            i   j

        current_length = 2 - 0 + 1 = 3

        Time complexity: 0(n^2) because for every syarting position i, we may scan the string forward using j
        Space complexity: O(n) because of the seen set, which could contain every character in the string if they are all unique

        - - -

        Optimized Approach (Sliding Window and Set)
        In brute force, whenever we encounter a duplicate, we:

        break -> throaway the current substring -> start again

        That's wasteful. Instead, we maintain a window containing only unique characters

        Example:

        s = "a b c a b c b b"
             ↑ ↑
             L R

        We use:
        - left: as the beginnning of our current ubstring/window
        - right: to explore new characters
        - seen: to store characters currently inside our window

        When s[rigght] is new, we add it and expand the window

        When s[right] is already in seen, we move left forward and remove characters until the duplicate is gone

        Then, we continue expanding instead of starting over

        Walkthrough:
        s = "a b c a b c b b"
             0 1 2 3 4 5 6 7

        left = 0
        seen = {}
        max_length = 0

        right = 0

        a b c a b c b b"
        ↑
        L/R

        'a' is not in seen
        seen = {a}
        length = 0 - 0 + 1
        max_lenght = 1

        right = 1

        "a b c a b c b b"
        ↑ ↑
        L R

        'b' is not in seen
        seen = {a, b}
        length = 1 - 0 + 1 = 2
        max_length = 2

        right = 2

        "a b c a b c b b"
         ↑   ↑
         L   R

        'c' is not in seen
        seen = {a, b, c}
        length = 2 - 0 + 1 = 3
        max_length = 3

        "a b c a b c b b"
         ↑     ↑
         L     R

         'a' is already in seen
         Our window will become "abca" which is invalid

         So, see.remove(s[left]) removes the first 'a'

         seen becomes = {b, c}

         Then, we shift left forward

         left += 1

        "a b c a b c b b"
           ↑   ↑
           L   R

        So, the new 'a' is no longer duplicated, so we add it:

        seen = {a, b, c}

        window = "bca"
        length = 3
        max_length = 3

        And we continue the same process.

        Algorithm:
        1. Create an empty seen set
        2. Initiate the left pointer to 0
        3. Initiate the max_length to 0
        4. Using the right pointer, loop through each character in the string
        5. If the character at s[right] is already in seen, remove s[left] from seen and move left forward
        6. Keep doing this while s[right] is still a duplicate
        7. Otherwise add it to seen
        8. Calculate the length of the substring/window using right - left + 1
        9. Update max_length
        10. Return max length

        Pseudocode:
        seen = set()
        left = 0
        max_length = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            current_length = right - left + 1

            max_length = max(max_length, current_length)

        return max_length

        Time complexity: O(n) because
            - left only moves forward through the string once
            - right also only moves forward through the string once
            - Neither pointer ever moves backward
            - Across the entire algorithm, each character is added and removed from the set at most once

        Space complexity: O(n) because the set can contain up to n unique characters

        """
        # # Brute force Approach (Nested Loops and Set)
        # max_length = 0

        # for i in range(len(s)):

        #     seen = set()

        #     for j in range(i, len(s)):

        #         if s[j] in seen:
        #             break
                
        #         seen.add(s[j])

        #         current_length = j - i + 1

        #         max_length = max(max_length, current_length)

        # return max_length


        # Optimized Approach (Two Pointers and a Set)
        seen = set()
        left = 0
        max_length = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            current_length = right - left + 1

            max_length = max(max_length, current_length)

        return max_length
