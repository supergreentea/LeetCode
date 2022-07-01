class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        capacity = truckSize
        units = 0
        box_index = 0
        
        while capacity > 0 and box_index < len(boxTypes):
            num_boxes, units_per_box = boxTypes[box_index]
            if num_boxes >= capacity:
                units += units_per_box * capacity
                capacity = 0
            else:
                capacity -= num_boxes
                units += units_per_box * num_boxes
            box_index += 1
        
        return units
                
                