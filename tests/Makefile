# tool macros
CC = gcc
CXX = g++ # FILL: the compiler
CFLAGS := -g -l -std-c++17 -funroll-all-loops # FILL: compile flags
CXXFLAGS := -g # FILL: compile flags
COBJFLAGS := $(CFLAGS) -c
TARGETS = tests

all: $(TARGETS)

clean:
	rm -f $(TARGERTS)

tests: graph.c
	$(CC) $(CFLAGS) -o $@ $^

.SUFFIXES: