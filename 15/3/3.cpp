#include <iostream>
#include <unordered_set>

inline std::string hash(const int& x, const int& y)
{
    std::string result = std::to_string(x) + "," + std::to_string(y);
    return result;
}

inline void add(const int& x, const int& y, std::unordered_set<std::string>& _set) {
    std::string value = hash(x, y);
    _set.insert(value);
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::unordered_set<std::string> _set;
    int x = 0, y = 0;
    int xr = 0, yr = 0;
    add(0, 0, _set);
    std::string line;
    std::getline(std::cin, line);
    short flip = 1;
    for (char c : line) {
        if (flip == 1){
            switch (c) {
                case '^':
                    y++;
                    break;
                case 'v':
                    y--;
                    break;
                case '>':
                    x++;
                    break;
                case '<':
                    x--;
                    break;
                default:
                    std::cout << "Unexpected argument: " << c << std::endl;
                    return 1;
            }
            add(x, y, _set);
        }
        else if (flip == -1){
            switch (c) {
                case '^':
                    yr++;
                    break;
                case 'v':
                    yr--;
                    break;
                case '>':
                    xr++;
                    break;
                case '<':
                    xr--;
                    break;
                default:
                    std::cout << "Unexpected argument: " << c << std::endl;
                    return 1;
            }
            add(xr, yr, _set);
        }
        else {
            std::cout << "Unexpected flip" << flip << std::endl;
            return 1;
        }
        flip *= -1;
    }
    std::cout << _set.size() << '\n';
    return 0;
}

int main1() {
    std::unordered_set<std::string> _set;
    int x = 0, y = 0;
    add(0, 0, _set);
    std::string line;
    std::getline(std::cin, line);
    for (char c : line) {
        switch (c) {
            case '^':
                y++;
                break;
            case 'v':
                y--;
                break;
            case '>':
                x++;
                break;
            case '<':
                x--;
                break;
            default:
                std::cout << "Unexpected argument: " << c << std::endl;
                return 1;
        }
        add(x, y, _set);
    }
    std::cout << _set.size() << std::endl;
    return 0;
}
