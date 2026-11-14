# This is unpacking in python.
# Nothing  really complicated here.
favorite_snacks = {
    "salty": ("pretzels", 100),
    "sweet": ("cookies", 180),
    "veggie": ("carrots", 20),
}
((type1, (name1, cals1)), (type2, (name2, cals2)), (type3, (name3, cals3))) = (
    favorite_snacks.items()
)
print(f"Favorite {type1} is {name1} with {cals1} calories")
print(f"Favorite {type2} is {name2} with {cals2} calories")
print(f"Favorite {type3} is {name3} with {cals3} calories")

print()


def bubble_sort(a):
    for j in range(len(a)):
        for i in range(1, len(a) - j):
            # Interesting way to swap.
            # The right side of assignment becomes
            # a temporary tuple till assignment
            # completes.
            a[i], a[i - 1] = a[i - 1], a[i]


names = ["pretzels", "carrots", "arugula", "bacon"]
bubble_sort(names)
print(names)

print()

snacks = [("bacon", 350), ("donut", 240), ("muffin", 190)]
# Normal way:
print("Normal way")
for i in range(len(snacks)):
    item = snacks[i]
    name = item[0]
    calories = item[1]
    print(f"#{i + 1}: {name} has {calories} calories")


# Pythonic way:
print("Pythonic way")
for i, (name, calories) in enumerate(snacks):
    print(f"#{i + 1}: {name} has {calories} calories")
