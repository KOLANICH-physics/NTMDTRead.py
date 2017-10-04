import sys, os
from pathlib import Path
from matplotlib.colors import LinearSegmentedColormap

__author__="KOLANICH"
__license__="Unlicense"

currentDir=Path(__file__).parent.absolute()
baseDir=currentDir.parent.absolute()
sys.path.insert(0, str(baseDir))

from NTMDTRead.colors import matplotlibColorMaps2Pal

if __name__ == "__main__":
	outputDir = Path(".") / "palletes"
	outputDir.mkdir(parents=True, exist_ok=True)
	with (outputDir / ("matplotlib.pal")).open("wb") as f:
		f.write(matplotlibColorMaps2Pal())
	
	try:
		import colorcet
		d={k:v for k,v in colorcet.__dict__.items() if isinstance(v, LinearSegmentedColormap)}
		with (outputDir / ("colorcet.pal")).open("wb") as f:
			f.write(matplotlibColorMaps2Pal(d))
	except:
		pass
	
	try:
		import cmocean
		with (outputDir / ("cmocean.pal")).open("wb") as f:
			f.write(matplotlibColorMaps2Pal(cmocean.cm.cmap_d))
	except:
		pass
