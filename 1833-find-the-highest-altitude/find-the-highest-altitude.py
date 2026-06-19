class Solution:
    def largestAltitude(self, gain):
        n = len(gain)
        maximum = 0
        for i in range(n + 1):
            altitude = 0
            for j in range(i):
                altitude += gain[j]
            maximum = max(maximum, altitude)
        return maximum