// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_389le
    // AI-like solution temp_389late
    unordered_map<int,int> mp_389;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_389.count(want)) {{
            cout<<mp_389[want]<<" "<<i<<"\n";
            break;
        }}
        mp_389[nums[i]] = i;
    }}
    return 0;
}}