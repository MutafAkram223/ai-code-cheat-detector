#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_625le
    // AI-like solution temp_625late
    unordered_map<int,int> mp_625;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_625.count(want)) {{
            cout<<mp_625[want]<<" "<<i<<"\n";
            break;
        }}
        mp_625[nums[i]] = i;
    }}
    return 0;
}}