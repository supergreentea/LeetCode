class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutes_angle = minutes / 60 * 360
        hours_angle = hour / 12 * 360 + minutes / 60 * 30
        return min(abs(minutes_angle - hours_angle), 360 - abs(minutes_angle - hours_angle))