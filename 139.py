class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = []
        for i in range(len(s)):
            dp.append(False)
            
        for i in range (len(s)):
            string = s[0:i+1]
            for word in wordDict:
                if word == string:
                    dp[i] = (True)
                    
                if len(word) < len(string):
                    if (string[len(string)-len(word):len(string)] == word) and (dp[len(string)-len(word)-1] == True):
                        dp[i] = (True)
                        
        return dp[len(s)-1]
