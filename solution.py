class Solution(object):
    def trap(self, height):
        l, r = 0, len(height) - 1
        lm = rm = ans = 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= lm:
                    lm = height[l]
                else:
                    ans += lm - height[l]
                l += 1
            else:
                if height[r] >= rm:
                    rm = height[r]
                else:
                    ans += rm - height[r]
                r -= 1
        return ans
