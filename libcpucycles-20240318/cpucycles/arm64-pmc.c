// version 20230105
// public domain
// djb
// adapted from supercop/cpucycles/armv8.c

#include "cpucycles_internal.h"

long long ticks(void)
{
  long long result;
  asm volatile("mrs %0, PMCCNTR_EL0" : "=r" (result));
  return result;
}

long long ticks_setup(void)
{
  if (!cpucycles_works(ticks)) return cpucycles_SKIP;
  return cpucycles_CYCLECOUNTER;
}
