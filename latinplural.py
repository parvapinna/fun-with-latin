# This code converts the singular nominative form of any Latin word to its plural nominative form.

vocabulum = " "
vocabulum = input("Quaeso, singulari verbo intrare: ")

if vocabulum.endswith("us", len(vocabulum)-2):
    print((vocabulum.replace("us", "i")))
elif vocabulum.endswith("a", len(vocabulum)-1):
    print((vocabulum.replace("a", "ae")))
elif vocabulum.endswith("um", len(vocabulum)-2):
    print((vocabulum.replace("um", "a")))

else:
    print("Nullum verbum")
