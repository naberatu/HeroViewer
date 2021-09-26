## Welcome to the HeroViewer!
The HeroViewer is a simple character creater and manager for tabletop games like Dungeons & Dragons.

## Download & Use Instructions: 
1) Download the HeroViewer.exe file. 
2) Create a folder and place the HeroViewer.exe file. 
3) Right-click on the HeroViewer.exe and select Send To --> Desktop Shortcut
4) Launch the desktop shortcut to begin using the program!

Software Features:
- Create a D&D character and set their name, alignment, race, class, level, etc.
- Set and edit your character's attribute scores and view instantly-updated stats.
- Instantly add, remove, and edit your character's abilities.
- Includes auto-saving, allowing you to pick up where you left off!
- Automatically adjusts window size to fit contents. Window is also resizeable.

<!-- Demo Image of Software -->
<image align="center" src="https://user-images.githubusercontent.com/39421939/134764748-3eb24877-a564-4eb5-8768-0ecc2996de03.png" height="400"> 


## Editing Name, Stats, etc... 
To edit values such as name or stats, simply double-click on the text field you wish to update. A text box will appear asking you to input the new string.
<!-- Demo Image of Software -->
<image align="center" src="https://user-images.githubusercontent.com/39421939/134764947-fd058899-4992-4565-bc7b-8f00d812650e.png" height="400">
When you're done, simply hit the "Submit" button to write the new changes. To cancel changes, simply close the textbox window instead.
  

## Level-Up
Two different appoaches exist to updating your character's level: 
- Manually editing the level using the double-click edit procedure outlined above.
- Clicking the "U" button next to the character's level.
Pressing the "U" button next to your character's level text box instantly increments their level by +1. Level cannot exceed 20 or fall under 1, which are the level bounds defined by D&D rules. Updating level immediately updates number of hit dice.


## Updating Race, Class, Alignment...
When updating fields such as your character's Race, Class, or Alignment, simply click on the respective field dropdown and select another option.
<!-- Demo Image of Software -->
<image align="center" src="https://user-images.githubusercontent.com/39421939/134782791-0dbe2304-bd1b-4827-a983-444d2596ae16.png" height="400">
Making a selection will immediately update the field. Selecting a new character class will immediately update the type of hit dice, while selecting a new character race will immediately update character speed.
  

## Selecting and Removing Features/Abilities...
Click on feature/ability in the "features" list to select it (highlight in blue) and display its description in the adjacent box.
<!-- Demo Image of Software -->
<image align="center" src="https://user-images.githubusercontent.com/39421939/134783128-178cff83-2570-44ed-b2cd-789df9c05131.png" height="400">

- Clicking the "-" button while a feature/ability is selected instantly removes that feature/ability from the list.
  

## Adding and Editing Features/Abilities...
You can either add new ability/feature by clicking the "+" button, or double-click on a feature/ability to select and edit that ability. Both actions will open the same "Edit Feature" window and ask for the same "Feat" and "Desc" fields.
<!-- Demo Image of Software -->
<image align="center" src="https://user-images.githubusercontent.com/39421939/134783129-37a57124-f8a5-4cdd-b208-9ccf1fc0f3d1.png" height="400">

After filling in the desired fields when either adding or editing a feature/ability, click "Submit" to write the changes. You could alternatively click "Cancel" or close the editing window to cancel the operation. 

- If you have chosen to add a feature/ability, it will instantly appear in the "features" list, while editing a feature/ability will automatically update the currently selection.
- When adding a feature the "description" field can be left blank, but a feature/ability name must be designated. Failure to designate a name will not submit/write the feature/ability.
- When editing a feature/ability, leaving one of the fields blank when submitting will not overwrite that field, allowing users to update a feature's/ability's name or description without having to update both. 

---  
Created using Python 3 with Tkinter.

Used the fonts [Hylia Serif by Artsy Omni] and [New Rocker by Pablo Impallari]

[Hylia Serif by Artsy Omni]: https://artsyomni.com/hyliaserif
[New Rocker by Pablo Impallari]: https://fonts.google.com/specimen/New+Rocker#standard-styles
