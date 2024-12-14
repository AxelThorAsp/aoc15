#include <bits/stdc++.h>
using namespace std;

#define STEPS 100
#ifdef DEBUG
    #define W 11
    #define H 7
#else
    #define W 101
    #define H 103
#endif
#define W2 W / 2
#define H2 H / 2

vector<pair<int,int>> pos;
vector<pair<int,int>> vel;

void step(int i)
{
    auto& p = pos[i];
    auto& v = vel[i];
    int nx = p.first + v.first * 100;
    int ny = p.second + v.second * 100;
    nx = (nx % W + W) % W;
    ny = (ny % H + H) % H;
    p.first = nx;
    p.second = ny;
}

int main()
{
    int a, b, c, d;
    array<int, 4> quads = {};
    while (scanf("p=%d,%d v=%d,%d\n", &a, &b, &c, &d) != EOF)
    {
        pos.push_back(make_pair(a, b));
        vel.push_back(make_pair(c, d));
    }

    for (int i = 0; i < (int)pos.size(); i++)
    {
        step(i);
    }

    for (int i = 0; i < (int)pos.size(); i++)
    {
        const auto& p = pos[i];
        int x = p.first;
        int y = p.second;

        if (x < W2 && y < H2)
        {
            quads[0]++;
        }
        if (x > W2 && y < H2)
        {
            quads[1]++;
        }
        if (x < W2 && y > H2)
        {
            quads[2]++;
        }
        if (x > W2 && y > H2)
        {
            quads[3]++;
        }
    }

    size_t t = 1;
    for (auto& q : quads)
    {
        t *= q;
    }

    cout << t << endl;
    return 0;
}
