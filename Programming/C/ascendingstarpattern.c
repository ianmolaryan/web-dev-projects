#include <stdio.h>

int main() {
    int i, j, rows;

    // Ask user for number of rows
    printf("Enter the number of rows: ");
    scanf("%d", &rows);

    // Loop through rows
    for (i = 1; i <= rows; i++) {
        // Loop to print stars in each row
        for (j = 1; j <= i; j++) {
            printf("*");
        }
        // Move to the next line after printing stars
        printf("\n");
    }

    return 0;
}
