import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

import mcpi.block as block

pos = mc.player.getTilePos()


for i in range(10):
    mc.setBlock(pos.x+i,pos.y,pos.z,block.IRON_BLOCK.id)
    mc.setBlock(pos.x+i,pos.y+1,pos.z,block.IRON_BLOCK.id)
    mc.setBlock(pos.x+i,pos.y+1,pos.z-1,block.IRON_BLOCK.id)
    mc.setBlock(pos.x+i,pos.y+1,pos.z+1,block.IRON_BLOCK.id)
    mc.setBlock(pos.x+i,pos.y+2,pos.z,block.Block(86).id)
