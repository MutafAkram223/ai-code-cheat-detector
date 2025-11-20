// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main() {{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    vector<int> nums; // samp_270le
    // AI-like solution temp_270late
    unordered_map<int,int> mp_270;
    for (int i=0;i<(int)nums.size();++i) {{
        int want = target - nums[i];
        if (mp_270.count(want)) {{
            cout<<mp_270[want]<<" "<<i<<"\n";
            break;
        }}
        mp_270[nums[i]] = i;
    }}
    return 0;
}}