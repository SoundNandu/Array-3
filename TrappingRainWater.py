Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

#Approach is that, we are calculating the maximum value of the left,and maximum value 
# of the right index.In order to find the rainwater filled we are taking the min(leftmax,rightmx) and subtract it with height.

#Time : O(n) | Space:O(n)

class Solution:
    def trap(self, height: List[int]) -> int:
        #edge Case
        if height == None or len(height) == 0:
            return 0
        # Initial values defined
        n=len(height)
        leftMax = [0]*n
        rightMax = [0]*n
        leftMax[0]=0
        rightMax[n-1]
        # Finding the leftMax
        for i in range(1,n):
            leftMax[i] = max(leftMax[i-1],height[i-1])
        # Finding the RightMax
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i+1],height[i+1])
        # need to keep on adding in the totalWater
        totalWater = 0
        for i in range(n):
            #calculate the currentWater
            currentWater = min(leftMax[i],rightMax[i]) - height[i]
            #if the currentWater is negative it means no water is filled
            # Assign currentWater = 0 in that case else add the currentWater to totalWater 
            # and keep on adding totalWater to sum 
            if currentWater < 0:
                currentWater = 0
            totalWater += currentWater
        #return the sum 
        return totalWater
