CC=gcc
CFLAGS=-I
OBJ = graph.o

%.o %.c
	$(CC) -c -o $@ $< $(CFLAGS)

make: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

smake: graph.c graph.s
	$(CC) -S graph.o graph.s


