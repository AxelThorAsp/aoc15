#include <iostream>
#include <string>
#include <regex>
#include <algorithm>
#include <numeric>

std::array<std::array<int, 1000>, 1000> m{};

inline void toggle(int x1, int y1, int x2, int y2)
{
    for (int i = x1; i <= x2; i++)
    {
        for (int j = y1; j <= y2; j++ )
        {
            m[j][i] += 2;
        }
    }
}

inline void ok(const std::string& action, int x1, int y1, int x2, int y2)
{
    const int dx = action == "turn on" ? 1 : -1;
    for (int i = x1; i <= x2; i++)
    {
        for (int j = y1; j <= y2; j++ )
        {
            m[j][i] = std::max(m[j][i] + dx, 0);
        }
    }
}

int main()
{
    std::string line;
    int x1, y1, x2, y2;
    const std::regex regex(R"x((\w+(?:\s+\w+)?)\s+(\d+),(\d+)\s+through\s+(\d+),(\d+)\s?)x");
    std::smatch match;
    while(std::getline(std::cin, line))
    {
        if (std::regex_search(line, match, regex))
        {
            const std::string& command = match[1];
            x1 = std::stoi(match[2]);
            y1 = std::stoi(match[3]);
            x2 = std::stoi(match[4]);
            y2 = std::stoi(match[5]);
            if (command == "toggle")
            {
                toggle(x1, y1, x2, y2);
            }
            else
            {
                ok(command, x1, y1, x2, y2);
            }
        }
    }

    size_t t = 0;
    for (const auto& row : m)
    {
        t += std::accumulate(row.begin(), row.end(), 0);
    }
    std::cout << t << std::endl;
    return 0;
}
