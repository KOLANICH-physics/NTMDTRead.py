echo "TRAVIS is $TRAVIS"
if [ "$TRAVIS" = "true" ]; then
  SUDO="sudo";
else
  SUDO="";
fi;
echo "SUDO is $SUDO";

source ./.ci/pythonStdlibFixes.sh
$SUDO bash ./.ci/setupKS.sh
pip3 install --upgrade setuptools
pip3 install coveralls setuptools_scm 	git+https://gitlab.com/KOLANICH1/kaitaiStructCompile.py
pip3 install --upgrade git+https://github.com/bokeh/colorcet.git git+https://github.com/matplotlib/cmocean.git