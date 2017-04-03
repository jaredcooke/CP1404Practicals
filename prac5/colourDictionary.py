COLOURS = {"alice blue": "#f0f8ff", "beige": "#f5f5dc", "black": "#000000", "blue violet": "#8a2be2",
           "dark green": "#006400", "dark orange": "#ff8c00", "white": "#ffffff", "yellow": "#ffff00", "red": "#ff0000",
           "orange": "#ffa500", "green": "#00ff00"}
print("These are the available colours:\n{}".format(COLOURS.keys()))
colour = input("Please enter a colour: ")
while not colour.strip():
    colour = input("Please enter a colour from list: ")
found_code = False
while not found_code:
    if colour in COLOURS:
        print("The hexadecimal code for {} is {}".format(colour, COLOURS[colour.lower()]))
        found_code = True
    else:
        colour = input("Please enter a colour from list: ")