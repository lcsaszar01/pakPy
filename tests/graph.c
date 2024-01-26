//graph.c
//author @lcsaszar01
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <float.h>

int main(int argc, char *argv[]){
    printf("setting up graph\n");
    double coverage = 0.000215;

    /// Opens the kmer_lst file
    FILE *fd1;
    fd1 = fopen("kmer_lst.txt", "r");
    char kmer_list[BUFSIZ];

    fgets(kmer_list, BUFSIZ, fd1);
    // printf("%s",kmer_list);
    fclose(fd1);
    //printf("%s\n", kmer_list);

    // Opens the kmer-1 file
    FILE *fd2;
    fd2 = fopen("kmer_1.txt", "r");
    char kmer_1[BUFSIZ];
    fgets(kmer_1, BUFSIZ, fd2);
    fclose(fd2);

    printf("Done importing kmer files.\n");

    printf("%s\n\n", kmer_1);
    printf("%s\n\n", kmer_list);

    double lst[BUFSIZ][2];

    int counter_for_find = 0;
    int counter_for_find2 = 0;
    int count = 0;
    
    char alpha[] = {'A','C','G','T','\0'};

    //printf("%s\n", kmer_1); 
    // Converst the kmer_list into token of strings
    char * token_strings;
    token_strings = strtok(kmer_list,",");
    char * tok_str;
    tok_str = strtok(kmer_1,", \n");
    printf("%s\n\n", &token_strings[0]);
    //printf("%s\n", tok_str);
    char * kmer_str;
    char * n;
 
    // LOOKS AT THE PREFIXES THAT CAN OCCURE
    for (int i = 0; i < 4; i++)
    {
        printf("%s\n\n", "Starting Prefixes");

        char * temp_lmer;
        temp_lmer = (char *)calloc(29, sizeof(char));

        count++;
        strncat(temp_lmer, &alpha[i], 1);//prints prefix
        printf("%s\n\n",temp_lmer);
        for (int u = 0; u <= 39; u++){
            strncat(temp_lmer, &kmer_list[u], 1); 
        }
        printf("%s\n\n", temp_lmer); //prints kmer-1 appended ot prefix

        // See if the string has a match is the strings
        for (int x = 0; x <= (int)strlen(kmer_list); x++)
        {

            if (kmer_list[x] == (char)*temp_lmer)
            {
                printf("kmer list: %s \n", &kmer_list[x]);
                printf("temp lmer: %s \n", temp_lmer);
                counter_for_find++;

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

        free(temp_lmer);
    }

    printf("\n\n");

    // For Suffixes
    for (int i = 0; i < 4; i++)
    {
        printf("%s\n", "Starting Suffixes");
        char *temp_lmer;
        temp_lmer = (char *)calloc(29, sizeof(char));

        count++;

        for (int u = 0; u <= 28; u++)
        {
            strncat(temp_lmer, &kmer_list[u], 1);
        }
        printf("%s\n\n", temp_lmer); // prints kmer-1 appended ot prefix

        strncat(temp_lmer, &alpha[i], 1); // prints prefix
        printf("%s\n\n", temp_lmer);

        // See if the string has a match is the strings
        for (int x = 0; x <= (int)strlen(kmer_list); x++)
        {

            if (kmer_list[x] == (char)*temp_lmer)
            {
                 printf("kmer list: %s \n", &kmer_list[x]);
                 printf("temp lmer: %s \n", temp_lmer);
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
    }
    return 0;
}

