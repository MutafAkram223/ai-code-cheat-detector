// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_269le
    // AI-like solution temp_269late
    unordered_map<int,int> mp_269;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_269.count(want)) {{
            cout<<mp_269[want]<<" "<<i<<"\n";
            break;
        }}
        mp_269[nums[i]] = i;
    }}
    return 0;
}}