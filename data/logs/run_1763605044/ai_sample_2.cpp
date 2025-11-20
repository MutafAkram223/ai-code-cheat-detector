// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_424le
    // AI-like solution temp_424late
    unordered_map<int,int> mp_424;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_424.count(want)) {{
            cout<<mp_424[want]<<" "<<i<<"\n";
            break;
        }}
        mp_424[nums[i]] = i;
    }}
    return 0;
}}