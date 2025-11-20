#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_854le
    // AI-like solution temp_854late
    unordered_map<int,int> mp_854;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_854.count(want)) {{
            cout<<mp_854[want]<<" "<<i<<"\n";
            break;
        }}
        mp_854[nums[i]] = i;
    }}
    return 0;
}}