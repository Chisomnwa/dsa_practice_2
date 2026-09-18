### 347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Input:
        - nums: a list of integers
        - k: an integer (the number of elemnts we need to return)

        Output: Return the k elements that appear most frewuently in nums

        The answer can be in any order, so [1, 2] and [2, 1] are both valid if they contain the correct elements

        Goal: Count how many times each unique number appears, then identify the k elements with the highest frequencies

        Example:
        nums: [1, 1, 1, 2, 2, 3]
        k = 2

        Frequency table
        Number        Frequency
        1               3
        2               2 
        3               1

        Therefore, the two most frequent elements are 1 and 2

        Output: [1, 2]
        
        Edge Cases:
        1. When nums has only one element
            e.g nums = [1], k = 1

            return [1]

        2. When k equals the number of unique elements
            e.g nums = [1, 2, 2, 3, 3, 3], k = 3

            return [1, 2, 3]

        3. When there are many duplicates of one element
            e.g nums = [5, 5, 5, 5, 2, 3], k = 1

            return = [5]

        4. When several elements have the same frequency
            e.g nums = [1, 1, 2, 2, 3, 3], k = 2

            return [3, 2]
            since the problem says any order and doesn't specify any tie breakng rule, any two of them are valid

        5. When we have negative numbers
            e.g nums = [-1, -1, -2, -2, -3, -3, -3], k = 2

            return [-1, -2]
            so, our solution needs to recognize and handle negative numbers

        Walkthrough:
        nums = [1, 1, 1, 2, 2, 3], k = 2

        Step 1: Count the frequencies

        We can use a dictionary to count how often each number appears

        nums = [1, 1, 1, 2, 2, 3]
                0  1  2  3  4  5
                ↑

        count = 
        {
            1: 3,
            2: 2,
            3: 1
        }

        Step 2: Find the most frequent elements

        We now need the top k = 2 elements

        One straightforward idea is to sort the unique numbers by their frequencies

        We want the frequencey order to be:
        1 -> 3 occurrences
        2 -> 2 occurrences
        3 -> 1 occurrence

        Then we select the top 2:
        [1, 2]

        - - -

        Brute Force Approach (Using a Dictionary and Sorting)

        Count the frequency of every number, sort the numbers by their 
        frequencies from highest to lowest, and return the first k numbers.

        Algorithm:
        1. Create an empty dictionary called count
        2. Iterate through nums and count the occurrences of each number
        3. Convert the dictionary keys into a list of unique numbers
        4. Sort the unique numbers according to their frequencies from highest to lowest
        5. Return the first k numbers from the sorted list

        Pseudocode:
        Create an empty dictionary count

        For each numbers in nums:
            if the number is already in count:
                increase its frequencey by 1
            otherwise:
                set its frequencey to 1

        Create a list of all unique numbers

        Sort the unique numbers by their ferquency in descending order

        Return the first k numbers

        Time complexity: O(n) + O(n) + O( m log m) + O(n) = O(m log m)
        Space complexity = O(n) + O(n) + O(n) = O(n)

        - - -

        Optimized Approach (Using Bucket Sort)

        The trick is to realize something important: An element can appear at most len(nums) times.

        So instead of sorting elements by frequency, we can create buckets where the index represents the frequencey.

        For example: nums = [1, 1, 1, 2, 2, 3]


        Now we create buckets:
        frequncy
        0   1   2   3   4   5   6

        bucket[1] = [3]
        bucket[2] = [2]
        bucket[3] = [1]

        So, conceptually:
        buckets = 
        [
            [],   # frequency 0
            [1],  # frequency 1
            [2],  # frequency 2
            [3],  # frequency 3
            [],
            [],
            [] 
        ]

        Now, we simply walk backwards from the highest frequency to the lowest,
        collecting elements until we have k elements..

        Why is this optimized?
        A straighforward approach would be:
        1. Count frequencies -> O(n)
        2. Sort the elements based on frequency -> O(n log n)
        3. Take the first k

        The sorting step is the expensive part.

        We know the possible frequencies range from: 0 -> len(nums)

        So we can simply directly place each number into its frequency bucket.

        Walkthrough:

        nums = [1, 1, 1, 2, 2, 3]
        k = 2

        Step 1: Count frequencies using a hash map.
        frequency = 
        {
            1: 3,
            2: 2
            3: 1
        }

        Step 2: Create the buckets
        There are 6 numbers, so the maximum possible frequency is 6

        buckets = [[] for _ in range(len(nums) + 1)]

        This gives us something like this:

        Index:    0   1   2   3   4   5   6
                  ↓   ↓   ↓   ↓   ↓   ↓   ↓
        Bucket:   []  []  []  []  []  []  []

        Step 3: Put each number into its frequency bucket
        For 1: frequency[1] = 3 -> bucket[3] = [1]
        For 2: frequency[2] = 2 -> bucket[2] = [2]
        For 3: frequency[3] = 1 -> bucket[1] = [3]

        So, we'll now have:

        Index:    0   1   2   3   4   5   6
                  ↓   ↓   ↓   ↓   ↓   ↓   ↓
        Bucket:   []  [3] [2] [1] []  []  []

        Step 4: Walk backwards to collect the top k elements
        k = 2

        Starting with highest posiible frequency:
        index 6: Nothing there
        Index 5: Nothing there
        Index 4: Nothing there
        Index 3: 1
        Index 2: 2

        Then we stop.

        result = [1, 2]

        Algorithm:
        1. Create a frequency map to store each number and how many times it appears in nums
        2. Go through nums and count the frequency of every number
        3. Create a list of buckets where each bucket represents a possible frequency
            - The index of the bucket represents a frequency
            - For example bucket[3] represents numbers that appear 3 times
        4. Go through the frequencuy map and place each number into the bucket corresponding to the frequency
        5. Create an empty result list to store the top k frequent elemets
        6. Start from the bucket with the highest frequency and move to the bucket with the lowest frequency
        7. For each number in the current bucket, add it to the result list
        8. Check if the results contain k elements

        Pseudocode:
        create a frequency map

        for each num in nums:
            if num in map:
                increase its frequency
            otherwise:
                create a new item and set its frequency to 1

        create buckets from frequency 0 to len(nums)

        for each number in frequency:
            put the number into bucket[frequency]

        create an empty result

        for frequency from highest to lowest:
            for each number in that bucket:
                add number to result

                if result contains k elements:
                    return result

        Time complexity:
        Space complexity:
        """
        # Brute Force Approach (Sorting)
        count = {}

        # Count the frequency of each number
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        # Get all unique numbers
        unique_nums = []

        for num in count:
            unique_nums.append(num)

        # Sort by frequency, highest first
        unique_nums.sort(key=lambda num: count[num], reverse=True)

        # Return the k most frequent numbers
        result = []

        for i in range(k):
            result.append(unique_nums[i])

        return result


    
        ########################

        # Optimized Aproach (Bucket Sort)
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        buckets = [[] for _ in range(len(nums) + 1)]

        for num in count:
            freq = count[num]
            buckets[freq].append(num)

        result = []

        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result
