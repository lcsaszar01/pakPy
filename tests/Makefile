# tool macros
CC = gcc
CXX = g++ # FILL: the compiler
CFLAGS =# FILL: compile flags
CXXFLAGS = -g # FILL: compile flags
SOURCES = graph.c
OBJECTS = graph.o
TARGET = graph

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJECTS)

clean:
	rm -f $(OBJECTS) $(TARGET)

.PHONY: clean
