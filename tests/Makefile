# tool macros
CC = gcc

#Flags 
CFLAGS = -O2 -g -Wall -Wextra -Wconversion -Wshadow -pedantic -Werror# FILL: compile flags

CXXFLAGS = -g # FILL: compile flags

SOURCES = graph.c
OBJECTS = graph.o 
TARGET = graph

#initialize directories

$(TARGET): $(OBJECTS)
	$(CC) $(CFLAGS) -o $(TARGET) $(OBJECTS)

#machine_code: 


all: $(TARGET) 

clean:
	rm -rf $(TARGET) $(OBJECTS)


