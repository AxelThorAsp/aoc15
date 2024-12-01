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
    std::string line;
    int a, b;
    const std::regex regex(R"x((\d+)\s+(\d+))x");
    std::smatch match;
    while(std::getline(std::cin, line))
    {
        if (std::regex_search(line, match, regex))
        {
            a = std::stoi(match[1]);
            b = std::stoi(match[2]);
            v.push_back(a);
            m[b]++;
        }
    }

    size_t t = 0;
    for (const auto& i : v)
    {
        t += m[i]*i;
    }
    std::cout << t << std::endl;
    return 0;
}