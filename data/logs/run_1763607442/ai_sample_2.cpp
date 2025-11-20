// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_51le
    // AI-like solution temp_51late
    unordered_map<int,int> mp_51;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_51.count(want)) {{
            cout<<mp_51[want]<<" "<<i<<"\n";
            break;
        }}
        mp_51[nums[i]] = i;
    }}
    return 0;
}}