# this program should help in searching for specific characters in the lines of the mbox-short.txt file
# first of all we open the file
fhandle = open("mbox-short.txt")
# the input/search bar where you enter the name of the person you want to search
x = input("who are you looking for,")
# then the for loop for reading through the file.
for line in fhandle:
    # we set x as the item we need to find in the file's lines.
    if not x in line:
        # the .strip strips the space.
        line = line.rstrip()
        # the continue will skip all the lines without the name
        continue
    # then we print the output.
    print(line)
