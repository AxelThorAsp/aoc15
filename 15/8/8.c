#include <stdio.h>

#define SLASH 92
#define DOUBLEQ 34

int main(void)
{
    char c, next;
    size_t total_c = 0;
    size_t sub = 0; 
    while((c = getc(stdin)) != EOF)
    {
        if (c == '\n')
            continue;
        if (c + 0 != DOUBLEQ && c + 0 != SLASH)
            sub++;
        if (c + 0 == SLASH)
        {
            next = getc(stdin);
            total_c++;
            if (next == 'x')
            {
                getc(stdin);
                getc(stdin);
                total_c += 2;
            }
            sub++;
        }
        total_c++;
    }
    printf("Total, %lu\n", total_c);
    printf("Sub, %lu\n", sub);
    printf("Dif, %lu\n", total_c - sub);
    return 0;
}
