// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_537le
    // AI-like solution temp_537late
    unordered_map<int,int> mp_537;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_537.count(want)) {{
            cout<<mp_537[want]<<" "<<i<<"\n";
            break;
        }}
        mp_537[nums[i]] = i;
    }}
    return 0;
}}