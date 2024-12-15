#include <bits/stdc++.h>
using namespace std;

#ifdef DEBUG
    #define W 11
    #define H 7
#else
    #define W 101
    #define H 103
#endif
#define W2 W / 2
#define H2 H / 2

#define STEPS H * W

vector<pair<int,int>> pos;
vector<pair<int,int>> vel;
array<int,H*W> there = {};

void show()
{
    for (int y = 0; y < H; y++)
    {
        for (int x = 0; x < W; x++)
        {
            if (there[y*W+x])
            {
                cout << "*";
            }
            else
            {
                cout << ".";
            }
        }
        cout << '\n';
    }
}

void step(int i)
{
    auto& p = pos[i];
    auto& v = vel[i];
    int nx = p.first + v.first;
    int ny = p.second + v.second;
    nx = (nx % W + W) % W;
    ny = (ny % H + H) % H;
    p.first = nx;
    p.second = ny;
}

int main()
{
    int a, b, c, d;
    array<int, 4> quads = {};
    size_t min_seen = 99999999999999;
    size_t max_seen = 0;
    size_t p1;
    int p2 = 0;
    while (scanf("p=%d,%d v=%d,%d\n", &a, &b, &c, &d) != EOF)
    {
        pos.push_back(make_pair(a, b));
        vel.push_back(make_pair(c, d));
    }
    for (int t = 0; t < STEPS; t++)
    {
        for (int i = 0; i < (int)pos.size(); i++)
        {
            step(i);
        }

        for (int i = 0; i < (int)pos.size(); i++)
        {
            const auto& p = pos[i];
            int x = p.first;
            int y = p.second;
            there[y*W+x] = true;

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

        if (t == 7343)
        {
            show();
        }

        size_t pp = 1;
        for (auto& q : quads)
        {
            pp *= q;
        }
        if (pp < min_seen)
        {
            p2 = t;
        }
        if (t == 99)
        {
            p1 = pp;
        }
        min_seen = min(pp, min_seen);
        fill(quads.begin(), quads.end(), 0);
        fill(there.begin(), there.end(), false);
    }

    cout << p2 + 1 << '\n';
    cout <<  p1 << endl;
    return 0;
}
