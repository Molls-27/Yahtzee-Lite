import easygui, random

dice = []
i = 0
roll = 0

while i < 5:
    dice.append(random.randint(1,6))
    i += 1

easygui.msgbox(f"You rolled:\n{dice[0:5]}")
if len(set(dice)) == 1:
    easygui.msgbox("Yahtzee")
if len(set(dice)) == 2:
    easygui.msgbox("Four of a kind")
if len(set(dice)) == 3:
    easygui.msgbox("Three of a kind")

choice=easygui.buttonbox("Choose", choices=["Stick", "Roll Again"])

while choice == "Roll Again":
    if roll == 2:
        easygui.msgbox("You've ran out of rolls!\nThanks for playing")
        break
    
    roll += 1
    i = 0
    dice= []

    while i < 5:
        dice.append(random.randint(1,6))
        i += 1

    easygui.msgbox(f"You rolled:\n{dice[0:5]}")
    if len(set(dice)) == 1:
        easygui.msgbox("Yahtzee")
    elif len(set(dice)) == 2:
        easygui.msgbox("Four of a kind")
    elif len(set(dice)) == 3:
        easygui.msgbox("Three of a kind")
    choice=easygui.buttonbox("Choose", choices=["Stick", "Roll Again"])
    
    if choice == "Stick":
        break