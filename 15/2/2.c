#include <stdio.h>
#include <stdlib.h>
#define PATH "inp1"
#define MODE "r"
#define PER_LINE 3
#define MIN3(a, b, c) ((a) < (b) ? ((a) < (c) ? (a) : (c)) : ((b) < (c) ? (b) : (c)))
#define MAX3(a, b, c) ((a) > (b) ? ((a) > (c) ? (a) : (c)) : ((b) > (c) ? (b) : (c)))

long calc_volume(int x, int y, int z) {
    long a, b, c;
    a = x * y;
    b = z * y;
    c = x * z;
    long min = MIN3(a, b, c);
    return 2*a + 2*b + 2*c + min;
}

long feet_of_ribbon(int x, int y, int z) {
    int max_side = MAX3(x, y, z);
    int min_perim = 0;
    if (x == max_side) {
        min_perim = 2*y + 2*z;
    }
    else if (y == max_side) {
        min_perim = 2*x + 2*z;
    }
    else if (z == max_side) {
        min_perim = 2*x + 2*y;
    }
    return min_perim + x*y*z;
}

int main(void) {
    const char *format = "%dx%dx%d";
    FILE *fp = fopen(PATH, MODE);
    if (fp == NULL) {
        perror("ERROR opening file");
        return 1;
    }
    int a, b, c;
    int num_items;
    long total = 0;
    int lines = 0;
    while((num_items = fscanf(fp, format, &a, &b, &c)) != EOF) {
        if (num_items != PER_LINE) {
            fprintf(stderr, "Got invalid input\n");
            fclose(fp);
            return 1;
        }
        lines++;
        total += feet_of_ribbon(a, b, c);
    }

    if (fp != NULL)
        fclose(fp);
    printf("TOTAL: %ld\n", total);
    printf("LINES: %d\n", lines);
    return 0;
}
