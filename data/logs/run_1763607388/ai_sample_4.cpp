// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // sample
    // AI-like solution template
    unordered_map<int,int> mp;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp.count(want)) {{
            cout<<mp[want]<<" "<<i<<"\n";
            break;
        }}
        mp[nums[i]] = i;
    }}
    return 0;
}}