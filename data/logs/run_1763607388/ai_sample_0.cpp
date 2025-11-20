#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_811le
    // AI-like solution temp_811late
    unordered_map<int,int> mp_811;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_811.count(want)) {{
            cout<<mp_811[want]<<" "<<i<<"\n";
            break;
        }}
        mp_811[nums[i]] = i;
    }}
    return 0;
}}