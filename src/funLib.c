# include <stdlib.h>
# include <stdint.h>
# include <string.h>

uint64_t getSum(int64_t * arr, uint32_t size){
  uint64_t sum = 0;
  for (uint32_t i = 0; i != size; ++i){
    sum += arr[i];
  }
  return sum;
} 
