#include <stdio.h>

int main()
{
char	word[80];
int	i,j;

printf("Enter a word: ");
scanf("%s", word);
i=0;
while (word[i] != '\0')
 {
  if (word[i] == word[i+1])
   {
   j=1;
   while (word[i] == word[i+j])
     j++;
    printf("%d consectuvie %c\n",j,word[i]);
    }
    i++;
   }
 return 0;
 }
