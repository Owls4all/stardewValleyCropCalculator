# stardewValleyCropCalculator
Primarily a nicer UI than the spreadsheet I was using for this purpose previously.

I wanted to be able to calculate how many of what type of seed I should get for my farm, depending on season and progress through the game.
This is my endeavor to create a UI that makes it easy.

So it has checkboxes for things like whether it's year 2+, if you can go to the desert, or the island etc, as well as what season it is.
Depending on whether you are money-limited or space-limited, it will calculate (based on a given budget and # of sprinklers) what to buy.
It assumes that you will try to plant the minimum of each thing required for perfection (excluding community center, because I like to play with remixed bundles)
so for instance you'd need 12 beet seeds, 1 for cooking, 1 to ship, and 10 for the quest.

It has a list of all the plantable crops on the right side, and on the left is the "fill the remaining space with the best one" calculations.
It takes the amount of space you have, the amount of space used by other things, the amount of budget available, etc. into account to tell you what fraction of your space to fill with your best vs. second best crop.

Right now there's a bit of an issue displaying the full list of crops when you choose "Island/greenhouse" for the season (because it is too long to fit in the window) but I hope to patch that soon.
