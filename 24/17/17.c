#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

#define adv 0
#define bxl 1
#define bst 2
#define jnz 3
#define bxc 4
#define out 5
#define bdv 6
#define cdv 7

typedef unsigned char uc;
typedef unsigned int ui;

uc program[] = { 0, 1, 5, 4, 3, 0 };

size_t prog_size = (sizeof program) / (sizeof program[0]); 

ui combo(uc operand, ui *a, ui *b, ui *c)
{
    switch (operand)
    {
        case 0:
        case 1:
        case 2:
        case 3:
            return operand;
        case 4:
            return *a;
        case 5:
            return *b;
        case 6:
            return *c;
        default:
            fprintf(stderr, "ERROR: Uknown operand %d\n", operand);
            exit(EXIT_FAILURE);
    }
}

void resolve(uc opcode, uc operand, ui *a, ui *b, ui *c, size_t *ip)
{
    switch (opcode)
    {
        case adv:
            *a = *a >> combo(operand, a, b, c);
            *ip += 2;
            break;
        case bxl:
            *b = *b ^ operand;
            *ip += 2;
            break;
        case bst:
            *b = combo(operand, a, b, c) & 7;
            *ip += 2;
            break;
        case jnz:
            if (*a == 0) {
                *ip += 2;
            }
            else {
                *ip = operand;
            }
            break;
        case bxc:
            *b = *b ^ *c;
            *ip += 2;
            break;
        case out:
           printf("%u,", combo(operand, a, b, c) & 7);
           *ip += 2;
           break;
        case bdv:
            *b = *a >> combo(operand, a, b, c);
            *ip += 2;
            break;
        case cdv:
            *c = *a >> combo(operand, a, b, c);
            *ip += 2;
            break;
        default:
            fprintf(stderr, "ERROR: Uknown opcode %d\n", opcode);
            exit(EXIT_FAILURE);
    }
}

int main(void)
{
    ui a = 729;
    ui b = 0;
    ui c = 0;
    size_t ip = 0;
    while (ip < prog_size)
    {
        assert(ip + 1 < prog_size); uc opcode = program[ip];
        uc operand = program[ip + 1];
        resolve(opcode, operand, &a, &b, &c, &ip);
    }
    printf("\n");
    return 0;
}
