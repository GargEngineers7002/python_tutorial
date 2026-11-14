from urllib.parse import parse_qs

my_vals = parse_qs("red=5&blue=0&green=", keep_blank_values=True)

print(repr(my_vals))

# So this is very complicated and
# takes a lot of time to read and understand.
red = int(my_vals.get("red", [""])[0] or 0)
print(red)

# Better
green_str = my_vals.get("green", [""])[0]
green = int(green_str) if green_str else 0
print(green)


# Best
def get_first_int(values, key, default=0):
    found = values.get(key, [""])
    if found[0]:
        return int(found[0])
    return default


print(get_first_int(my_vals, "oppa"))
