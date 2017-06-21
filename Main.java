package org.devoxx4kids.forge.mods;

import net.minecraft.block.Block;
import net.minecraft.item.Item;
import net.minecraftforge.common.MinecraftForge;
import net.minecraftforge.fml.common.Mod;
import net.minecraftforge.fml.common.Mod.EventHandler;
import net.minecraftforge.fml.common.event.FMLInitializationEvent;

@Mod(modid = Main.MODID, version = Main.VERSION)
public class Main {
	public static final String MODID = "MyMods";
	public static final String VERSION = "1.0";

	public static Block enderBlock;
	public static Item enderIngot;

	@EventHandler
	public void init(FMLInitializationEvent event) {
		//registering the event handlers
		MinecraftForge.EVENT_BUS.register(new BlockBreakMessage());
		MinecraftForge.EVENT_BUS.register(new ExplodingMinecarts());
		MinecraftForge.EVENT_BUS.register(new ExplodingAnvils());
		MinecraftForge.EVENT_BUS.register(new BouncySponges());
		MinecraftForge.EVENT_BUS.register(new Parachute());
		MinecraftForge.EVENT_BUS.register(new SuperJump ());
	}
}
