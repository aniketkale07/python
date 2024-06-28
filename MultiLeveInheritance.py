# MultiLevel Inheritance

class GrandFather:
    def __init__(self) -> None:
        print("Is GrandFather Here :")

class Father(GrandFather):
    def __init__(self) -> None:
        super().__init__()
        print("Is Father Here :")
        
class Son(Father):
    def __init__(self) -> None:
        super().__init__()
        print("Is Son is Here :")
        
s=Son()

# Diamond Problem 
print("\n---------------------------------------\nDiamond Proble")

class GrandFather:
    def __init__(self) -> None:
        print("Is GrandFather is Here :")
        
class Father(GrandFather):
    def __init__(self) -> None:
        super().__init__()
        print("Is Father is Here :")

class Mother(GrandFather):
    def __init__(self) -> None:
        super().__init__()
        print("Is Mother is Here :")

class Daughter(Father, Mother):
    def __init__(self) -> None:
        super().__init__()
        print("is Daughter Here")

d=Daughter()

#operator OverLoading----------->

print("\n---------------------------------------\nOperator Overloading")

a=23
b=44

print(a+b)


s1,s2 = "Aniket", " Kale"
print(s1+s2)

a = [11,10]
b=[30,30]
print(a+b)