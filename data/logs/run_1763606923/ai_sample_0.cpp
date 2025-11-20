// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_29le
    // AI-like solution temp_29late
    unordered_map<int,int> mp_29;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_29.count(want)) {{
            cout<<mp_29[want]<<" "<<i<<"\n";
            break;
        }}
        mp_29[nums[i]] = i;
    }}
    return 0;
}}