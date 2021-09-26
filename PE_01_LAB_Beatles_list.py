# Beatles list has been created.
beatles=[]
print("Step 1:", beatles)

# 3 memmbers have been added to Beatles.
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# User type 2 extra members.
for i in range(2):
    beatles.append(input("Name:"))
print("Step 3:", beatles)

# Remove the last 2 members.
del beatles[-1]
del beatles[-1]
print("Step 4:", beatles)

# Add Ringo Star
beatles.insert(3,"Ringo Starr")
print("Step 5:", beatles)


# Print out the listlenght.
print("The Fab", len(beatles))
