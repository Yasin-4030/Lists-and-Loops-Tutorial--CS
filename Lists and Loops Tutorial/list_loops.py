songs = ["ROCKSTAR", "Do It", "For The Night"]

print(songs[0])
print(songs[-1])

print(songs[1:3])
# .............................................................

songs[-1] = "Despacito"
print(songs)
#...............................................................

songs.extend(["Hotline Bling", "God's Plan", "Caribbean Queen"])
print(songs)

# songs.remove("Do It")
del songs[1]
print(songs)
# ..............................................................

# for songs in songs:
#     print(songs)

# for i in range(len(songs)):
#    print(songs[i])
print()
# ..............................................................

animals = ["Rabbit", "Horse", "Panda"]
print(animals)
animals.append("Harambe")
print(animals)
print(animals[2])
del animals[0]
print(animals)

for animals in animals:
    print(animals)
