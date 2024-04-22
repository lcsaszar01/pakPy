//graph.c
//authpr @lcsaszar01
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <float.h>
#include <sys/sysinfo.h>

int sysinfo(struct sysinfo *info);

// Define constants
#define ALPHA_SIZE 4
#define K_SIZE 3
#define MAX_KMER_LEN 100
#define MAX_DICT_SIZE 1000
#define COVERAGE 0.000215

// Define structure for kmer nodes
typedef struct {
    char kmer[MAX_KMER_LEN];
    char type[10];
    char letter;
    int counts[2];
    int term;
} KmerNode;

// Function prototypes
void createNodes(Graph *graph, char *kmer, char *type, char letter, int counts[], int term);
void loop_stat(int counts, char *message);
void data_chart(int tm[], int l[], char *lname[], double ratio[], char *label);
void data_append(int tm[], int lps[]);

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

int main(int argc, char *argv[]){

    printf("setting up graph\n");
    printf("Mem unit sz in bytes = %llu", info.mem_unit);


    /// Opens the kmer_lst file
    FILE *fd1;
    fd1 = fopen("kmer_lst.txt", "r");
    char kmer_list[BUFSIZ];

    fgets(kmer_list, BUFSIZ, fd1);
    // printf("%s",kmer_list);
    fclose(fd1);
    printf("%s\n", kmer_list);

    // Opens the kmer-1 file
    FILE *fd2;
    fd2 = fopen("kmer_1.txt", "r");
    char kmer_1[BUFSIZ];
    fgets(kmer_1, BUFSIZ, fd2);
    fclose(fd2);

    printf("Done importing kmer files.\n");
    
    double lst[BUFSIZ][2];

    char kmer_list[MAX_DICT_SIZE][MAX_KMER_LEN]; // Assuming a maximum dictionary size and kmer length
    int numKmers = 0; // Number of kmers in the list

    int counter_for_find = 0;
    int counter_for_find2 = 0;
    int count = 0;
    char temp_lmer[BUFSIZ];
    char alpha[ALPHA_SIZE] = {'A', 'T', 'C', 'G'};



    //printf("%s\n", kmer_1); 
    // Converst the kmer_list into token of strings
    char * token_strings;
    token_strings = strtok(kmer_list,", \n");
    char * tok_str;
    tok_str = strtok(kmer_1,", \n");
    //printf("%s\n", tok_str);



    // LOOKS AT THE PREFIXES THAT CAN OCCURE
    for (int i = 0; i <= numKmers; i++)
    {
        
        count++;
        char lmer1[MAX_KMER_LEN] = "";
        char lmer2[MAX_KMER_LEN] = "";
        printf("%s\n", alpha[i]);
        strcat(temp_lmer, &alpha[i]);
        printf("%s\n",temp_lmer);
        printf("stats: \t Availabel mem sz = %llu,
                    \n\t\t total swap sz = %llu,
                    \n\t\t Available high mem sz = %llu",
                    info.freeram, info.totalswap, info.freehigh);
        break;
        //strcat(temp_lmer, kmer_1);
        //printf("%s\n", temp_lmer);

        for (int a = 0; a < ALPHA_SIZE; a++)
        {
            char temp_lmer[MAX_KMER_LEN];
            sprintf(temp_lmer, "%s%c", lmer1, alpha[a]);

            // Check if temp_lmer exists in kmer_list

            // Create nodes in the graph
            int counts[2] = {0};
            int term = 0;
            createNodes(&graph, lmer1, "Suffix", alpha[a], counts, term);
        }

        if (counter_for_find > 0)
        {
            double visit_count = counter_for_find / coverage;
            lst[count][1] = counter_for_find;
            lst[count][0] = visit_count;
        }
    }
    
    /*
    // For Suffixes
    for (int i = 0; i < (int)strlen(alpha); i++)
    {
        count++;
        strcat(temp_lmer, kmer_1);
        strcat(temp_lmer, &alpha[i]);

        // See if the string has a match is the strings
        for (int x = 0; x <= (int)strlen(kmer_list); x++)
        {

            if (kmer_list[x] == (char)*temp_lmer)
            {
                // printf("kmer list: %s \n", &kmer_list[x]);
                // printf("temp lmer: %s \n", temp_lmer);
                counter_for_find2++;

                int kmers = (int)strlen(kmer_list);
                if (x == kmers || x == 0)
                {
                    // term = 1;
                }
            }
        }

        if (counter_for_find > 0)
        {
            double visit_count = counter_for_find / coverage;
            lst[count][1] = counter_for_find;
            lst[count][0] = visit_count;
        }
    */
    }

    // Perform stats and data operations
    int tm[MAX_DICT_SIZE], lps[MAX_DICT_SIZE];
    char *lname[MAX_DICT_SIZE];
    loop_stat(numKmers, "graph values break down");
    data_append(tm, lps);

    return 0;
}

