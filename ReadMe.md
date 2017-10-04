NTMDTRead
==========
[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-physics/NTMDTRead/workflows/CI/master/urm-0.CI-py3-none-any.whl)
[wheel (GitLab)](https://gitlab.com/KOLANICH/NTMDTRead/-/jobs/artifacts/master/raw/wheels/NTMDTRead-0.CI-py3-none-any.whl?job=build)
[![PyPi Status](https://img.shields.io/pypi/v/NTMDTRead.svg)](https://pypi.org/pypi/NTMDTRead)
![GitLab Build Status](https://gitlab.com/KOLANICH/NTMDTRead/badges/master/pipeline.svg)
![GitLab Coverage](https://gitlab.com/KOLANICH/NTMDTRead/badges/master/coverage.svg)
[![GitHub Actions](https://github.com/KOLANICH-physics/NTMDTRead/workflows/CI/badge.svg)](https://github.com/KOLANICH-physics/NTMDTRead/actions/)
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-physics/NTMDTRead.svg)](https://libraries.io/github/KOLANICH-physics/NTMDTRead)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://github.com/KOLANICH-tools/antiflash.py)

An **unofficial** set of tools to read the files produced by [NT-MDT®](https://www.ntmdt-si.ru/) software.

Different parts of this module are licensed differently. See [`./.reuse/dep5`](./.reuse/dep5) for more info.

* `.NTMDTReader` - Reads `.mdt` file format. Not very ready: some files are not read at all, some are read incorrectly, some frames are not yet implemented. But for large share of files it works pretty fine. Since it is based on the [Kaitai Struct](https://github.com/kaitai-io/kaitai_struct) [description](https://github.com/kaitai-io/kaitai_struct_formats/blob/master/scientific/nt_mdt/nt_mdt.ksy) reverse-engineered from [gwyddion implementation](https://svn.code.sf.net/p/gwyddion/code/trunk/gwyddion/modules/file/nt-mdt.c), it is licensed on the terms of [![GNU General Public License v3](https://www.gnu.org/graphics/gplv3-88x31.png)](./gpl-3.0.md). I'm sorry for that I'm too lazy to black box reverse engineer it from scratch entirely.

* `.colors` - Reads `.pal` palette files and transforms them into `matplotlib` colormaps. Also allows transforming matplotlib colormaps into NT-MDT format for using them in the original software. The format parsing code is based on the Kaitai Struct [description](https://github.com/kaitai-io/kaitai_struct_formats/blob/master/scientific/nt_mdt/nt_mdt_pal.ksy). This submodule license is [Unlicense](https://unlicense.org/). [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/).

* `.palettes` - A convenient importer for palettes. You may prefer to use it instead of `colors`.
```python
from NTMDTRead.palettes.Rainbows import Rainbow1
from NTMDTRead.palettes import Rainbows
import NTMDTRead.palettes.Rainbows
```
The names under `NTMDTRead.palettes.` are the names of `*.pal` files, and the names under them are the names of palettes in files.
Its license is [Unlicense](https://unlicense.org/). [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/).

* `.NTMDTReaderTSV` - Reads TSV file exported by `Nova` or `ImageAnalysis`. The license is [Unlicense](https://unlicense.org/). [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/).

* `examples/` - obviously, contains some usage examples
  * `show.py` contains a very stupid example of a viewer. It loops over all the mdt files in the dir and tries to show them.

  * `matplotlibColorMapConvert.py` converts matplotlib colormaps to the format available for ImageAnalysis/Nova.
    * [matplotlib.pal](https://gitlab.com/KOLANICH/NTMDTRead/-/jobs/artifacts/master/raw/palletes/matplotlib.pal?job=build). The license of this file is the same as [the one matplotlib has](https://matplotlib.org/users/license.html).
    * [colorcet.pal](https://gitlab.com/KOLANICH/NTMDTRead/-/jobs/artifacts/master/raw/palletes/colorcet.pal?job=build). The license of this file is the same as [the one colorcet has](https://github.com/bokeh/colorcet/blob/master/LICENSE.txt).
    * [cmocean.pal](https://gitlab.com/KOLANICH/NTMDTRead/-/jobs/artifacts/master/raw/palletes/cmocean.pal?job=build). The license of this file is the same as [the one cmocean has](https://github.com/matplotlib/cmocean/blob/master/LICENSE.txt) ![](https://img.shields.io/github/license/matplotlib/cmocean.svg).
    * [cmclimate.pal](https://gitlab.com/KOLANICH/NTMDTRead/-/jobs/artifacts/master/raw/palletes/cmclimate.pal?job=build). The license of this file is the same as [the one cmclimate has](https://github.com/serazing/cmclimate/blob/master/LICENSE.txt) ![](https://img.shields.io/github/license/serazing/cmclimate.svg).
    * [cmasher.pal](https://gitlab.com/KOLANICH/NTMDTRead/-/jobs/artifacts/master/raw/palletes/cmasher.pal?job=build). The license of this file is the same as [the one cmasher has](https://github.com/1313e/CMasher/blob/master/LICENSE) ![](https://img.shields.io/github/license/1313e/CMasher.svg).
    * [vapeplot.pal](https://gitlab.com/KOLANICH/NTMDTRead/-/jobs/artifacts/master/raw/palletes/vapeplot.pal?job=build). The license of this file is the same as [the one vapeplot has](https://github.com/dantaki/vapeplot/blob/master/LICENSE) ![](https://img.shields.io/github/license/dantaki/vapeplot.svg).
    * [seaborn.pal](https://gitlab.com/KOLANICH/NTMDTRead/-/jobs/artifacts/master/raw/palletes/seaborn.pal?job=build). The license of this file is the same as [the one seaborn has](https://github.com/mwaskom/seaborn/blob/master/LICENSE) ![](https://img.shields.io/github/license/mwaskom/seaborn.svg).
    * [proplot.pal](https://gitlab.com/KOLANICH/NTMDTRead/-/jobs/artifacts/master/raw/palletes/proplot.pal?job=build). The license of this file is the same as [the one proplot has](https://github.com/lukelbd/proplot/blob/master/LICENSE.txt) ![](https://img.shields.io/github/license/lukelbd/proplot.svg).
    * [cmcrameri.pal](https://gitlab.com/KOLANICH/NTMDTRead/-/jobs/artifacts/master/raw/palletes/cmcrameri.pal?job=build). The license of this file is the same as [the one cmcrameri has](https://github.com/callumrollo/cmcrameri/blob/main/LICENSE) ![](https://img.shields.io/github/license/callumrollo/cmcrameri.svg).
    * [cmastro.pal](https://gitlab.com/KOLANICH/NTMDTRead/-/jobs/artifacts/master/raw/palletes/cmastro.pal?job=build). The license of this file is the same as [the one cmastro has](https://github.com/adrn/cmastro/blob/main/LICENSE) ![](https://img.shields.io/github/license/adrn/cmastro.svg).
