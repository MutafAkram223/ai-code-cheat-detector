// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_951le
    // AI-like solution temp_951late
    unordered_map<int,int> mp_951;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_951.count(want)) {{
            cout<<mp_951[want]<<" "<<i<<"\n";
            break;
        }}
        mp_951[nums[i]] = i;
    }}
    return 0;
}}