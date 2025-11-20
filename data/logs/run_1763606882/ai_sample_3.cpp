// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_356le
    // AI-like solution temp_356late
    unordered_map<int,int> mp_356;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_356.count(want)) {{
            cout<<mp_356[want]<<" "<<i<<"\n";
            break;
        }}
        mp_356[nums[i]] = i;
    }}
    return 0;
}}