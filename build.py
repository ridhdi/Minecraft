import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

import mcpi.block as block

pos = mc.player.getTilePos()
for y in range(20):
    for x in range(20):
        mc.setBlock(pos.x+x,pos.y+y,pos.z,block.Block(20).id)


for y in range(20):
    for z in range(20):
        mc.setBlock(pos.x,pos.y+y,pos.z+z,block.Block(20).id)


for y in range(20):
    for x in range(20):
        mc.setBlock(pos.x+x,pos.y+y,pos.z+20,block.Block(20).id)

for y in range(20):
    for z in range(20):
        mc.setBlock(pos.x+20,pos.y+y,pos.z+z,block.Block(20).id)

for x in range(20):
    for z in range(20):
        mc.setBlock(pos.x+x,pos.y,pos.z+z,block.Block(20).id)

for x in range(20):
    for z in range(20):
        mc.setBlock(pos.x+x,pos.y+20,pos.z+z,block.Block(20).id)



mc.setBlock(pos.x+10,pos.y+12,pos.z+10,block.TORCH.id)
mc.setBlock(pos.x+10,pos.y+1,pos.z+10,block.TORCH.id)
mc.setBlock(pos.x+21,pos.y,pos.z-1,block.TORCH.id)
mc.setBlock(pos.x-1,pos.y,pos.z-1,block.TORCH.id)

#Start of Iron
