2.1

Toy:

Name       :STRING
ID         :STRING
Price      :FLOAT
MinimumAge :INTEGER

Constructor()
SetName()
SetID()
SetPrice()
SetMinimumAge()
GetName()
GetID()
GetPrice()
GetMinimumAge()
ComputerGame:

Category   :STRING
Console    :STRING

Constructor()
SetCategory()
SetConsole()
GetCategory()
GetConsole() 
Vehicle:

Type       :STRING 
Height     :FLOAT
Length     :FLOAT
Weight     :FLOAT

Constructor()
SetType()
SetHeight()
SetLength()
SetWeight()
GetType()
GetHeight()
GetLength()
GetWeight()

2.2



2.3

class Toy():
    def __init__(self, N,I,P,M):
        self.__Name= N
        self.__ID= I
        self.__Price= P
        self.__MinimumAge= M
    def SetName(self,N):
        self.__Name = N
    def SetID(self, I):
        self.__ID = I
    def SetPrice(self,P):
        self.__Price = P
    def SetMinimumAge(self,M):
        self.__MinimumAge = M
    def GetName(self):
        return(self.__Name)
    def GetID(self):
        return(self.__ID)
    def GetPrice(self):
        return(self.__Price)
    def GetMinimumAge(self):
        return(self.__MinimumAge)
    def PrintDetails(self):
        print('Name:',self.GetName())
        print('ID:',self.GetID())
        print('Price:',self.GetPrice())
        print('Minimum Age:', self.GetMinimumAge())
        print()

2.4

class ComputerGame(Toy):
    def __init__(self, N,I,P,M,Ca,Co):
        Toy.__init__(self, N,I,P,M)
        self.__Category = Ca
        self.__Console = Co
    def SetCategory(self,Ca):
        self.__Category = Ca
    def SetConsole(self,Co):
        self.__Console = Co
    def GetCategory(self):
        return(self.__Category)
    def GetConsole(self):
        return(self.__Console)
    def PrintDetails(self):
        print('Name:',self.GetName())
        print('ID:',self.GetID())
        print('Price:',self.GetPrice())
        print('Minimum Age:', self.GetMinimumAge())
        print('Category:',self.GetCategory())
        print('Console:', self.GetConsole())
        print()
    
class Vehicle(Toy):
    def __init__(self, N,I,P,M,T,H,L,W):
        Toy.__init__(self, N,I,P,M)
        self.__Type = T
        self.__Height = H
        self.__Length = L
        self.__Weight = W
    def SetType(self,T):
        self.__Type = T
    def SetHeight(self,H):
        self.__Height = H
    def SetLength(self,L):
        self.__Length
    def SetWeight(self,W):
        self.__Weight
    def GetType(self):
        return(self.__Type)
    def GetHeight(self):
        return(self.__Height)
    def GetLength(self):
        return(self.__Length)
    def GetWeight(self):
        return(self.__Weight)
    def PrintDetails(self):
        print('Name:',self.GetName())
        print('ID:',self.GetID())
        print('Price:',self.GetPrice())
        print('Minimum Age:', self.GetMinimumAge())
        print('Type:', self.GetType())
        print('Height:',self.GetHeight())
        print('Length:',self.GetLength())
        print('Weight:',self.GetWeight())
        print()

2.5

class User():
    def __init__(self, N, A):
        self.__Name = N
        self.__Age = A
    def SetUserName(self,N):
        self.__Name  = N
    def SetUserAge(self,A):
        while A<0 or A>18:
            A = input('please input valid age')
        self.__Age = A 
    def GetUserName(self):
        return(self.__Name)
    def GetUserAge(self):
        return(self.__Age)


2.6

A=Vehicle("red Sports Car", "RSC13", 15.00,6,"car",3.3,12.1,0.08)
B=ComputerGame("Roulette","RSC14", 300,10,"Casino", "Ps4")
C=Toy("JoyStick", "RSC15",100,6)
List=[A,B,C]

2.7

def searchID(I):
    for i in range(len(List)):
        if List[i].GetID()==I:
            List[i].PrintDetails()

2.8

def discount(d):
    d = 1 - d/100
    for i in range (len(List)):
        List[i].SetPrice(List[i].GetPrice()*d)

2.9 

A bubble sort changes the order of the list one item and another by comparing the two near once at a time.

A bubble sort goes from the start of the list to the end of the list.

A insertion sort does it by finding the approperiate position to insert the item.

A insertion sort goes from the back of the list to the start of the list.

2.10

def sort():
    for j in range(len(List)):
        for i in range(len(List)-1):
            if List[i].GetPrice()>List[i+1].GetPrice():
                temp= List[i]
                List[i]=List[i+1]
                List[i+1]=temp
