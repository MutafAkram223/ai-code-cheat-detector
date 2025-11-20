#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_351le
    // AI-like solution temp_351late
    unordered_map<int,int> mp_351;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_351.count(want)) {{
            cout<<mp_351[want]<<" "<<i<<"\n";
            break;
        }}
        mp_351[nums[i]] = i;
    }}
    return 0;
}}