// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_307le
    // AI-like solution temp_307late
    unordered_map<int,int> mp_307;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_307.count(want)) {{
            cout<<mp_307[want]<<" "<<i<<"\n";
            break;
        }}
        mp_307[nums[i]] = i;
    }}
    return 0;
}}