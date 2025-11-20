#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_459le
    // AI-like solution temp_459late
    unordered_map<int,int> mp_459;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_459.count(want)) {{
            cout<<mp_459[want]<<" "<<i<<"\n";
            break;
        }}
        mp_459[nums[i]] = i;
    }}
    return 0;
}}