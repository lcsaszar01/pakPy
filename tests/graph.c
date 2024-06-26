//graph.c
//author @lcsaszar01
#include "graph.h"

// Function prototypes
void createNodes(Graph *graph, char *kmer, char *type, char letter, int counts[], int term);
//long long count = cpucycles();
//long long persecond = cpucycles_persecond();
//const char *implementation = cpucycles_implementation();
//const char *version = cpucycles_version();
//void loop_stat(int counts, char *message);
//void data_chart(int tm[], int l[], char *lname[], double ratio[], char *label);
//void data_append(int tm[], int lps[]);

int main(void){
    printf("here");
	for(int h = 0; h <= 500; h++){
    // Opens the kmer_lst file

		char string[50];
		char temper[4];
    	char fstring[32];
    	char * line;
        const char *str = temper;

        memset(string, 0, 50);
        printf("HERE");
		strcat(string,"../kmers/dna_kmer_");
        snprintf(temper, sizeof(temper), "%d", h);
		strcat(string,str);
		strcat(string,".txt");
        printf("%s", string);
        

    	FILE *fd1;
    	fd1 = fopen(string, "r");
    	char kmer_list[MAX_DICT_SIZE][MAX_KMER_LEN]; // Assuming a maximum dictionary size and kmer length

    	for(int k = 0; k <= NUM_FILES; k++){
        	for(int f = 0; f <= MAX_DICT_SIZE; f++){
            	fgets(fstring, BUFSIZ, fd1);
            	line= strtok(fstring, ", ");
            	while(line != NULL){
                	line = strtok(fstring, ", ");
                	fgets(&kmer_list[f][f], BUFSIZ, fd1);
                	//sprintf("%s%s", kmer_list[f][f]);
            	}
        	}
   		}


        fclose(fd1);
    }

    printf("Done importing kmer files.\n");
    
    double lst[BUFSIZ][2];

    int numKmers = 0; // Number of kmers in the list

    int counter_for_find = 0;
    //int counter_for_find2 = 0;
    int count = 0;
    //char temp_lmer[MAX_DICT_SIZE];
    char alpha[ALPHA_SIZE] = {'A', 'T', 'C', 'G'};

    // LOOKS AT THE PREFIXES THAT CAN OCCURE
    for (int i = 0; i <= numKmers; i++)
    {
        count++;
        char lmer1[MAX_KMER_LEN] = "";
        //char lmer2[MAX_KMER_LEN] = "";

        for (int a = 0; a < ALPHA_SIZE; a++){
            for (int o = 0; o <= MAX_DICT_SIZE-1; o++){
                for (int e = 0; e <= MAX_KMER_LEN-1; e++){
                    printf("%c\n", alpha[a]);
                    //strcat(&kmer_list[o][e], &alpha[a]);
                    //sprintf("%s\n", temp_lmer);
                }
            }


            // Check if temp_lmer exists in kmer_list
            

            // Create nodes in the graph
            int counts[2] = {0};
            int term = 0;
            createNodes(0, lmer1, "Suffix", alpha[a], counts, term);
        }

        if (counter_for_find > 0)
        {
            double visit_count = counter_for_find / COVERAGE;
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
            double visit_count = counter_for_find / COVERAGE;
            lst[count][1] = counter_for_find;
            lst[count][0] = visit_count;
        }
    }
    */

    // Perform stats and data operations
    //int tm[MAX_DICT_SIZE],
    //lps[MAX_DICT_SIZE];
    //char *lname[MAX_DICT_SIZE];
    //loop_stat(numKmers, "graph values break down");
    //data_append(tm, lps);

    return 0;
}
