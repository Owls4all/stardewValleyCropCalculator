from tkinter import *
from tkinter import ttk

from crops import *
def do_stuff(*args):
    #calc_space()
    do_plants()
    calc_plants()
def calc_space(*args):
    try:
        s1 = int(rSprinklers.get())
        s2 = int(qSprinklers.get())
        s3 = int(iSprinklers.get())
        s4 = int(pSprinklers.get())
        soil.set(4*s1 + 8*s2 + 24*s3 + 48*s4)
        calc_plants()
    except ValueError:
        pass

availablePlants=[]
def do_plants():
    global availablePlants
    availablePlants=[]
    availableSources=[0,1]
    if desertAccess.get() == 'True':
        availableSources.append(2)
    if islandAccess.get() == 'True':
        availableSources.append(3)
    if y2Access.get() == 'True':
        availableSources.append(4)
    for i in range(len(listOfAllPlants)):
        plant = listOfAllPlants[i]
        plant.show = False
        if season.get() in plant.season and plant.sources in availableSources:
            plant.show = True
            availablePlants.append(plant.name)
            
            plant.frame.grid()
            #print(f"It should have put {plant.name} on the screen")
        else:
            plant.frame.grid_remove()
            #print(f"{plant.name} should not be on the screen")
    defaultCropChooser['values']=availablePlants
    secondCropChooser['values']=availablePlants
    print(availablePlants)
def calc_plants(*args):
    defaultCrop.set(defaultCrop.get())
    global availablePlants
    try:
        best = defaultCrop.get()
        second = alternateCrop.get()
        spaceTotal = int(soil.get())
        spaceLeft=spaceTotal
        gTotal = int(budget.get())
        gLeft=gTotal
        print(availablePlants)
        for i in range(len(availablePlants)):
            
            plantIndex = namesList.index(availablePlants[i])
            plant=listOfAllPlants[plantIndex]
            
            countHave = int(plant.have.get())
            countBuy = int(plant.buy.get())
            print(f"{plant.name}: have {countHave}, buy {countBuy}")
            cost = plant.cost * countBuy
            gLeft -= cost
            spaceLeft -= countBuy
            spaceLeft -= countHave
            print(f"Remaining funds: {gLeft}")
            print(f"Remaining space: {spaceLeft}")

        bestIndex = namesList.index(best)
        max_cost = spaceLeft*pricesList[bestIndex]

        secondIndex = namesList.index(second)
        min_cost = spaceLeft*pricesList[secondIndex]

        if max_cost <=gLeft:
            bestCount = spaceLeft
            secondCount=0
        elif min_cost >=gLeft:
            bestCount = 0
            secondCount = gLeft//pricesList[secondIndex]
            pass # Too Expensive! Choose something cheaper! (maybe output gLeft//costofsecondBest - like, an "as many as you can" type thing)
        else:
            upgrade_funds = gLeft-min_cost
            difference=pricesList[bestIndex]-pricesList[secondIndex]
            bestCount = upgrade_funds//difference
            secondCount = spaceLeft-bestCount
        bestBuy.set(bestCount)
        secondBuy.set(secondCount)

            
        
            
    except ValueError:
        pass
        
root = Tk()
root.bind("<Return>",do_stuff)
root.title("Soil + Budget Seed calculator")

outputsMainframe = ttk.Frame(root,padding="3 3 12 12")
outputsMainframe.grid(row=1,column=0)

plantsMainframe = ttk.Frame(root,padding="3 3 12 12")
plantsMainframe.grid(column=1,row=0,rowspan=4,sticky=NE)
defaultCrop = StringVar()
alternateCrop = StringVar()


defaultCropChooser = ttk.Combobox(outputsMainframe,textvariable=defaultCrop)
defaultCropChooser.bind('<<ComboboxSelected>>',calc_plants)
defaultCropChooser.grid(column=1,row=0,sticky=N)
ttk.Label(outputsMainframe,text='Primary Crop:').grid(column=0,row=0)
bestBuy = StringVar()
ttk.Label(outputsMainframe,text="You should buy").grid(column=0,row=2)
ttk.Label(outputsMainframe,textvariable=bestBuy).grid(column=1,row=2)
ttk.Label(outputsMainframe,text="Primary Crop").grid(column=2,row=2)

secondCropChooser = ttk.Combobox(outputsMainframe,textvariable=alternateCrop)
secondCropChooser.bind('<<ComboboxSelected>>',calc_plants)
secondCropChooser.grid(column=1,row=1)
ttk.Label(outputsMainframe,text='Secondary Crop:').grid(column=0,row=1)
secondBuy = StringVar()
ttk.Label(outputsMainframe,text="And ").grid(column=0,row=3)
ttk.Label(outputsMainframe,textvariable=secondBuy).grid(column=1,row=3)
ttk.Label(outputsMainframe,text="Secondary Crop").grid(column=2,row=3)


makePlants(plantsMainframe)

sprinklerMainframe = ttk.Frame(root,padding="3 3 12 12")
sprinklerMainframe.grid(column=0,row=0,sticky=(N,W))
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

rSprinklers=StringVar(value="0")
rSprinklers.trace_add("write",calc_space)
rEntry = ttk.Entry(sprinklerMainframe,width=5,textvariable=rSprinklers)
rEntry.grid(column=0,row=1,sticky=(W,E))
ttk.Label(sprinklerMainframe,text="Sprinklers").grid(column=1,columnspan=3,row=1,sticky=W)

qSprinklers = StringVar(value="0")
qSprinklers.trace_add("write",calc_space)
qEntry = ttk.Entry(sprinklerMainframe, width=5, textvariable=qSprinklers)
qEntry.grid(column=0,row=2,sticky=(W,E))
ttk.Label(sprinklerMainframe,text="Quality Sprinklers").grid(column=1,columnspan=3,row=2,sticky=W)

iSprinklers = StringVar(value="0")
iSprinklers.trace_add("write",calc_space)
iEntry = ttk.Entry(sprinklerMainframe,width=5,textvariable=iSprinklers)
iEntry.grid(column=0,row=3,sticky=(W,E))
ttk.Label(sprinklerMainframe,text="Iridium Sprinklers").grid(column=1,columnspan=3,row=3,sticky=W)

pSprinklers = StringVar(value='0')
pSprinklers.trace_add("write",calc_space)
pEntry = ttk.Entry(sprinklerMainframe,width=5,textvariable=pSprinklers)
pEntry.grid(column=0,row=4,sticky=(W,E))
ttk.Label(sprinklerMainframe,text="Pressurized Iridium Sprinklers").grid(column=1,columnspan=3,row=4,sticky=W)

soil = StringVar(value="0")
ttk.Label(sprinklerMainframe,textvariable=soil).grid(column=0,row=6)
ttk.Label(sprinklerMainframe, text='Soil',).grid(column=1,row=6)

growingCrops = StringVar(value='0')
spaceUsed = ttk.Entry(sprinklerMainframe,textvariable=growingCrops,width=5)
spaceUsed.grid(column=0,row=7)
ttk.Label(sprinklerMainframe,text="Persistant Crops").grid(column=1,row=7)

for child in sprinklerMainframe.winfo_children():
    child.grid_configure(padx=5,pady=5)

statsMainframe=ttk.Frame(root,padding = "3 3 12 12")
statsMainframe.grid(column=0,row=2,sticky=(N))
budget = StringVar(value='500')
ttk.Entry(statsMainframe,width=8,textvariable=budget).grid(column=1,row=1,sticky=W)
ttk.Label(statsMainframe,text="Available Funds").grid(column=0,row=1,sticky=W)

desertAccess = StringVar(value='False')
desertCheck = Checkbutton(statsMainframe,text='Unlocked Desert?',variable=desertAccess,onvalue='True',offvalue="False")
desertCheck.grid(column=0,row=2,sticky=W)

islandAccess = StringVar(value='False')
islandCheck = Checkbutton(statsMainframe, text="Unlocked Island?",variable=islandAccess,onvalue='True',offvalue='False')
islandCheck.grid(column=0,row=3,sticky=W)

y2Access=StringVar(value='False')
y2Check = Checkbutton(statsMainframe,text='Year 2+ crops available?', variable=y2Access,onvalue='True',offvalue='False')
y2Check.grid(column=0,row=4,sticky=W)

season = StringVar(value='spring')
spring = ttk.Radiobutton(statsMainframe,text='Spring',variable=season,value='spring')
summer = ttk.Radiobutton(statsMainframe,text='Summer',variable=season,value='summer')
fall = ttk.Radiobutton(statsMainframe,text='Fall',variable=season,value='fall')
winter = ttk.Radiobutton(statsMainframe,text="Winter",value="winter",variable=season)
island = ttk.Radiobutton(statsMainframe,text="Island/Greenhouse",value="island",variable=season)


ttk.Button(statsMainframe,text='Calibrate Plant Options',command=do_stuff)

for child in statsMainframe.winfo_children():
    child.grid_configure(padx=5,pady=5)

do_stuff()
root.mainloop()

