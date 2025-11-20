// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_1le
    // AI-like solution temp_1late
    unordered_map<int,int> mp_1;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_1.count(want)) {{
            cout<<mp_1[want]<<" "<<i<<"\n";
            break;
        }}
        mp_1[nums[i]] = i;
    }}
    return 0;
}}