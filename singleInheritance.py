# Single Inheritance

class Base:
    def __init__(self) -> None:
        print("This is the Addition of two number : ",5+5)
            
class Derived(Base):
    def __init__(self) -> None:
        super().__init__()
        print("THis is the derived : ")
        
        

a=Derived()
