"""
Intermediate Exercise
"""

COLOUR_CODES = {"AliceBlue": "#f0f8ff", "Azure1": "#f0fffff",
                "Beige": "#f5f5dc", "Bisque1": "#ffe4c4",
                "Black": "#000000", "Brown": "#a52a2a",
                "Burlywood": "#deb887", "BlueViolet": "#8a2be2",
                "CadetBlue": "#5f9ea0", "Chocolate": "#d2691e",
                "DimGray": "#696969", "DodgerBlue1": "#1e90ff", "FloralWhite": "#fffaf0",
                "FireBrick": "#b22222", "Gold1": "#ffd700"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name,
                                             COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")
