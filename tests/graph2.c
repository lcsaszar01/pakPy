#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

// Define constants
#define ALPHA_SIZE 4
#define K_SIZE 3
#define MAX_KMER_LEN 100
#define MAX_DICT_SIZE 1000

// Define structure for kmer nodes
typedef struct {
    char kmer[MAX_KMER_LEN];
    char type[10];
    char letter;
    int counts[2];
    int term;
} KmerNode;

// Define structure for graph nodes
typedef struct {
    KmerNode nodes[MAX_DICT_SIZE];
    int numNodes;
} Graph;

// Function prototypes
void createNodes(Graph *graph, char *kmer, char *type, char letter, int counts[], int term);
void loop_stat(int counts, char *message);
void data_chart(int tm[], int l[], char *lname[], double ratio[], char *label);
void data_append(int tm[], int lps[]);

int main() {
    char kmer_list[MAX_DICT_SIZE][MAX_KMER_LEN]; // Assuming a maximum dictionary size and kmer length
    int numKmers = 0; // Number of kmers in the list

    // Initialize graph and other variables
    Graph graph;
    graph.numNodes = 0;

    double coverage = 0.000215;
    char alpha[ALPHA_SIZE] = {'A', 'T', 'C', 'G'};

    // Populate kmer_list (assuming it's already filled)

    for (int i = 0; i < numKmers; i++) {
        char kmer_str[MAX_KMER_LEN];
        strcpy(kmer_str, kmer_list[i]);

        char lmer1[MAX_KMER_LEN] = "";
        char lmer2[MAX_KMER_LEN] = "";

        // Extract lmers
        for (int j = 0; j < strlen(kmer_str) - 1; j++) {
            strncat(lmer1, &kmer_str[j], 1);
        }
        for (int j = 1; j < strlen(kmer_str); j++) {
            strncat(lmer2, &kmer_str[j], 1);
        }

        // Process prefixes
        for (int a = 0; a < ALPHA_SIZE; a++) {
            char temp_lmer[MAX_KMER_LEN];
            sprintf(temp_lmer, "%c%s", alpha[a], lmer2);

            // Check if temp_lmer exists in kmer_list

            // Create nodes in the graph
            int counts[2] = {0};
            int term = 0;
            createNodes(&graph, lmer2, "Prefix", alpha[a], counts, term);
        }

        // Process suffixes
        for (int a = 0; a < ALPHA_SIZE; a++) {
            char temp_lmer[MAX_KMER_LEN];
            sprintf(temp_lmer, "%s%c", lmer1, alpha[a]);

            // Check if temp_lmer exists in kmer_list

            // Create nodes in the graph
            int counts[2] = {0};
            int term = 0;
            createNodes(&graph, lmer1, "Suffix", alpha[a], counts, term);
        }
    }

    // Perform stats and data operations
    int tm[MAX_DICT_SIZE], lps[MAX_DICT_SIZE];
    char *lname[MAX_DICT_SIZE];
    loop_stat(numKmers, "graph values break down");
    data_append(tm, lps);

    return 0;
}

void createNodes(Graph *graph, char *kmer, char *type, char letter, int counts[], int term) {
    if (graph->numNodes < MAX_DICT_SIZE) {
        KmerNode newNode;
        strcpy(newNode.kmer, kmer);
        strcpy(newNode.type, type);
        newNode.letter = letter;
        newNode.counts[0] = counts[0];
        newNode.counts[1] = counts[1];
        newNode.term = term;

        graph->nodes[graph->numNodes++] = newNode;
    } else {
        printf("Maximum number of nodes reached.\n");
    }
}

void loop_stat(int counts, char *message) {
    // Implementation of loop_stat function
}

void data_chart(int tm[], int l[], char *lname[], double ratio[], char *label) {
    // Implementation of data_chart function
}

void data_append(int tm[], int lps[]) {
    // Implementation of data_append function
}
