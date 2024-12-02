CC = g++
CFLAGS = -Wall -Wextra -Werror -O3
SOURCE = 1.cpp
OUT = 1.o

all: $(OUT)

$(OUT): $(SOURCE)
	$(CC) $(CFLAGS) $(SOURCE) -o $(OUT)

run: $(OUT)
	./$(OUT)