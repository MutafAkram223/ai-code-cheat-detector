#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_284le
    // AI-like solution temp_284late
    unordered_map<int,int> mp_284;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_284.count(want)) {{
            cout<<mp_284[want]<<" "<<i<<"\n";
            break;
        }}
        mp_284[nums[i]] = i;
    }}
    return 0;
}}