#include <iostream>
#include <string>
#include <regex>
#include <algorithm>
#include <numeric>
#include <unordered_map>

std::unordered_map<int, int> m{};
std::vector<int> v{};

int main()
{
    int a, b;
    while (std::cin >> a >> b) {
        v.push_back(a);
        m[b]++;
    }

    size_t t = 0;
    for (const auto& i : v)
    {
        t += m[i]*i;
    }
    std::cout << t << std::endl;
    return 0;
}