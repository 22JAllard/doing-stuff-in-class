# Animal = Class
#   Public
#     Constructor (s, n)
#     Procedure feed()
#     Function getState()
#     Function getSize()
#   Private
#     state: String 
#     size: Integer

#   Animal.Constructor (s, n)
#     Animal.state 🡨 s
#     Animal.size 🡨 n
#   End Constructor

#   Procedure Animal.feed()
#     Animal.size 🡨 Animal.size + 1
#     If Animal.size = 5 Then
#       Animal.state 🡨 "FISH"
#     End If
#   End Procedure

#   Function Animal.getState()
#     Return Animal.state
#   End Function

#   Function Animal.getSize()
#     Return Animal.size
#   End Function

# End Class

class Animals:
    def __init__(self, s, n):
        self.state = s
        self.size = n

    def get_state(self):
        return self.state

    def get_size(self):
        return self.size
    
    def feed(self):
        self.size = self.size + 1
        print("Fish fed")
        if self.size == 5:
            self.state = self.state.upper()


# thisFish 🡨 new Animal("Fish", 1)
 
# Output thisFish.getState() 
# Output " is of size ", thisFish.getSize()

# While thisFish.getState() <> "FISH"
#    thisFish.feed()
# Endwhile

# Output "It is now a big " 
# Output thisFish.getState() 

thisfish = Animals("Fish", 1)

print(thisfish.get_state(), "is of size ", thisfish.get_size())

while thisfish.get_state() != "FISH":
    thisfish.feed()

print("It is now a big", thisfish.get_state())
