#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <stdexcept>
#include <cctype>
#include <cstdlib>

using namespace std;

enum class OP {
    OP_MUL,
    OP_ADD,
    OP_CAT
};

static long _target;
static long _sum = 0;

bool Backtrack(const vector<long>& equation);
long Eval(const vector<long>& equation, size_t i, OP op);

int main() {
    string line;
    while (getline(cin, line)) {
        auto colonPos = line.find(":");
        if (colonPos == string::npos) {
            cerr << "Invalid input format" << endl;
            continue;
        }

        _target = stol(line.substr(0, colonPos));
        string equationPart = line.substr(colonPos + 1);

        istringstream iss(equationPart);
        vector<long> equation;
        string token;
        while (iss >> token) {
            equation.push_back(stol(token));
        }

        if (Backtrack(equation)) {
            _sum += _target;
        }
    }

    cout << _sum << endl;
    return 0;
}

bool Backtrack(const vector<long>& equation) {
    if (equation.size() == 1) {
        return equation[0] == _target;
    }

    for (int j = 0; j < 3; ++j) {
        OP op = static_cast<OP>(j);
        long res = Eval(equation, 0, op);

        if (equation.size() == 2 && res < _target) {
            continue;
        }
        if (res > _target || res == -1) {
            continue;
        }

        if (equation.size() == 2 && res == _target) {
            return true;
        }

        vector<long> newEquation(equation.size() - 1);
        newEquation[0] = res;
        for (size_t k = 1; k < newEquation.size(); ++k) {
            newEquation[k] = equation[k + 1];
        }

        if (Backtrack(newEquation)) {
            return true;
        }
    }
    return false;
}

long Eval(const vector<long>& equation, size_t i, OP op) {
    if (equation.size() == 1) {
        return equation[0];
    }
    if (i + 1 >= equation.size()) {
        return -1;
    }

    try {
        switch (op) {
            case OP::OP_MUL: {
                return equation[i] * equation[i + 1];
            }
            case OP::OP_ADD: {
                return equation[i] + equation[i + 1];
            }
            case OP::OP_CAT: {
                string concatenated = to_string(equation[i]) + to_string(equation[i + 1]);
                return stol(concatenated);
            }
            default:
                throw out_of_range("Invalid operation");
        }
    } catch (const overflow_error&) {
        return -1;
    }
}

