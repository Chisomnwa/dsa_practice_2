class Solution:
    def maxArea(self, height: list[int]) -> int:
        """
        Inpu: height - an array of integers
            - Each number represents the height of a vertical line
            - The index tells us where the line is positioned horizontally

            height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
            index:    0  1  2  3  4  5  6  7  8

        Output: to retun an integer, whihc is the maximum area that contains the most water.

        How do we calculate the water?
        This is the most important part to understand.

        The container's area = width * height

        Width:
        Width is the distace between the two indexes:
        width = right - left

        Choose indexes 1 and 8

        [1, 8, 6, 2, 5, 4, 8, 3, 7]
        0  1  2  3  4  5  6  7  8
            ↑                    ↑
        left               right

        Therefore width = 8 - 1 = 7

        Height:
        Height is the minimum between the two vertical lines because we can only go as high as the shorter line

        Our two lines above have heights:
        height[1] = 8
        height[8] = 7

        So, height = min(8, 7) = 7

        Why the shorter line you might ask?

        8|     
            |------|7
            |      |
            |------|

        - Even though the left wall has only height 8, the right wall onlly has height 7
        - if the water rises above 7, it spills over the right side
        - Therefore, the shorter wall determines how high the water can go

        Therefore:
        area = width * height
        area = 7 * 7 = 49

        Goal: find two vertical lines such that together with the x-axis form a container that contains the maximum amount of water.

        Edge Cases:
        1. if we have only two line
            - There is only one possible container
            - e.g height = [1, 1]
            area = width * height
            areaa = 1 * 1 = 1

        2. A line can have a height of 0
            - e.g height = [0, 5]
            area = width * height
            area = 1 * 0 = 0

        NB: The tallest two lines aren't necessarily the answer. Distance matters too.

        For example, a slightly shorter pair that is much farther apart can hold more water. 
        So, we can't simply find the two largest heights.

        - - -
        Brute Force Approach
        The straightforward way of solving this is trying every possible pair of lines, calculating how much water that pair hold and remembering te largest area.

        For example:
        height = [1, 8, 6, 2]
                0  1  2  3

        We'll try:

        index 0 and 1
        index 0 and 2
        index 0 and 3

        index 1 and 2
        index 1 and 3

        index 2 and 3

        width = j - i
        container_height = min(height[j], height[i])
        area = width * height

        Then, we'll alwayk keep thelargest area

        Algorithm:
        1. Initialize an empty max_area integer to 0
        2. Loop through the array using index i, starting from 0
        3. Loop through the array using index j, startig from index i + 1
        4. Calulate the width
        5. Calclate the height
        6. Multiply the width and the heigt to find the area of the container
        7. Keep the maximum result area

        Pseudocode:
        max_area = 0

        for i, from 0 to len of height - 1
            for j, from i + 1 to len of height - 1

                calculate the width
                calculate the heigh
                area = width * height

            max_area  = max(max_area , area)
        
        return max_area 

        Time complexity: O(n^2) because we loop through the elemnets of height array twicw
        Space complexity: O(1) because no extra data structure was created

        - - -

        Optimized Approach(Two pointers)
        - Brute frce approach is inefficient because it checks every possible pair
        - But because the area depends on both the width and the shorter height, we can intelligent eliminate pairs using two pointers
        - We will star with the two lines that are farthest apart

        [1, 8, 6, 2, 5, 4, 8, 3, 7]
         0  1  2  3  4  5  6  7  8
         ↑                       ↑
         left                 right

        This gives us the maximum possible width, then we calculate:
        width = rigt - left
        container_height = min(height[lef], height[right])
        area = width * cntainer_height

        Then comes the key question: Which pointer should we move?

        We always move the pointer pointing o a shorter line, because the shorter line limits how much pointer we can hold.

        e.g if:
        left height = 1
        right heigh = 7

        Our container_height = min(1, 7) = 1

        Moving the 7 inward makes our width smaller while 1 still limits our height

        Instead, move away from the 1 and hope to find a taller one.

        Walkthrough:

        [1, 8, 6, 2, 5, 4, 8, 3, 7]
         0  1  2  3  4  5  6  7  8
            ↑                    ↑
           left                 right

        left = 0 -> height 1
        right = 8 -> height 7

        width = 8 - 0 = 8
        height = min(1, 7) = 1

        area = 8 * 1 = 8

        max_area = 8

        1 is shorter, so move left

        left = 1 -> height 8
        right = 8 -> height 7

        width = 8 - 1 = 7
        height = min(8, 7) = 7

        area = 7 * 7 = 8

        max_area = 49

        Now, seven is shoter, move the right poniter..

        So, we keep doing this until left >= right.

        Algorithm:
        1. Initiate an empty max_area  to 0
        2. initilaze the left pointer: left = 0
        3. initialize right pointer: right = len(height) - 1
        4. While left is less athan right
            - Calculate the width
            - Calculate the height
            - Calculate the area
            - Keep the maximum area
            - If the left vertical line is shorter than the right vertical line
                - move the left ponter inwards
                - otherwise, move the right pointer backwards
        5. Continueuntil the two pointers meet
        6. Return the maximum area

        Pseudocode:
        max_area = 0

        left = 0
        right = len(height) - 1

        for i, from 0 to len(height) - 1
            calculate the width
            calculate the height
            calculate the area

            keep the maximum area

            if left pointer is pointing the the shorter hright
                move left pointer inwards
            else:
                move right pointer backwards

        return max_area

        Time complexity: O(n) because each pointer moves inwards at most n times
        Space complexity: O(1) becaus we used only a few variables

        """
        # # Brute Force Approach(Basic Array Traversal and Nested loops)
        # max_area = 0

        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):

        #         width = j - i
        #         container_height = min(height[j], height[i])

        #         area = width * container_height

        #         max_area = max(max_area, area)

        # return max_area


        # Optimized approach
        max_area = 0

        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            container_height = min(height[left], height[right])

            area = width * container_height

            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
