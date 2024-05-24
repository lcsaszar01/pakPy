//graph.h
//header file for graph.c
//@author: Lydia Csaszar

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <float.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
// include <cpucycles.h>

// Define constants
#define ALPHA_SIZE 4
#define K_SIZE 3
#define MAX_KMER_LEN 100
#define MAX_DICT_SIZE 1000
#define COVERAGE 0.000215
#define NUM_FILES 500

// Define structure for kmer nodes
typedef struct
{
    char kmer[MAX_KMER_LEN];
    char type[10];
    char letter;
    int counts[2];
    int term;
} KmerNode;

// Define structure for graph nodes
typedef struct
{
    KmerNode nodes[MAX_DICT_SIZE];
    int numNodes;
} Graph;

void createNodes(Graph *graph, char *kmer, char *type, char letter, int counts[], int term)
{
    if (graph->numNodes < MAX_DICT_SIZE)
    {
        KmerNode newNode;
        strcpy(newNode.kmer, kmer);
        strcpy(newNode.type, type);
        newNode.letter = letter;
        newNode.counts[0] = counts[0];
        newNode.counts[1] = counts[1];
        newNode.term = term;

        graph->nodes[graph->numNodes++] = newNode;
    }
    else
    {
        printf("Maximum number of nodes reached.\n");
    }
}
