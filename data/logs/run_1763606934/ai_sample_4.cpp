// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_941le
    // AI-like solution temp_941late
    unordered_map<int,int> mp_941;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_941.count(want)) {{
            cout<<mp_941[want]<<" "<<i<<"\n";
            break;
        }}
        mp_941[nums[i]] = i;
    }}
    return 0;
}}