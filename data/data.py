import worlds.ff6wc.WorldsCollide.data.dialogs as dialogs
import worlds.ff6wc.WorldsCollide.data.spells as spells
import worlds.ff6wc.WorldsCollide.data.characters as characters
import worlds.ff6wc.WorldsCollide.data.items as items
import worlds.ff6wc.WorldsCollide.data.metamorph_groups as metamorph_groups
import worlds.ff6wc.WorldsCollide.data.maps as maps
import worlds.ff6wc.WorldsCollide.data.enemies as enemies
import worlds.ff6wc.WorldsCollide.data.swdtechs as swdtechs
import worlds.ff6wc.WorldsCollide.data.blitzes as blitzes
import worlds.ff6wc.WorldsCollide.data.lores as lores
import worlds.ff6wc.WorldsCollide.data.rages as rages
import worlds.ff6wc.WorldsCollide.data.dances as dances
import worlds.ff6wc.WorldsCollide.data.steal as steal
import worlds.ff6wc.WorldsCollide.data.sketches as sketches
import worlds.ff6wc.WorldsCollide.data.controls as controls
import worlds.ff6wc.WorldsCollide.data.magiteks as magiteks
import worlds.ff6wc.WorldsCollide.data.espers as espers
import worlds.ff6wc.WorldsCollide.data.shops as shops
import worlds.ff6wc.WorldsCollide.data.coliseum as coliseum
import worlds.ff6wc.WorldsCollide.data.title_graphics as title_graphics

class Data:
    def __init__(self, rom, args):
        self.dialogs = dialogs

        self.spells = spells.Spells(rom, args)
        self.spells.mod()

        self.characters = characters.Characters(rom, args, self.spells)
        self.characters.mod()

        self.items = items.Items(rom, args, self.dialogs, self.characters)
        self.items.mod()

        self.metamorph_groups = metamorph_groups.MetamorphGroups(rom)
        self.metamorph_groups.mod()

        self.maps = maps.Maps(rom, args, self.items)
        self.maps.mod(self.characters)

        self.enemies = enemies.Enemies(rom, args)
        self.enemies.mod(self.maps)

        self.swdtechs = swdtechs.SwdTechs(rom, args, self.characters)
        self.swdtechs.mod()

        self.blitzes = blitzes.Blitzes(rom, args, self.characters)
        self.blitzes.mod()

        self.lores = lores.Lores(rom, args, self.characters)
        self.lores.mod(self.dialogs)

        self.rages = rages.Rages(rom, args, self.enemies)
        self.rages.mod()

        self.dances = dances.Dances(rom, args, self.characters)
        self.dances.mod()

        self.steal = steal.Steal(rom, args)
        self.steal.mod()

        self.sketches = sketches.Sketches(rom, args, self.enemies, self.rages)
        self.sketches.mod()

        self.controls = controls.Controls(rom, args, self.enemies, self.rages)
        self.controls.mod()

        self.magiteks = magiteks.Magiteks(rom, args)
        self.magiteks.mod()

        self.espers = espers.Espers(rom, args, self.spells, self.characters)
        self.espers.mod(self.dialogs)

        self.shops = shops.Shops(rom, args, self.items)
        self.shops.mod()

        self.coliseum = coliseum.Coliseum(rom, args, self.enemies, self.items)
        self.coliseum.mod()

        self.title_graphics = title_graphics.TitleGraphics(rom, args)
        self.title_graphics.mod()

    def write(self):
        self.dialogs.write()
        self.characters.write()
        self.items.write()
        self.metamorph_groups.write()
        self.maps.write()
        self.enemies.write()
        self.spells.write()
        self.swdtechs.write()
        self.blitzes.write()
        self.lores.write()
        self.rages.write()
        self.dances.write()
        self.steal.write()
        self.sketches.write()
        self.controls.write()
        self.magiteks.write()
        self.espers.write()
        self.shops.write()
        self.coliseum.write()
        self.title_graphics.write()
