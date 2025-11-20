// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_18le
    // AI-like solution temp_18late
    unordered_map<int,int> mp_18;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_18.count(want)) {{
            cout<<mp_18[want]<<" "<<i<<"\n";
            break;
        }}
        mp_18[nums[i]] = i;
    }}
    return 0;
}}