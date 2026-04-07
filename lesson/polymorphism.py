# polymorphism is many forms of a function or method. It allows us to use the same function name for different types of data.

class Instrument:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def play(self):
        print("Playing the instrument.")
        
class Guitar(Instrument):
    # overriding the play method of the Instrument class
    def play(self):
        print("Strumming the guitar.")

class Piano(Instrument):
    # overriding the play method of the Instrument class
    def play(self):
        print("Playing the piano.")
    
class Drums(Instrument):
    # overriding the play method of the Instrument class
    def play(self):
        print("Beating the drums.")
        
guitar = Guitar("Fender", "Stratocaster")
piano = Piano("Yamaha", "U3")
drums = Drums("Pearl", "Export")

# instrument = guitar
# instrument.play()  # Output: Strumming the guitar.

# instrument = piano
# instrument.play()  # Output: Playing the piano.

# instrument = drums
# instrument.play()  # Output: Beating the drums.

for instrument in (guitar, piano, drums):
    instrument.play()  # Output: Strumming the guitar. Playing the piano. Beating the drums.