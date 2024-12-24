#include <stdio.h>

long prune(long val)
{
    return val % 16777216;
}

long mix(long secret, long val)
{
    return secret ^ val;
}

long next(long s)
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
    size_t sum = 0;
    while (scanf("%ld", &s) != EOF)
    {
        for (int i = 0; i < 2000; i++)
        {
            s = next(s);
        }
        printf("%lu\n", s % 10);
        sum+=s;
    }
    return 0;
}
