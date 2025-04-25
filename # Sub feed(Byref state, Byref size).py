# Sub feed(Byref state, Byref size)
#    size 🡨 size + 1
#    Output "Fish fed" 
#    If size = 5 Then 
#       state 🡨 "FISH" 
#    End If
# End Sub

# thisFishState 🡨 "Fish" 
# thisFishSize 🡨 1
# Output thisFishState, " is of size ", thisFishSize
# While thisFishState <> "FISH"
#    feed(thisFishState, thisFishSize)
# Endwhile
# Output "It is now a big ", thisFishState

def feed(state, size):
    size = size + 1
    print ("Fish fed")
    if size == 5:
        state = "FISH"
    return state, size

thisfishstate = "Fish"
thisfishsize = 1
print(thisfishstate, "is of size ", thisfishsize)
while thisfishstate != "FISH":
    thisfishstate, thisfishsize = feed(thisfishstate, thisfishsize)
print("It is now a big ", thisfishstate)