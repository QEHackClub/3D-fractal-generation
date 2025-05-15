import PIL as pil
from PIL import Image
import numpy
import amulet_nbt #be sure to use the 1.0 pure python version

#these are all the recorded RGB values for a bunch of blocks, in the order given by palette, i do 3D pythag to determine closest colour match
concs=[
[191,165,169],
[8,10,15],
[44,46,143],
[96,59,31],
[21,119,136],
[54,57,61],
[73,91,36],
[35,137,198],
[125,125,115],
[94,168,24],
[169,48,159],
[224,97,0],
[213,101,142],
[100,31,156],
[142,32,32],
[207,213,214],
[240,175,21],    
[121,42,172],
[20,21,25],
[53,57,157],
[114,71,40],
[21,137,145],
[62,68,71],
[84,109,27],
[58,175,217],
[142,142,134],
[112,185,25],
[189,68,179],
[240,118,19],
[237,141,172],
[160,39,34],
[233,236,236]
]

#world=input("what is your world called?\n") #this changes the file path and where the structure is saved
world = "'for research'"
blocks='blocks: ['
palette='palette:[{"Name": "minecraft:polished_andesite"},{"Name": "minecraft:black_concrete"}, {"Name": "minecraft:blue_concrete"}, {"Name": "minecraft:brown_concrete"}, {"Name": "minecraft:cyan_concrete"}, {"Name": "minecraft:gray_concrete"}, {"Name": "minecraft:green_concrete"}, {"Name": "minecraft:light_blue_concrete"}, {"Name": "minecraft:light_gray_concrete"}, {"Name": "minecraft:lime_concrete"}, {"Name": "minecraft:magenta_concrete"}, {"Name": "minecraft:orange_concrete"}, {"Name": "minecraft:pink_concrete"}, {"Name": "minecraft:purple_concrete"}, {"Name": "minecraft:red_concrete"}, {"Name": "minecraft:white_concrete"}, {"Name": "minecraft:yellow_concrete"},{"Name":"minecraft:purple_wool"},{"Name":"minecraft:black_wool"},{"Name":"minecraft:blue_wool"},{"Name":"minecraft:brown_wool"},{"Name":"minecraft:cyan_wool"},{"Name":"minecraft:gray_wool"},{"Name":"minecraft:green_wool"},{"Name":"minecraft:light_blue_wool"},{"Name":"minecraft:light_gray_wool"},{"Name":"minecraft:lime_wool"},{"Name":"minecraft:magenta_wool"},{"Name":"minecraft:orange_wool"},{"Name":"minecraft:pink_wool"},{"Name":"minecraft:red_wool"},{"Name":"minecraft:white_wool"}]'

#palette='palette:[{"Name":"minecraft:foo"}]' #this is the format for adding more blocks to the palette
im=Image.open('C:/Users/euanr/OneDrive/Pictures/Camera Roll/M.png') #Change this to your filepath of the image
width,height=im.size
print(width,height) #keep the image size sensible (in the hundreds for width/height)


#this is all the actual math, its just pythag
for x in range(round(width)):
    x=width-x-1
    for y in range(height):
        smallest=1000
        coord=x,y
        values=["","",""]
        values=im.getpixel(coord)
        for n in range(len(concs)):
            distance=abs((((concs[n][0]-values[0])**2)+((concs[n][1]-values[1])**2)+((concs[n][2]-values[2])**2))**0.5)
            if distance<smallest-1:
                smallest=distance
                state=n
                
        blocks=blocks+'{"pos": ['+ str(x)+','+str(height-y)+','+str(round(1))+'],"state":'+str(state)+'},'
blocks = blocks +']'
filepath="C:/Users/euanr/AppData/Roaming/.minecraft/saves/"+world+"/generated/minecraft/structures/circle.nbt" #change this to the correct filepath for your stucture
#you might have to create a blank structure called image as it sometimes only edits existing ones and struggles to generate new files
nbt_obj = amulet_nbt.load(filepath)  

#this all comes from https://github.com/Amulet-Team/Amulet-NBT/blob/1.0/README.md
nbt_obj.save_to('filepath')
with open(filepath, 'wb') as f:
    nbt_obj.save_to(f)

nbt_obj3 = amulet_nbt.from_snbt('{size: ['+"1"+', '+str(1)+', '+str(1)+'],entities: [], '+blocks+','+palette+',DataVersion:2860,},')

nbt_obj3.save_to(filepath) # binary NBT has extra data that is lost in SNBT so you need to do this to add that data back in
nbt_obj3.to_snbt() # convert back to SNBT
