#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
int main(void)
{
    // Initialize random seed
    srand((unsigned int)time(NULL));

    const char *first[] = {
        "Baby Oil", "Bad News", "Big Burps", "Bill 'Beenie-Weenie'",
        "Bob 'Stinkbug'", "Bowel Noises", "Boxelder", "Bud 'Lite'",
        "Butterbean", "Buttermilk", "Buttocks", "Chad", "Chesterfield",
        "Chewy", "Chigger", "Cinnabuns", "Cleet", "Cornbread", "Crab Meat",
        "Crapps", "Dark Skies", "Dennis Clawhammer", "Dicman", "Elphonso",
        "Fancypants", "Figgs", "Foncy", "Gootsy", "Greasy Jim", "Huckleberry",
        "Huggy", "Ignatious", "Jimbo", "Joe 'Pottin Soil'", "Johnny",
        "Lemongrass", "Lil Debil", "Longbranch", "Lunch Money",
        "Mergatroid", "Mr Peabody", "Oil-Can", "Oinks", "Old Scratch",
        "Ovaltine", "Pennywhistle", "Pitchfork Ben", "Potato Bug",
        "Pushmeet", "Rock Candy", "Schlomo", "Scratchensniff", "Scut",
        "Sid 'The Squirts'", "Skidmark", "Slaps", "Snakes", "Snoobs",
        "Snorki", "Soupcan Sam", "Spitzitout", "Squids", "Stinky",
        "Storyboard", "Sweet Tea", "TeeTee", "Wheezy Joe",
        "Winston 'Jazz Hands'", "Worms"
    };

    const char *last[] = {
        "Appleyard", "Bigmeat", "Bloominshine", "Boogerbottom",
        "Breedslovetrout", "Butterbaugh", "Clovenhoof", "Clutterbuck",
        "Cocktoasten", "Endicott", "Fewhairs", "Gooberdapple", "Goodensmith",
        "Goodpasture", "Guster", "Henderson", "Hooperbag", "Hoosenater",
        "Hootkins", "Jefferson", "Jenkins", "Jingley-Schmidt", "Johnson",
        "Kingfish", "Listenbee", "M'Bembo", "McFadden", "Moonshine",
        "Nettles", "Noseworthy", "Olivetti", "Outerbridge", "Overpeck",
        "Overturf", "Oxhandler", "Pealike", "Pennywhistle", "Peterson",
        "Pieplow", "Pinkerton", "Porkins", "Putney", "Quakenbush",
        "Rainwater", "Rosenthal", "Rubbins", "Sackrider", "Snuggleshine",
        "Splern", "Stevens", "Stroganoff", "Sugar-Gold", "Swackhamer",
        "Tippins", "Turnipseed", "Vinaigrette", "Walkingstick", "Wallbanger",
        "Weewax", "Weiners", "Whipkey", "Wigglesworth", "Wimplesnatch",
        "Winterkorn", "Woolysocks"
    };

    int first_count = sizeof(first) / sizeof(first[0]);
    int last_count = sizeof(last) / sizeof(last[0]);

    char input [10];
    // Main loop

while (1) {
    const char *firstName = first[rand() % first_count];
    const char *lastName = last[rand() % last_count];

    fprintf(stderr, "\nName = %s %s\n", firstName, lastName);

    printf("Try again? (press Enter or type 'n' to quit): ");
    if (fgets(input, sizeof(input), stdin) != NULL) {
        if (input[0] == 'n' || input[0] == 'N')
        break;
    }
    }

    printf("Goodbye!\n");
}

