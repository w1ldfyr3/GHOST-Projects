#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main()
{
    char word[50];
    char pig_latin[54];
    const char *VOWELS = "AEIOUaeiou";

    printf("Type a word: ");
    if (scanf("%49s", word) != 1)

{
        printf("\nNo input.");
        return 1;

}

if (strchr(VOWELS, word[0]))

{
    snprintf(pig_latin, sizeof(pig_latin), "%sway", word);
}

else

{

    snprintf(pig_latin, sizeof(pig_latin), "%s%cay", word + 1, word[0]);

}

    printf("Pig Latin: %s\n", pig_latin);
    return 0;

}