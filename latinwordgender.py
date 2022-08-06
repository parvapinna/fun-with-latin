# This code tells you the gender of any singular word in nominative form.

vocabulum = " "
vocabulum = input("Quaeso, singulari verbo intrare: ")

if vocabulum.endswith("s", len(vocabulum)-1):
    print(vocabulum.capitalize(), "est vocabulum masculinum.")
elif vocabulum.endswith("a", len(vocabulum)-1):
    print(vocabulum.capitalize(), "est vocabulum femininum.")
elif vocabulum.endswith("m", len(vocabulum)-1):
    print(vocabulum.capitalize(), "est vocabulum neutrum.")

else:
    print("Nullum verbum")
