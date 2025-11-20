// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_549le
    // AI-like solution temp_549late
    unordered_map<int,int> mp_549;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_549.count(want)) {{
            cout<<mp_549[want]<<" "<<i<<"\n";
            break;
        }}
        mp_549[nums[i]] = i;
    }}
    return 0;
}}