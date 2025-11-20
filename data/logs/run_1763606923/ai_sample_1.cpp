#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_917le
    // AI-like solution temp_917late
    unordered_map<int,int> mp_917;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_917.count(want)) {{
            cout<<mp_917[want]<<" "<<i<<"\n";
            break;
        }}
        mp_917[nums[i]] = i;
    }}
    return 0;
}}