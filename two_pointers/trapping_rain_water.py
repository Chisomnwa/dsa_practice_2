class Solution:
    def trap(self, height: list[int]) -> int:
        """
        Input: height - an array of integers
            - e.g height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
            - Each number represents the height of a bar, and every bar has wiidth 1
            - After rain falls, some water gets trapped between taller bars
        
        Output: to return the total un its of trapped water

        Goal:
            - To calculate how much water is sitting directly above each individual position.
            - Then, we add those together

        Consider:
        height = [4, 2, 0, 3, 2, 5]
                  0  1  2  3  4  5

        Look at index 2:
        height[2] = 0

        There's a tall wall somwhere on its left: 4
        There's also a tall wall somwhere on its right: 5

        So, water can sit above this position

        How much water can one position hold?

        For any index i, we need to know:
        - tallest bar to the left
        - tallest bar to the right

        The water level is controlled  by the shorter of those two boundaries:
        water_level = min(left_max, right_max)

        The, we subtract the height of the current bar:
        water_at_i = min(left_max, right_max) - height[i]

        Example:
        height = [4, 2, 0, 3, 2, 5]

        at index 2: 0

        left_max = 4
        right_max = 5
        water_at_i = min(4, 5) - 0 = 4 units of water

        at index 3: 3

        left_max = 4
        right_max = 5
        water_at_i = min(4, 5) - 3 = 1 unit of water

        If we calculate every position:
        index:   0 1 2 3 4 5
        height:  4 2 0 3 2 5
        water:   0 2 4 2 2 0

        Why min(left_max, right_max)?
        Some basic reason as container with most water: the shorter boundary determines the water level
        if:
        lef_max = 4
        right_max = 7

        water_level = min(4, 7) = 4

        Edge cases:
        1. when we have no walls capable of trapping water
            e.g [1, 2, 3, 4]
            - Everything increases, so water simply runs off
            answer = 0

            e.g [4, 3, 2, 1]
            - everything decreases, so water simply runs off too
            answer = 0

        2. When we have flat bars
            e.g [3, 3, 3]
            - There's no where for water to sit above the bars
            answer = 0

        3. When we have valley between walls
            e.g [3, 0, 3]
            - At the missle: min(3, 3) - 0 = 3
            answer = 3

        4. When we have one bar
            e.g [5]
            - One bar cannot trap water
            answer = 0

        - - -

        Brute Force Approach
        The straightforward idea is: 
        - For every position, search to its left for the tallest bar and search to its right for the tallest bar
        - Then calculate: water = min(left_max, right_max) - height[i]
        - Then add that to our total

        Algorithm:
        1. Initialize total_water to 0
        2. Loop through every index i
        3. Find the tallest bar from index 0 through i
        4. Find the tallest bar from i through the end of the array
        5. Take the smaller of those two maximum heights
        6. Subtract height[i] to determine how much water is above the current bar
        7. Add that amount to total water
        8. After checking every position, return total_water

        Pseudocode:
        total_water = 0

        for each index i:
            max_left = 0

            for j in range(i + 1):
                max_left = max(max_left, height[j])

            max_right = 0

            for j in range(i, len(height)):
                max_right = max(max_right, height[j])

            water = min(max_left, max_right) - height[i]

            total_water += water

        return total_water       
        
        Time complexity: O(n^2) because for each position, we are potentially scanning through the array to find the maximum on its left and right.

        Space complexity: O(1) because we only used a few variable, and no extra data struture
        
        - - -
        
        Optimized Approach (Two Pointers):
        The problem with brute force is that for every position, we search the left, and right sides again.
        Instead, we keep track of the maximum heights we've already been seeing using:

        Intuition:
        Water at any position depends on the shorter wall between the left and the right side.
        So if the left wall is shorter, the right wall can;t help us because water is limited by the right side.
        That means we safely move the left pointer inward and calculate how much water can be trappe dthere.
        Similary, if the right wall is shorter, we move the right pointer left.

        As we move the pointers, we keep track of the highest wall sen so far on each side (leftMax and rightMax)

        The water at each position is simply:

        max wall on that side - height of that position

        Algorithm
        1. Set two pointers
            - left at the start
            - right at the end
                Track left_max and right_max as the tallest walls seen.

        2. While left < right:
            - if left_max < right_max
                - Move lett right
                - Update left_max
                - Add left_max - height[i] to the result
            - else
                - Move right left
                - Update right_max
                - Add right_max - height[i] to the result

        3. Return the total trapped water

        Time complexity: O(n) because we loop through each elemnt n times
        Space complexity: O(1) because no extra data structure was created.
        """
        # # Brute force Approach (Basic Traversal and Nested loops)
        # total_water = 0

        # for i in range(len(height)):

        #     max_left = 0

        #     for j in range(i + 1):
        #         max_left = max(max_left, height[j])

        #     max_right = 0

        #     for j in range(i, len(height)):
        #         max_right = max(max_right, height[j])

        #     water = min(max_left, max_right) - height[i]

        #     total_water += water

        # return total_water

        # Optimized Approach(Two pointers)
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        result = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                result += left_max - height[left]

            else:
                right -= 1
                right_max = max(right_max, height[right])
                result += right_max - height[right]

        return result
