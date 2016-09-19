def cipher(toChange, shift):
    new = ""
    if shift > 0:
        value = -1
    else:
        value = 1
        
    for i in toChange:
        if i.isalpha():
            if -26 < shift < 26:
                if ((ord(i) + shift) < 65 and ord(i) > 64) or ((ord(i) + shift) < 97 and ord(i) > 96) or ((ord(i) < 91 and (ord(i) + shift) > 90) or ((96 < ord(i) < 123) and (ord(i) + shift) > 122)):
                    y = ord(i) + (value * (26 + (value * shift)))
                    new = new + chr(x)
                else:
                    x = ord(i) + shift
                    new = new + chr(x)
            else:
                new = "The shift must be greater than -26 and less than 26! Your shift was: " + str(shift)
        else:
            new = new + i
    print new

cipher("the quick brown fox jumps over the lazy dog", 1)
cipher("uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph", -1)
print ""
cipher("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", 1)
print ""
cipher("ThE qUIcK BrowN fOx jUMPs oVeR THe lAzY Dog", 1)
print ""











