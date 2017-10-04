import importlib
import os
import sys
from pathlib import Path

from matplotlib.colors import LinearSegmentedColormap, Colormap

from NTMDTRead.colors import matplotlibColorMaps2Pal

try:
	from pantarei import chosenProgressReporter
except ImportError:

	class chosenProgressReporter:
		__slots__ = ("progress", "total")

		def __init__(self, total, title) -> None:
			self.progress = 0
			self.total = total
			print(title)

		def report(self, key, incr=None, op=None) -> None:
			self.progress += incr
			print(key, ":", round(self.progress * 100 / self.total), "%\t", op)

		def __enter__(self):
			return self

		def __exit__(self, exc_type, exc_value, traceback):
			pass


__author__ = "KOLANICH"
__license__ = "Unlicense"

currentDir = Path(__file__).parent.absolute()
baseDir = currentDir.parent.absolute()
sys.path.insert(0, str(baseDir))


def detectColormapsNamesInAModuleByPresenceReversed(module):
	cmapNames = set(dir(module))
	cmapNamesRev = [el for el in cmapNames if el.endswith("_r") and el[:-2] in cmapNames]
	cmapNames = sorted(cmapNamesRev + [el[:-2] for el in cmapNamesRev])
	del cmapNamesRev
	return cmapNames


def filterByType(mod, targetType = None):
	if targetType is None:
		targetType = Colormap
	return {k: v for k, v in mod.__dict__.items() if isinstance(v, targetType)}

def getPalettableMatplotlibCmap(palletableSubmodule):
	import palettable
	return {k: v.mpl_colormap for k, v in filterByType(palletableSubmodule, palettable.palette.Palette).items()}


# (output file name, module name, function to get dict of colormaps, official website you can get the module)
conversionSpec = (
	("matplotlib", "matplotlib.cm", lambda matplotlibCm: matplotlibCm._cmap_registry, "https://github.com/matplotlib/matplotlib"),
	("colorcet", "colorcet", filterByType, "https://github.com/holoviz/colorcet"),
	("cmocean", "cmocean", lambda cmocean: cmocean.cm.cmap_d, "https://github.com/matplotlib/cmocean"),
	("cmclimate", "cmclimate", lambda cmclimate: cmclimate.cm.cmaps, "https://github.com/serazing/cmclimate"),
	("cmasher", "cmasher", lambda cmasher: {k: getattr(cmasher.cm, k) for k in cmasher.cm.__all__}, "https://github.com/1313e/CMasher"),
	("vapeplot", "vapeplot", lambda vapeplot: {k: vapeplot.cmap(k) for k in vapeplot.palettes.keys()}, "https://github.com/dantaki/vapeplot"),
	("seaborn", "seaborn.cm", filterByType, "https://github.com/mwaskom/seaborn/"),
	("proplot", "proplot.colors", lambda pcolors: pcolors._cmap_database, "https://github.com/lukelbd/proplot"),
	("cmcrameri", "cmcrameri.cm", lambda cm: cm.cmaps, "https://github.com/callumrollo/cmcrameri"),
	("cmastro", "cmastro", lambda cmastro: {k.replace("cma:", ""): v for k, v in cmastro.cmaps.items()}, "https://github.com/adrn/cmastro"),
	
	#("nmmn", "nmmn.plots", lambda nmmn_plots: {k[:-4]: v() for k, v in nmmn_plots.__dict__.items() if k.endswith("cmap") and v.__code__.co_argcount == 0}, "https://github.com/rsnemmen/nmmn/blob/master/nmmn/plots.py"), # I don't recommend to install this package
	

	("cubehelix", "palettable.cubehelix", getPalettableMatplotlibCmap, "https://github.com/jiffyclub/palettable/tree/master/palettable/cubehelix"),
	("mycarta", "palettable.mycarta", getPalettableMatplotlibCmap, "https://github.com/jiffyclub/palettable/tree/master/palettable/mycarta"),
	("tableau", "palettable.tableau", getPalettableMatplotlibCmap, "https://github.com/jiffyclub/palettable/tree/master/palettable/tableau"),
	("wesanderson", "palettable.wesanderson", getPalettableMatplotlibCmap, "https://github.com/jiffyclub/palettable/tree/master/palettable/wesanderson"),

	("cartocolors_diverging", "palettable.cartocolors.diverging", getPalettableMatplotlibCmap, "https://github.com/jiffyclub/palettable/tree/master/palettable/cartocolors"),
	("cartocolors_sequential", "palettable.cartocolors.sequential", getPalettableMatplotlibCmap, "https://github.com/jiffyclub/palettable/tree/master/palettable/cartocolors"),
	("cartocolors_qualitative", "palettable.cartocolors.qualitative", getPalettableMatplotlibCmap, "https://github.com/jiffyclub/palettable/tree/master/palettable/cartocolors"),

	#("lightbartlein_diverging", "palettable.lightbartlein.diverging", getPalettableMatplotlibCmap, "https://github.com/jiffyclub/palettable/tree/master/palettable/lightbartlein"), # seems to be broken
	("lightbartlein_sequential", "palettable.lightbartlein.sequential", getPalettableMatplotlibCmap, "https://github.com/jiffyclub/palettable/tree/master/palettable/lightbartlein"),
)


if __name__ == "__main__":
	outputDir = Path(".") / "palletes"
	outputDir.mkdir(parents=True, exist_ok=True)

	with chosenProgressReporter(len(conversionSpec), "converting colormaps") as pr:
		for el in conversionSpec:
			(palName, modName, retriever, link) = el
			pr.report(key=palName, incr=0, op="importing")
			try:
				mod = importlib.import_module(modName)
			except ImportError:
				msg = "The lib is not installed, can be got at " + link
				pr.report(key=palName, incr=1, op=msg)
				pr.print(msg)
				continue

			pr.report(key=palName, incr=0, op="converting")
			try:
				cmapDict = retriever(mod)
				if len(cmapDict) == 0:
					pr.report(key=palName, incr=1, op="failed!")
					pr.print("No colormaps detected in " + palName +  "!")
					continue

				palData = matplotlibColorMaps2Pal(cmapDict)
			except BaseException as ex:
				pr.report(key=palName, incr=1, op="failed!")
				pr.print("Conversion of " + palName +  " has failed! " + str(ex))
				continue

			with (outputDir / (palName + ".pal")).open("wb") as f:
				f.write(palData)
				pr.report(key=palName, incr=1, op="converted")
