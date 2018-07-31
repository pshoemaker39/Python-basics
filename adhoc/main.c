#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "info.h"




/* comments */
// comment

int main() {
    
    // conversion characters
    // %s : string
    // %d : integer
    // %f : float
    printf("%s %d %f %.2f \n", "Hello World", 100, 3.14999, 3.14999);

    int age;
    int currentYear;
    int birthYear;

    currentYear = 2018;
    birthYear = 1987;

    age = currentYear-birthYear;

    printf("Age: %d \n", age);


    char name[] = "Price Shoemaker";
    strcpy(name, "Stuff");

    printf("Name: %s %d \n", MYNAME, MYAGE);

    char firstName[21];
    char otherName[21];
    int number;

    printf("What is your name? \n");
    scanf("%s", firstName);

    printf("What is other name? \n");
    scanf("%s", otherName); 

    printf("Number? \n");
    scanf("%d", &number);

    printf("%s %s %d \n", firstName, otherName, number);

    return 0;
}