#!/usr/bin/env python3
import os
from setuptools import setup
from setuptools.config import read_configuration
from pathlib import Path

thisDir = Path(__file__).parent.absolute()
packageDir = thisDir / "NTMDTRead"
cfg = read_configuration(str(thisDir / 'setup.cfg'))
#print(cfg)
cfg["options"].update(cfg["metadata"])
cfg = cfg["options"]

from kaitaiStructCompile.toolkit import permissiveDecoding
from pathlib import Path
formatsPath = thisDir / "kaitai_struct_formats"
mdtFormatsDir = formatsPath / "scientific" / "nt_mdt"
cfg["kaitai"] = {
	"formatsRepo": {
		"git": "https://github.com/KOLANICH/kaitai_struct_formats.git",
		"refspec": "mdt",
		"localPath" : str(formatsPath),
		"update": True
	},
	"flags": ["--python-package", "."],
	"outputDir": packageDir / "kaitai",
	"inputDir": mdtFormatsDir,
	"formats": {},
	"search": True
}

setup(use_scm_version = True, **cfg)
