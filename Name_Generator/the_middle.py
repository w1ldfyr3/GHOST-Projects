"""A script to randomly choose silly names with optional middle names."""

import random


def main():
    """Main function to generate silly names."""
    first = (
        'Baby Oil', 'Bad News', 'Big Burps', 'Bill', 'Bob',
        'Bowel Noises', 'Boxelder', 'Bud', 'Butterbean', 'Buttermilk',
        'Buttocks', 'Chad', 'Chesterfield', 'Chewy', 'Chigger', 'Cinnabuns',
        'Cleet', 'Cornbread', 'Crab Meat', 'Crapps', 'Dark Skies',
        'Dennis Clawhammer', 'Dicman', 'Elphonso', 'Fancypants', 'Figgs',
        'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry', 'Huggy', 'Ignatious',
        'Jimbo', 'Joe', 'Johnny', 'Lemongrass', 'Lil Debil', 'Longbranch',
        'Lunch Money', 'Mergatroid', 'Mr Peabody', 'Oinks', 'Old Scratch',
        'Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
        'Pushmeet', 'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut', 'Sid',
        'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan Sam',
        'Spitzitout', 'Squids', 'Stinky', 'Storyboard', 'Sweet Tea', 'TeeTee',
        'Wheezy Joe', 'Winston', 'Worms'
    )

    middle = (
        'Pottin Soil', 'The Squirts', 'Jazz Hands', 'Lite',
        'Oil Can', 'The Big News', 'Grunts', 'Tinkie Winkie',
        'The Tornado', 'The Menace'
    )

    last = (
        'Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom', 'Breedslovetrout',
        'Butterbaugh', 'Clovenhoof', 'Clutterbuck', 'Cocktoasten', 'Endicott',
        'Fewhairs', 'Gooberdapple', 'Goodensmith', 'Goodpasture', 'Guster',
        'Henderson', 'Hooperbag', 'Hoosenater', 'Hootkins', 'Jefferson',
        'Jenkins', 'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee',
        "M'Bembo", 'McFadden', 'Moonshine', 'Nettles', 'Noseworthy', 'Olivetti',
        'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler', 'Pealike',
        'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton', 'Porkins', 'Putney',
        'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins', 'Sackrider',
        'Snuggleshine', 'Splern', 'Stevens', 'Stroganoff', 'Sugar-Gold',
        'Swackhamer', 'Tippins', 'Turnipseed', 'Vinaigrette', 'Walkingstick',
        'Wallbanger', 'Weewax', 'Weiners', 'Whipkey', 'Wigglesworth',
        'Wimplesnatch', 'Winterkorn', 'Woolysocks'
    )

    # Step 4: Main loop
    while True:
        first_name = random.choice(first)
        last_name = random.choice(last)

        # decide whether to include a middle name
        if random.random() < 0.5:
            middle_name = random.choice(middle)
            full_name = f"{first_name} '{middle_name}' {last_name}"
        else:
            full_name = f"{first_name} {last_name}"

        print(f"\nName = {full_name}")

        try_again = input("\nTry again? (Press Enter else n to quit): ")
        if try_again.lower() == "n":
            break

if __name__ == "__main__":
    main()
