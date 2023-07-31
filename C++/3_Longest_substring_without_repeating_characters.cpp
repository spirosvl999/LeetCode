class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        set<char>Set;                                   // We will use this to find the current element
        int max = 0;
        int start = 0; int end = 0;                     //We will use 2 pointers to find the max(aka. the longest substring)

        while(start<s.size())
        {
            auto it = Set.find(s[start]);
            if(it==Set.end())
            {
                if(start-end+1>max)                     // We do +1 because start&end valued at 0
                {
                    max=start-end+1;                    // We change the max value only if we find a longer substring
                }
                Set.insert(s[start]);
                start++;
            }
            else
            {
                Set.erase(s[end]);
                end++;
            }

        }

        return max;
    }
};
