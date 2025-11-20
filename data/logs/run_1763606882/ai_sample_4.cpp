// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_255le
    // AI-like solution temp_255late
    unordered_map<int,int> mp_255;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_255.count(want)) {{
            cout<<mp_255[want]<<" "<<i<<"\n";
            break;
        }}
        mp_255[nums[i]] = i;
    }}
    return 0;
}}