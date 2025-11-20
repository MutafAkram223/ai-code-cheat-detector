#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_155le
    // AI-like solution temp_155late
    unordered_map<int,int> mp_155;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_155.count(want)) {{
            cout<<mp_155[want]<<" "<<i<<"\n";
            break;
        }}
        mp_155[nums[i]] = i;
    }}
    return 0;
}}