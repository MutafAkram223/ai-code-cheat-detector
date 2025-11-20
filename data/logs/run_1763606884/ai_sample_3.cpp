// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_261le
    // AI-like solution temp_261late
    unordered_map<int,int> mp_261;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_261.count(want)) {{
            cout<<mp_261[want]<<" "<<i<<"\n";
            break;
        }}
        mp_261[nums[i]] = i;
    }}
    return 0;
}}