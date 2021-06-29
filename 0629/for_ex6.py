print("##1##")
for i in range(5):
    for j in range(5):
        print("*",end="")
    print()

print("##2##")
for i in range(5):
    for j in range(6,5-i,-1):
        print("*",end="")
    print()

print("##3##")
for i in range(5):
    for j in range(i,5):
        print("*",end="")
    print()

print("##4##")
