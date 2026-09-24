class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Input: 
            - a list of lowercase strings made up of 26 English caharacters
            - can contain empty strings

        Output:
            - a list of groups
            - Each group contains strings that are anagrams of each other

        Goal: Group together all strings that are anagrams

        Example:

        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

        [
            ["eat", "tea", "ate"],
            ["tan", "nat"],
            ["bat"]
        ]

        Edge cases:
        1. When we have an empty string -> return an empty string
            input: [""]
            Output: [[""]]

        2. When we have just one string -> return a one string
            Input: ["a"]
            Output: [["a"]]

        3. When we have duplicate anagrams -> duplicate anagrams should stay in the same anagram group
            Input: ["eat", "tea", "ate"]
            Output: [["eat", "tea", "ate"]]

        4. When all strings are already anagrams -> they all belong to the same group
            Input: ["eat", "tea", "ate"]
            Output: [["eat", "tea", "ate"]]

        5. When no strings are anagrasm -> each string forms its own group
            Input: ["cat", "dog", "pen"]
            Output:[["cat"], ["dog"], ["pen"]]

        Walkthrough:
        Input: ["eat", "tea", "tan", "ate", "nat", "bat"]

        Notice:
        - eat, tea, ate, all become aet when sorted
        - tan, nat all become ant when sorted
        - bat becomes abt when sorted

        idea: Use the sorted string as the dictionary key

        Dictionary becomes:

        {
            "aet": ["eat", "tea", "ate"],
            "ant": ["tan", "nat"],
            "abt": ["bat"]
        }

        Return:
        [
            ["eat", tea", "ate"],
            ["tan", "nat"]
            ["bat"]
        ]
        
        - - -

        Brute Force Approach

        Intuition:
        - Compare each word with every other word
        - If two words are anagrams:
            - Puth them in the same group
            - Mark the second word as already grouped so you don't process it again.

        - To check whether two words are anagrams
            - Sort both words
            - Compare sorted strings

        Algorithm
        1. Create an empty list called result to store all groups of Anagrams
        2. Create an empty set called visited to keep track of strings that already been placed in a group.
        3. Iterate through index i in strs
        4. If index i in already in visited, skip it
        5. Othersise, create a new group containing strs[i] and mark index i as visited
        6. Iterate through remaining indexes j after i
        7. If index j is already in visited, skip it
        8. Sort the characters of strs[i] and strs[j]
        9. If the sorted strings are equal they are anagrams
            - Add strs[j] to the current group
            - Mark index j as visited
        10. After checking all remaining strings, add the current group to the result list
        11. Return the result list


        Pseudocode:
        Create an empty result list

        Create an empty visited set

        For each index i:

            if i has already been visited:
                continue

            Create a new group containing strs[i]

            Mark i as visited

            For each j after i:
                if j has not been visited:
                    if sorted(strs[i]) == sorted(strs[j]):
                        Add strs[j] to the group

                        Mark j as visited

            Add the group to result

        Return result

        Time complexity: O(n^2 . n log n ). Why?
            - Outer loop : O(n)
            - Inner loop: O(n)
            - Every comparism sorts two strings

        Space complexity: O(n) Why?
            - visited can srtore up to n indices
            - result stores the grouped strings (the output itself is typically not counted as
            extra space in interviews, but the auxilliary set is O(n))

        - - -

        Optmized approach (Using a hash Map)

        Key insight: Every anagram has the same sorted version

        Exaple:
        "eat" -> aet
        "tea" -> aet
        "ate" -> aet

        so, we use the sorted word as the dictionary key

        Algorithm:
        1. Create an empty dictionary called groups
        2. Iterate through each word in the string
        3. Create a shared key using the sorted version of the word
        4. If key is not in the groups
            - Add it as an element of the group dictionary using groups[key] = []
        5. Append the word to that list for that group
        6. At the end of the iteration, return the values of the group, and converting them to a list

        Pseudocode:
        Create an empty groups dictionary

        For each word in strs:
            key = sort the word

            If key not in dictionary:
                create it as an element of the dictionary with empty list as its value

                Append word to that list

        Return all dictionary values

        Space and Time complexity:
        Let:
        - n = number of words in strs
        - k = maximum length of each word
        
        Time complexity: O(n * k log k). For each word:
        1. sorted(word) takes O(k log k) time because we sort its characters.
        2. "".join(...) takes O(k) time to combine the characters.
        3. Dictionary lookup and appending take O(1) average time

        Therefore: O(n * (k log k + k)) = O(nk log k)

        Space complexity: O(n * k)
        We store:
        - The sorted strings used as dictionary keys
        - The original words inside the grouped lists
        - The temporary sorted character for each word

        If there are n words, each of length at most k, the stored 
        input characters and keys can require O(nk) space.

        In summary: The time complexity is O(nk log k) because we sort each of the n words,
        and each word has at most k characters. The space complexity is O(nk) because we
        store the original words and their sorted keys in the hash map.

        """
        # # Brute Force Approach (Using Nested For loops for comparison)
        # result = []

        # visited = set()

        # for i in range(len(strs)):
        #     if strs[i] in visited:
        #         continue

        #     group = [strs[i]]

        #     visited.add(strs[i])

        #     for j in range(i + 1, len(strs)):
        #         if strs[j] not in visited:

        #             if sorted(strs[i]) == sorted(strs[j]):
        #                 group.append(strs[j])
        #                 visited.add(strs[j])

        #     result.append(group)

        # return result

        # Optimized Approach (Using a Has Map)
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
