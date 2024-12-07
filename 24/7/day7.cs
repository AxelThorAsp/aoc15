using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Aoc
{
    enum OP
    {
        OP_MUL,
        OP_ADD
    }

    internal class Program
    {
        private static long _target;
        private static long _sum;
        private static void Main(string[] args)
        {
            string? line;
            while((line = Console.ReadLine()) != null)
            {
                var split = line.Split(':');
                _target = long.Parse(split[0].Trim());
                var equation = split[1].Split(' ', StringSplitOptions.RemoveEmptyEntries).Select(long.Parse).ToArray();
                if (Backtrack(equation))
                {
                    _sum += _target;
                }
            }
            Console.WriteLine(_sum);
        }

        static bool Backtrack(long[] equation)
        {
            if (equation.Length == 1)
            {
                return equation[0] == _target;
            }
            for (int j = 0; j < 2; j++)
            {
                var op = (OP)j;
                var res = Eval(equation, 0, op);
                if (equation.Length == 2 && res < _target)
                {
                    continue;
                }
                if (res > _target || res == -1)
                {
                    continue;
                }

                if (equation.Length == 2 && res == _target)
                {
                    return true; 
                }
                var newEquation = new long[equation.Length - 1];
                newEquation[0] = res;
                for (int k = 1; k < newEquation.Length; k++)
                {
                    newEquation[k] = equation[k+1];
                }
                if (Backtrack(newEquation))
                {
                    return true;
                }
            }
            return false;
        }

        private static long Eval(long[] equation, int i, OP op)
        {
            if (equation.Length == 1)
            {
                return equation[0];
            }
            if (i + 1 >= equation.Length)
            {
                return -1;
            }
            switch (op)
            {
                case OP.OP_MUL:
                {
                    var res = checked(equation[i] * equation[i + 1]);
                    return res;
                }
                case OP.OP_ADD:
                {
                    var res = checked(equation[i] + equation[i + 1]);
                    return res;
                }
                default:
                    throw new ArgumentOutOfRangeException();
            }
        }
    }
}

