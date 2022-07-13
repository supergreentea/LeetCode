class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        
        count = defaultdict(int)
        
        min_x = min_y = math.inf
        max_x = max_y = -math.inf
        
        area = 0
        
        for x_start, y_start, x_end, y_end in rectangles:
            
            # Update min and max x and y values.
            min_x, min_y, max_x, max_y = min(x_start, min_x), min(y_start, min_y), max(x_end, max_x), max(y_end, max_y)
            start_point, end_point = (x_start, y_start), (x_end, y_end)
            top_left_corner, bottom_right_corner = (x_start, y_end), (x_end, y_start)
            
            area += (y_end - y_start) * (x_end - x_start)
            
            count[start_point] += 1
            count[end_point] += 1
            count[top_left_corner] += 1
            count[bottom_right_corner] += 1
            
        corners = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]
        
        if area != (max_y - min_y) * (max_x - min_x):
            return False
        
        for point in count:
            if point in corners:
                if count[point] != 1:
                    return False
            else:
                if count[point] % 2 == 1:
                    return False

        return True