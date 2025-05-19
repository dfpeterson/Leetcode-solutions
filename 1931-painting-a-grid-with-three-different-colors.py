"""
Level: Hard
Link: https://leetcode.com/problems/painting-a-grid-with-three-different-colors/
Tags: dynamic-programming
Description:
You are given two integers m and n. Consider an m x n grid where each cell is
initially white. You can paint each cell red, green, or blue. All cells must be
painted.

Return the number of ways to color the grid with no two adjacent cells having
the same color. Since the answer can be very large, return it modulo 109 + 7.
"""
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        def get_mask_colors(mask_val, rows):
            colors = [0] *  rows
            temp_mask = mask_val
            for i in range(rows):
                colors[i] = temp_mask % 3
                temp_mask //= 3
            return colors

        def is_internally_valid(mask_colors, num_rows):
            if num_rows == 1:
                return True
            for r in range(num_rows - 1):
                if mask_colors[r] == mask_colors[r-1]:
                    return False
            return True
        
        internally_valid_masks = []
        mask_to_colors_map = {}
        limit = 3**m
        for i in range(limit):
            colors = get_mask_colors(i, m)
            if is_internally_valid(colors, m):
                internally_valid_masks.append(i)
                mask_to_colors_map[i] = colors
        
        def are_masks_compatible(mask1_colors, mask2_colors, rows):
            for r in range(rows):
                if mask1_colors[r] == mask2_colors[r]:
                    return False
            return True

        transitions = {mask: [] for mask in internally_valid_masks}
        for prev_mask in internally_valid_masks:
            prev_colors = mask_to_colors_map[prev_mask]
            for next_mask in internally_valid_masks:
                next_colors = mask_to_colors_map[next_mask]
                if are_masks_compatible(prev_colors, next_colors, m):
                    transitions[prev_mask].append(next_mask)

        dp = {mask: 1 for mask in internally_valid_masks}

        for _ in range(n - 1):
            new_dp = {mask: 0 for mask in internally_valid_masks}
            for prev_mask in internally_valid_masks:
                if dp[prev_mask] == 0:
                    continue
                for next_mask in transitions[prev_mask]:
                    new_dp[next_mask] = (new_dp[next_mask] + dp[prev_mask]) % MOD
            dp = new_dp
        total_combos = sum(dp.values()) % MOD
        return total_combos