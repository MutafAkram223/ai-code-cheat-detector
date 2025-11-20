// AI-generated sample
#include <bits/stdc++.h>
using namespace std;
int main(){{
    vector<int> a;
    unordered_map<int,int> pos;
    for(int i=0;i<(int)a.size();i++){{
        int need = target - a[i];
        if(pos.find(need) != pos.end()) {{
            cout<<pos[need]<<" "<<i;
            return 0;
        }}
        pos[a[i]] = i;
    }}
    return 0;
}}