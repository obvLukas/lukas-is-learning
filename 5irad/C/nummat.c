#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

int ** makeMat(FILE *fil, int nrows, int ncols){
  int ** matris = malloc(sizeof(int*) * nrows);
  for(int i = 0; i<nrows; i++) {
    matris[i] = malloc(sizeof(int) * ncols);
    for(int j = 0; j<ncols; j++){
      int x = 0;
      fscanf(fil, "%d", &x);
      *(*(matris+i) + j) = x;
    }
  }
  return matris;
}

void printMat(int **matris, int rows, int cols){
  for(int i = 0; i<rows; i++){
    for(int j = 0; j<cols; j++){
      printf("\nMat[%d][%d]: %d\n", i, j, *(*(matris+i) + j));
    }
  }
}

int main(){
  printf("\n Läser fil... \n");
  FILE * fil = fopen("mat.txt", "r");
  int rows, cols;

  fscanf(fil, "%d", &rows);
  fscanf(fil, "%d", &cols);

  printf("Rows: %d, Cols: %d\n\n", rows, cols);
  int ** matris;
  matris = makeMat(fil, rows, cols);
  printMat(matris, rows, cols);
}
