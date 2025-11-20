#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_841le
    // AI-like solution temp_841late
    unordered_map<int,int> mp_841;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_841.count(want)) {{
            cout<<mp_841[want]<<" "<<i<<"\n";
            break;
        }}
        mp_841[nums[i]] = i;
    }}
    return 0;
}}