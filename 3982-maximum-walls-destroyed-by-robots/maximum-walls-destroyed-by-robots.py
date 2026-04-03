from bisect import bisect_left, bisect_right

class Solution:
    def maxWalls(self, robots, distance, walls):
        robots = sorted(zip(robots, distance))
        walls.sort()
        
        n = len(robots)
        left = [0] * n
        right = [0] * n
        num = [0] * n
        
        for i in range(n):
            pos, dist = robots[i]
            
            pos1 = bisect_right(walls, pos)
            
            if i >= 1:
                left_bound = max(pos - dist, robots[i - 1][0] + 1)
                left_pos = bisect_left(walls, left_bound)
            else:
                left_pos = bisect_left(walls, pos - dist)
            
            left[i] = pos1 - left_pos
            
            if i < n - 1:
                right_bound = min(pos + dist, robots[i + 1][0] - 1)
                right_pos = bisect_right(walls, right_bound)
            else:
                right_pos = bisect_right(walls, pos + dist)
            
            pos2 = bisect_left(walls, pos)
            right[i] = right_pos - pos2
            
            if i == 0:
                continue
            
            pos3 = bisect_left(walls, robots[i - 1][0])
            num[i] = pos1 - pos3
        
        sub_left, sub_right = left[0], right[0]
        
        for i in range(1, n):
            current_left = max(
                sub_left + left[i],
                sub_right - right[i - 1] + min(left[i] + right[i - 1], num[i]),
            )
            current_right = max(sub_left + right[i], sub_right + right[i])
            
            sub_left, sub_right = current_left, current_right
        
        return max(sub_left, sub_right)