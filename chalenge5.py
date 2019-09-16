# 1
fav_mv = ["Ed sheeran","eminem","Bump of chickin"]

print(fav_mv[1])

# 2

lists = []

yatugatake = (35.970 , 138.370)
hawaii = (36.994 , 140.815)

lists.append(yatugatake)
lists.append(hawaii)

print(lists)

# 3 4

my_info = {"height": 175.5, "heir": "black", "national":"japan"}

key = input("何が知りたい？：")

answer = my_info[key]

print(answer)

# 5

arbum = {
    "Ed sheeran":[
        "perfect",
        "cathle on the hill",
        "shape of you"
        ]
    }

print(arbum["Ed sheeran"])

# 6

loc1 = set(["oosaka","oosaka","tokyo"])

loc2 = set(["okinawa","sasebo","oosaka"])

print(loc1)
print(loc2)

loc1.add("okinawa")

# 和集合

c = loc1 | loc2
print(c)

# 集合隻
d = loc1 & loc2
print(d)
