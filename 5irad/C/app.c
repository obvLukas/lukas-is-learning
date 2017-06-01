#include <stdio.h>
#include <stdlib.h>

char ** makeMat(FILE *fil, int nrows, int ncols){
  char ** matris = malloc(sizeof(char*) * nrows);
  for(int i = 0; i<nrows; i++) {
    matris[i] = malloc(sizeof(char) * ncols);
    for(int j = 0; j<ncols; j++){
      char x;
      fscanf(fil, "%c\t", &x);
      *(*(matris+i) + j) = x;
    }
  }
  return matris;
}

void printMat(char **matris, int rows, int cols){
  for(int i = 0; i<rows; i++){
    for(int j = 0; j<cols; j++){
      printf("\nMat[%d][%d]: %c\n", i, j, *(*(matris+i) + j));
    }
  }
}

void checkRows(char **mat, int row, int col, int n_in_row, char symb){
  int count = 0;
  for(int i = 0; i<row; i++){
//DBG    printf("\nScanning Row: %d\n", i);
    for(int j = 0; j<=col; j++){
//DBG      printf("\n%d: %c\n", j, *(*(mat+i)+j));
      if(*(*(mat+i) + j) == symb){
        count++;
        if(count == n_in_row){
          printf("\nThere is %d in a row in row %d!!!!\n", n_in_row, i+1);
          return;
        }
      }
      else{
        count = 0;
      }
    }
  }
  printf("\nThere is not %d in a row in any of the rows...\n", n_in_row);
}

void checkCols(char **mat, int row, int col, int n_in_row, char symb){
  int count = 0;
  for(int i = 0; i<col; i++){
//DBG    printf("\nScanning Row: %d\n", i);
    for(int j = 0; j<row; j++){
//DBG      printf("\n%d: %c\n", j, *(*(mat+i)+j));
      if(*(*(mat+j) + i) == symb){
        count++;
        if(count == n_in_row){
          printf("\nThere is %d in a row in column %d!!!!\n", n_in_row, i+1);
          return;
        }
      }
      else{
        count = 0;
      }
    }
  }
  printf("\nThere is not %d in a row in any of the columns...\n", n_in_row);
}

int leastOf(int rows, int cols){
  if(rows < cols){
    return rows;
  }
  else{
    return cols;
  }
}


void checkDiag(char **mat, int row, int col, int n_in_row, char symb, int start_ind_i, int start_ind_j){
  int count = 1;
  for(int j = 0; j<leastOf(row-start_ind_i, col-start_ind_j); j++){
    if((*(*(mat + j + start_ind_i) + j + start_ind_j)) == symb){
//DBG        printf("\nTEST: %c,  i = %d,   j = %d\n", (*(*(mat + j + start_ind_i) + j + start_ind_j)), j + start_ind_i, j + start_ind_j);
      count++;
      }
    else{
      count = 0;
    }
    if(count == n_in_row){
      printf("\nThere is %d in a row in a diagonal!!!!\n", n_in_row);
      return;
      }
    }
  printf("\nThere is not %d in a row in any of the down-diagonals...\n", n_in_row);
}




int main(){
  printf("\n Läser fil... \n");
  FILE * fil = fopen("mat2.txt", "r");
  int rows, cols;

  fscanf(fil, "%d\n", &rows);
  fscanf(fil, "%d\n", &cols);

  printf("Rows: %d, Cols: %d\n\n", rows, cols);
  char ** matris;
  matris = makeMat(fil, rows, cols);
  //printMat(matris, rows, cols);
  checkRows(matris, rows, cols, 5, 'X');
  checkCols(matris, rows, cols, 5, 'X');
  checkDiag(matris, rows, cols, 5, 'X', 0, 0);
}
