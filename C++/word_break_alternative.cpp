class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {                      // This program can find solution on some problems
        string temp = "";                                                    // But with Input s="goalspecial" wordDict = ["go","goal","goals","special"]
        string substring = s;                                               // We can't finish because we find "go" first and we remove it from temp,
        int counter = 0;                                                   // So we cant find a solution with the remaining, but still theres a solution.
                                                                          // But this algorithm could be usefull so I posted it.
        for(int i = 0; i<s.size(); i++)
        {
            temp += s[i];
            for(int j = 0; j<wordDict.size(); j++)
            {
                if(wordDict[j] == temp)
                {
                    for(int k = 0; k<wordDict.size(); k++)
                    {
                        if(wordDict[j]+wordDict[k] == substring)
                        {
                            return true;
                        }
                    }
                    substring.erase(0, temp.length());
                    temp = "";
                    counter ++;
                }
            }
        }
        if(substring == "")
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};
