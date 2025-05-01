# Animal = Class
#   Protected
#     state: String 
#     size: Integer
#   Public
#     Constructor(s, n)
#       state 🡨 s
#       size 🡨 n
#     End Constructor

#     Procedure feed()
#       size 🡨 size + 1
#       Output state, " fed"
#     End Procedure

#     Function getState()
#       Return state
#     End Function

#     Function getSize()
#       Return size
#     End Function
# End Class

# Fish = SubClass(Animal)
#   Private
#     maxSize : Integer
#   Public
#     Constructor(s)
#       Animal.Constructor(s, 1)
#       maxSize = 2
#     End Constructor

#     Procedure setMaxSize(m)
#       maxSize 🡨 m
#     End Procedure

#     Procedure feed Override
#       size += 2
#       Output state, " fed"
#       If size >= maxSize Then
#         state 🡨 "BIG FISH"
#       End If
#     End Procedure
# End Class

# Duck = Subclass(Animal)
#   Public
#     Procedure feed Override
#       Animal.feed()
#       If size = 5 Then
#         state 🡨 "BIG DUCK" 
#       End If
#     End Procedure
# End Class

# thisFish 🡨 new Fish("little fish", 1)
# thisFish.setMaxSize(3)
# thisDuck 🡨 new Duck("little duck", 1)
# For count 🡨 1 To 3
#   thisDuck.feed()
#   Output(thisDuck.getState())
#   thisFish.feed()
#   Output(thisFish.getState())
# End For

class Animal():
    def __init__(self, s, n):
        self.s = s #state
        self.n = n #size

    def feed(self):
        self.n += 1
        print(self.s, "Fed")

    def get_state(self):
        return self.s

    def get_size(self):
        return self.n

class Fish(Animal):
    def __init__(self, s, n):
        self.max_size = 2
        super().__init__(s, n)
    
    def set_max_size(self, m):
        self.max_size = m
    
    def feed(self):
        self.n += 2
        print(self.s, "Fed")
        if self.n >= self.max_size:
            self.s = "BIG FISH"

class Duck(Animal):
    def __init__(self, s, n):
        super().__init__(s,n)
    
    def feed(self):
        if self.n == 5:
            self.s = "BIG DUCK"

thisfish = Fish("little fish", 1)
thisfish.set_max_size(3)
thisduck = Duck("little duck", 1)
for i in range(3):
    thisduck.feed()
    print(thisduck.get_state())
    thisfish.feed()
    print(thisfish.get_state())
