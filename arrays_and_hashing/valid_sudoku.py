class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        Input: a 9 * 9 sudoku board

        board = [
            ["5","3",".",".","7",".",".",".","."]
            ["6",".",".","1","9","5",".",".","."]
            ...
        ]

        A "." means the cell is empty, so we ignore it.

        Output: Return
        - True if the cells follow all three sudoku rules
        - Fasle otherwise 

        Goal: For every filled cell, make sure its number does not already appear in:
        1. Its row
        2. Its column
        3. Its 3 * 3 box

        For example this cell:
                0  1  2
            0   5  3  .
            1   6  .  .
            2   .  9  8

        The 5 at (0, 0) must not appear anywhere else in:
        - row 0
        - column 0
        - top-left 3 * 3 box

        Edge cases 1: Empty Cases
        1. When we encounter empty cells; "."
            - We simply skip them because only filled cells need validation
        
        2. When we have duplicate in the same row
            e.g ["5","3",".",".","7",".",".","3","."]
            - There are two 3s in the same row -> return False

        3. Whe we have duplicate in the same column
            e.g 5
                .
                .
                5
                .
                .
                .
                .
                .
            - We have two 5s in the same column -> we return False

        4. When we have duplicate inside the 3 * 3 box
            - Even if the duplicate isn't in the same row or column, it can still make the board invalid
            e.g
            5  3  .
            6  5  .
            .  9  8
            
            The two 5s are inside the same 3 * 3 box, so we return False

        - - 

        Brute Force Approach (Nested For Loops)
        Intuition: For every cell, check its entire column, and entire 3 8 3 box for another copy of the same number

        For example this cell:
                0  1  2
            0   5  3  .
            1   6  .  .
            2   .  9  8

        If we are looking at board[0][0 = "5", we check:
        - Does 5 exist in another cell in row 0
        - Does 5 exist in another cell in column 0
        - Does 5 exists in the top-left 3 * 3 box?

        If we find one anywhere we return False.
        Otherwise continue to the next cell.

        Algorithm:
        1. We loop through every row r from 0 to 8
        2. For every column c from 0 to 8:
            - if board[r][c] == ".", skip the cell
            - Otherwise, store the current digit
        3. Check the current row for another occurrence of that digit
        4. Check the current column for another occurrence of that digit
        5. Find the 3 * 3 box containing the current cell
        5. If a duplicate is found, return False
        6. If all cells pass, return True

        How do we find the 3 * 3 box?
        This is the important part.

        Suppose:

        suppose r = 4
                c = 7

        0  1   2   3  4  5  6  7  8
        1                  
        2                    _____
        3                   |     |
        4                   |     |
        5                   |_____|
        6
        7
        8

        We calculate:
        box_row = (r // 3) * 3
        box_col = (r // 3) * 3

        For r = 4:
            = (4 // 3) * 3 
            = 1 * 3 = 3

            So, the box starts at row 3

        For column 7:
            = (7 // 3) * 3
            = 2 * 3 = 6

            So, the column starts at column 6

        Therefor the box starts at:
        (row=3, col=6)

        and covers:
        row 3, 4, 5
        column 6, 7, 8

        Pseudocode:
        for each row r:
            for each column c:
                
                if cell is ".":
                    continue

                digit = board[r][c]

                check the entire row
                if duplicate is found:
                    return false

                check the entire column
                if duplicate is found:
                    return False

                find the starting row and column of the 3*3 box

                check the entire 3*3 box
                if duplicate is found:
                    return False

        return True

        Time complexity: O(n^2) because we iterate through each cell in the board 9 * 9 times
        Space complexity: 0(1) because no extra data structure was created

        - - -

        Optimized Approach (Using a Hah Set)
        Key idea: The pattern we use sets to keep track of digits we've seen:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        Think of it as:
        - rows[0] -> digits already seen in row 0
        - cols[0] -> digits already seen in column 0
        - boxes[0] -> digits already seen in the top-left 3*3 box

        So, instead of repeatedly scanning, we simply ask:
        "Have I seen this digit here?"

        How do we identify the 3*3 box?
        The formular is:
        box = (r // 3) * 3 + (c // 3)

        There are 9 boxes, which we can number:

        0 | 1 | 2
        ---------
        3 | 4 | 5
        ---------
        6 | 7 | 8


        For example, if:
        r = 1
        c = 7

        Then, 

        (r // 3) * 3 + (c // 3)   
        = (1 // 3) * 3 + (7 // 3)
        = 0 * 3 + 2
        = 2

        So (1, 7) belongs to box 2

        Algorithm:
        1. Create 9 empty sets to keep track of the digits already seen in each row
        2. Create 9 empty sets to keep track of the digits already seen in each column
        3. Create 9 empty sets to keep track of the digits already seen in each 3*3 box
        4. Go through every cell of the sudoku board
        5. If the cell is empty ("."), skip it and move to the next cell
        6. Store the digit in the current cell
        7. Determine which 3*3 box the current cell belongs to
        8. Check if the digit has already appeared in the current row, column, or 3*3 box
        9. If the digit has alreday appeared in any of them, return False
        10. Otherwise, add the digit to the corresponding row, column, and box sets
        11. After checking every cell without finding a duplicate, return True

        The most important difference from brute force is that we're remembering previous cells, rather than scanning the board again.

        Pseudocode:
        rows = 9 empty sets
        cols = 9 empty sets
        boxes = 9 empty sets

        for r from 0 to 8:
            for c from 0 to 8

                if cell is empty
                    continue

                digit = board[r][c]

                box = (r // 3) * 3 + (c // 3)

                if digit in rows[r]
                    return False
                
                if digit in cols[c]
                    return False

                if digits in boxes[box]
                    return False

                add digit to rows[r]
                add digit to cols[c]
                add digit to boxes[box]

        return True

        Time complexity: O(n^2) because we visit each of the n^2 cells once, and each cell does only O(1) set operations.
        
        Space complexity: O(n^2) because we store up to n digits across n row/column/box sets, giving O(n^2) extra

        i.e for a generalized n * n board:
        - n row sets * up to n digits = O(n^2)
        - n column sets * up to n digits = O(n^2)
        - n box sets * up to n digits = O(n^2)

        So, overall: O(n^2) extra space

        - - -
        Use cases for each approach:
        - Brute Force: useful when you are first developing the solution, want the simplest conceptual approach, or the input is so small that the extra work doesn't matter.
        - Optimized: useful when the board/input can become much larger, because it avoids repeatedly scanning the same information
        
        """
        # # Brute Force Approach
        # for r in range(9):
        #     for c in range(9):

        #         # Skip empty cells
        #         if board[r][c] == ".":
        #             continue

        #         digit = board[r][c]

        #         # Check the row
        #         for col in range(9):
        #             if col != c and board[r][col] == digit:
        #                 return False

        #         # Check the column
        #         for row in range(9):
        #             if row != r and board[row][c] == digit:
        #                 return False

        #         # Find the starting position of the 3*3 box
        #         box_row = (r // 3) * 3
        #         box_col = (c // 3) * 3

        #         # Check the 3*3 box
        #         for row in range(box_row, box_row + 3):
        #             for col in range(box_col, box_col + 3):
        #                 if (row != r or col != c) and board[row][col] == digit:
        #                     return False

        # return True

        # Optimized Approach
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                # Skip empty cells
                if board[r][c] == ".":
                    continue

                digit = board[r][c]

                # Calculate the box where the curent cell is located
                box = (r // 3) * 3 + (c // 3)

                # Check the row
                if digit in rows[r]:
                    return False

                # Check the column
                if digit in cols[c]:
                    return False

                # Check the box
                if digit in boxes[box]:
                    return False

                # Add them to the current row, column, and box
                rows[r].add(digit)
                cols[c].add(digit)
                boxes[box].add(digit)
        
        return True
