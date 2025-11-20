#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_784le
    // AI-like solution temp_784late
    unordered_map<int,int> mp_784;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_784.count(want)) {{
            cout<<mp_784[want]<<" "<<i<<"\n";
            break;
        }}
        mp_784[nums[i]] = i;
    }}
    return 0;
}}