# D&D 3.5e Character Generator

##Introduction

I am an avid fan of Dungeons and Dragons and an aspiring Dungeon Master.  Over my years of playing I have come to the realization that the character creation process just takes too long sometimes.  Character creation is a very detailed process that includes rolling up an ability score array, choosing a class and race, assigning ability scores, calculating hit points and saving throws, choosing feats, picking spells or powers (if playing a spellcaster or psionic) and allocating skill points.  Doing all of this can take up a sizeable chunk of time, especially if you do not have an idea of what you want going it.  The idea behind this project was that I wanted something that could be used to take care of most of the character creation process for me in a very short amount of time or when I needed to create a character on the fly.  This application handles ability score generation, race and class selection, ability score assignment and modification based on race and class value, generation of starting hit points, saving throw modifiers, and skill points, and will even generate a name for the character.  I have included every race and class I could find in the books as well as the option to use homemade classes and races to allow for maximum diversity.

##Instructions

**NOTE: Both .py files must be saved into the same folder for this application to work correctly.**
* Once the application is launched it will prompt the user with a series of four yes or no questions.  To respond to a question with yes, simply enter a y (non case sensitive) then press enter.  Doing anything else will be treated as a no.  **When prompted about using Homebrew (homemade) races or classes you will have to have first ran the HomebrewInstaller.py file**
![alt tex](https://github.com/JosephMoses/D-D/blob/master/First%20Two%20Prompts.png "First and Second Promtp")
* After answering all of the prompts, the application will display the newly generated character to the user and ask the user if they wish to save the character.  This question is answered the same was as the previous ones though a yes answer will prompt the user to supply the name of the .txt file they wish to save the character to.
![alt tex](https://github.com/JosephMoses/D-D/blob/master/FinalPrompt.png "Saving Character display")
* When the HombrewInstaller application is launched it will ask the user to enter class if they are adding a new homebrew class or race for a new homebrew race.  The answer to this question is case specific and must be answered in all lower case letters.  Once you have entered the type of homebrew you wish to install the installer will prompt you with several more questions, each with on screen instructions about how to answer them.  If no instructions are given, simply answer with numeric characters.
![alt text](https://github.com/JosephMoses/D-D/blob/master/HomebrewClassPrompts.png "Homebrew Class installation Prompts")
![alt text](https://github.com/JosephMoses/D-D/blob/master/HomebrewRacePrompts.png "Homebrew Race Installation Prompts")

##Notes

This application is actually the second version of this concept.  Originally it depended heavily on text files for everything but I decide to include as much information into the program itself as I could in an attempt to further develop my skills as a programmer.  Now whenever I learn a new programming language I try to convert this application into the new code as a means of helping me familiarize myself with that language.  I am currently working on converting this into Java.
