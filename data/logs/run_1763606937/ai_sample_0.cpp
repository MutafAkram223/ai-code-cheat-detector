// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_548le
    // AI-like solution temp_548late
    unordered_map<int,int> mp_548;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_548.count(want)) {{
            cout<<mp_548[want]<<" "<<i<<"\n";
            break;
        }}
        mp_548[nums[i]] = i;
    }}
    return 0;
}}