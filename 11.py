class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        maxArea = 0
        
        flipL = 0
        flipR = len(height)-1
        
        indL = 0
        indR = len(height)-1
        
        pushingL = False
        pushingR = False
        
        while(flipR>=flipL):
            if pushingL:
                if height[indL]<height[flipL]:
                    indL = flipL
                    pushingL = False
                    continue
                else:
                    flipL+=1
                    continue
            if pushingR: 
                if height[indR]<height[flipR]:
                    indR = flipR
                    pushingR = False
                    continue
                else:
                    flipR-=1
                    continue
            
            if height[indL]==height[indR]:
                area = (abs(indR-indL))*height[indL]
                pushingL = True
                pushingR = True
                if area>maxArea:
                    maxArea = area
                    
            elif height[indL]<height[indR]:
                area = (abs(indR-indL))*height[indL]
                pushingL = True
                if area>maxArea:
                    maxArea = area
                    
            elif height[indL]>height[indR]:
                area = (abs(indR-indL))*height[indR]
                pushingR = True
                if area>maxArea:
                    maxArea = area
                    
        return maxArea
            
