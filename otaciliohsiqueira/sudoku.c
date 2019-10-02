#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>

#define TAM 9
#define L 9
#define C 9


int global = 0;


int sudoku [L][C] =     {6, 2, 4, 5, 3, 9, 1, 8, 7,      //Sudoku Válido
			 5, 1, 9, 7, 2, 8, 6, 3, 4,
			 8, 3, 7, 6, 1, 4, 2, 9, 5,
			 1, 4, 3, 8, 6, 5, 7, 2, 9,
			 9, 5, 8, 2, 4, 7, 3, 6, 1,
			 7, 6, 2, 3, 9, 1, 4, 5, 8,
			 3, 7, 1, 9, 5, 6, 8, 4, 2,
			 4, 9, 6, 1, 8, 2, 5, 7, 3,
		         2, 8, 5, 4, 7, 3, 9, 1, 6};

/*int sudoku [L][C] =     {6, 2, 3, 5, 3, 9, 1, 8, 7,     //Sudoku Inválido
						 5, 1, 4, 7, 2, 8, 6, 3, 4,
						 8, 3, 7, 6, 1, 1, 2, 9, 5,
						 1, 4, 3, 5, 2, 5, 7, 2, 9,
						 9, 5, 8, 2, 4, 7, 3, 6, 1,
						 7, 6, 2, 2, 9, 1, 4, 5, 8,
						 3, 7, 1, 9, 6, 6, 1, 4, 2,
						 4, 9, 6, 1, 8, 2, 5, 7, 3,
						 2, 8, 5, 4, 7, 3, 1, 1, 6};*/


int imprimir() {
	for (int i = 0; i < 9; i++) {

		for (int j = 0; j < 9; j++) {

			printf(" %d", sudoku[i][j]);
		}
		printf("\n");
	}
	return 0;
}

int validacao(int list[]) {

	int count = 0;int pro = 1;

	for (int i = 0; i < TAM; i++) {
		count = count + list[i];
	}
	
	for (int x = 0; x < TAM; x++) {
		pro = pro * list[x];
	}

	if(count == 45 && pro == 362880) {
		return 1;
	}
	else {
		return 0;
	}
}

void *check_linha(void *arg) {

	int auxline[10];
	int va = 0;
	int c = 0;
	int i = 0, j = 0;


	for (int i = 0; i < 9;i++) {
		for (int j = 0; j < 9;j++) {
			auxline[c] = sudoku[i][j];
			c++;
			
		}
		if(validacao(auxline) == 1) {
			printf("\nLinha %d Valida!", i+1);


		}
		else {
			printf("\nLinha %d Invalida -> Sudoku Invalidado", i+1);
		}
		c = 0;
	}
	printf("\n");
	return NULL;
}

void *check_coluna(void *arg) {

	int auxcol[10];
	int va = 0;
	int c = 0;
	int i = 0, j = 0;


	for (j = 0; j < TAM; j++) {
		for (i = 0; i < TAM; i++) {
			auxcol[c] = sudoku[i][j];
			c++;
		}
		if(validacao(auxcol) == 1) {
			printf("\nColuna %d Valida!", j+1);
		}
		else {
			printf("\nColuna %d Invalida -> Sudoku Invalidado", j+1);
		
		}
		c = 0;
	}
	printf("\n");
	return NULL;
}

void *check_box(void *arg) {

	int auxbox[10];
	int va;
	int i = 0; int j = 0;
	int y = 0; int x = 0;
	int c = 0;

	int temp_lin, temp_col;

	temp_lin = 3 * i;
	temp_col = 3 * j;
	int valida[10] = {0};

	for (int i = 0; i < 3; i++) {

		for (int j = 0; j < 3; j++) {

			for(int y = temp_lin; y < temp_lin+3; y++) {
				
				for(int x = temp_col; x < temp_col+3; x++) {
					auxbox[c] = sudoku[y][x];
					c++;
					
					while(c == 9){

					if(validacao(auxbox) == 1) {
						
						printf("\nSub-Box Valida!");
						va++;
					}
					else {
						
						printf("\nSub-Box Invalida -> Sudoku Invalidado");
					}
					c = 0;
					printf("%d\n", va);
					}
				}	
			}
		}
	}
	return NULL;
}

int main() {

	pthread_t t_linha, t_coluna, t_box;

	imprimir();
	 
	printf("\nInit Thread\n"); 
	
	//Create Threads  

	pthread_create(&t_linha, NULL, check_linha, (void *) &t_linha);
	pthread_create(&t_coluna, NULL, check_coluna, (void *) &t_coluna);
	pthread_create(&t_box, NULL, check_box, (void *) &t_box); 
	
	//Wait Threads

	pthread_join(t_linha, NULL);
	pthread_join(t_coluna, NULL);
	pthread_join(t_box, NULL); 
	

	printf("\n\nEnd Thread\n");

	exit(0); 

	return 0;
}