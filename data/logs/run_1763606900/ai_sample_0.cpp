// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_474le
    // AI-like solution temp_474late
    unordered_map<int,int> mp_474;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_474.count(want)) {{
            cout<<mp_474[want]<<" "<<i<<"\n";
            break;
        }}
        mp_474[nums[i]] = i;
    }}
    return 0;
}}