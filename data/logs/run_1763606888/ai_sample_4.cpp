#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_283le
    // AI-like solution temp_283late
    unordered_map<int,int> mp_283;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_283.count(want)) {{
            cout<<mp_283[want]<<" "<<i<<"\n";
            break;
        }}
        mp_283[nums[i]] = i;
    }}
    return 0;
}}