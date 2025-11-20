// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_365le
    // AI-like solution temp_365late
    unordered_map<int,int> mp_365;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_365.count(want)) {{
            cout<<mp_365[want]<<" "<<i<<"\n";
            break;
        }}
        mp_365[nums[i]] = i;
    }}
    return 0;
}}