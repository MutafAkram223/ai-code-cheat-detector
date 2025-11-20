// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_571le
    // AI-like solution temp_571late
    unordered_map<int,int> mp_571;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_571.count(want)) {{
            cout<<mp_571[want]<<" "<<i<<"\n";
            break;
        }}
        mp_571[nums[i]] = i;
    }}
    return 0;
}}