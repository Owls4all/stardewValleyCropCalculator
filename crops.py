from tkinter import *
from tkinter import ttk

class crop: #make the class
    def __init__(self,season,sources,cost,minimum,name,parent,i):
        self.season = season
        self.sources = sources
        self.cost = cost
        self.minimum = minimum
        self.name = name
        self.have = StringVar(value='0')
        self.buy = StringVar(value=str(self.minimum))
        self.show = False

        self.frame = ttk.Frame(parent, padding=0)
        
        self.frame.grid(column=0,row=i+1)
        
        self.label = ttk.Label(self.frame,text=self.name+':')

        self.haveEntry = ttk.Entry(self.frame,textvariable=self.have,width=5)
        self.buyEntry = ttk.Entry(self.frame, textvariable=self.buy,width=5)

        ttk.Label(self.frame,text=f"# in storage?").grid(column=1,row=1,sticky=E)
        ttk.Label(self.frame,text=f"# to buy?").grid(column=3,row=1,sticky=E)

        self.label.grid(column=0,row=1,padx=4)
        self.haveEntry.grid(column=2,row=1,sticky=W)
        self.buyEntry.grid(column=4,row=1,sticky=W)

'''
Sources refers to where a seed can be purchased / obtained
0 = mines / tilling source / cart
1 = pierre sells it
2 = sandy sells it
3 = requires island access 
4 = year 2+
'''
listOfAllPlants=[]
seasonsSPR = ["spring/summer/fall","spring","spring","spring","spring/summer","spring","spring","spring","spring","spring","spring","spring","spring","spring"]
seasonsSUM = ["summer","summer/fall","summer","summer","summer","summer","summer","summer","summer","summer","summer","summer/fall","summer","summer/fall"]
seasonsFALL= ["fall","fall","fall","fall","fall","fall","fall","fall","fall","fall","fall","fall","winter","summer","summer"]
seasonsList = seasonsSPR+seasonsSUM+seasonsFALL

sourcesSPR = [0,1,0,1,0,3,1,1,1,1,2,0,1,1]
sourcesSUM = [1,1,1,1,1,1,1,4,2,1,0,1,1,1]
sourcesFALL= [1,4,2,1,0,1,1,1,1,1,1,0,0,3,3]
sourcesList = sourcesSPR+sourcesSUM+sourcesFALL

pricesSPR = [0,30,0,80,0,40,60,70,20,50,100,100,20,40]
pricesSUM = [80,150,60,40,80,100,40,100,400,50,0,200,50,10]
pricesFALL = [70,30,20,50,0,240,20,200,60,100,60,1000,0,0,0]
pricesList = pricesSPR+pricesSUM+pricesFALL

neededSPR = [1,2,1,2,1,13,3,3,3,3,2,1,1,1]
neededSUM = [3,3,3,5,4,2,4,4,2,1,1,1,9,1]
neededFALL= [3,3,12,2,1,5,3,2,1,6,3,2,1,2,5]
neededList = neededSPR+neededSUM+neededFALL

namesSPR = ["Ancient Fruit","Blue Jazz","Carrot","Cauliflower","Coffee Bean","Garlic","Green Bean","Kale","Parsnip","Potato","Rhubarb","Strawberry","Tulip","Unmilled Rice"]
namesSUM = ["Blueberry","Corn","Hops","Hot Pepper","Melon","Poppy","Radish","Red Cabbage","Starfruit","Summer Spangle","Summer Squash","Sunflower","Tomato","Wheat"]
namesFALL= ["Amaranth","Artichoke","Beet","Bok Choy","Broccoli","Cranberries","Eggplant","Fairy Rose","Grape","Pumpkin","Yam","Sweet Gem Berry","Powdermelon","Pineapple","Taro Root"]
namesList = namesSPR+namesSUM+namesFALL
#max 30 can show at a time
def makePlants(parent):
    
    for i in range(len(neededList)):
        plant = crop(seasonsList[i]+"/island",sourcesList[i],pricesList[i],neededList[i],namesList[i],parent,i)
        listOfAllPlants.append(plant)
