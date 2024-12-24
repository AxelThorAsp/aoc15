#include <stdio.h>
#include <iostream>
#include <vector>
#include <map>
#include <tuple>
#include <set>
#include <assert.h>

using namespace std;


map<tuple<short,short,short,short>, short> M = {};
set<tuple<short, short, short, short>> S = {};

inline long prune(long val)
{
    return val % 16777216;
}

inline long mix(long secret, long val)
{
    return secret ^ val;
}

inline long next(long s)
{
    s = mix(s, s * 64);
    s = prune(s);
    s = mix(s, (long) (s / 32));
    s = prune(s);
    s = mix(s, s * 2048);
    s = prune(s);
    return s;
}


int main(void)
{
    long s;
    while (scanf("%ld", &s) != EOF)
    {
        vector<short> v;
        v.push_back(s%10);
        S.clear();
        for (int i = 0; i < 1999; i++)
        {
            s = next(s);
            v.push_back(s%10);
        }
        for (int i = 1; i < (int)v.size()-3; i++)
        {
            short a,b,c,d,e;
            a = v[i] - v[i-1];
            b = v[i + 1] - v[i];
            c = v[i + 2] - v[i + 1];
            d = v[i + 3] - v[i + 2];
            e = v[i + 3];
            tuple<short, short, short, short> t = make_tuple(a,b,c,d);
            if (S.find(t) == S.end())
            {
                M[t] += e;
                S.emplace(t);
            }
        }
    }
    short m = 0;
    for (const auto& t : M) {
        m = max(t.second, m);
    }
    cout << m << endl;
    return 0;
}
