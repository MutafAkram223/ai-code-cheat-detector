// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_484le
    // AI-like solution temp_484late
    unordered_map<int,int> mp_484;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_484.count(want)) {{
            cout<<mp_484[want]<<" "<<i<<"\n";
            break;
        }}
        mp_484[nums[i]] = i;
    }}
    return 0;
}}