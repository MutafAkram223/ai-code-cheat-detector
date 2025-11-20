// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_146le
    // AI-like solution temp_146late
    unordered_map<int,int> mp_146;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_146.count(want)) {{
            cout<<mp_146[want]<<" "<<i<<"\n";
            break;
        }}
        mp_146[nums[i]] = i;
    }}
    return 0;
}}