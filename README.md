# OpenDataHubProcess
Preparing ARC's OpenDataHub regular datasets by cleaning and uploading to ARC's OpenDataHub

## Package Setup
1. the arcgis packages is not avaailable for mac silicon chips at the time of development... so you have to set your virtual or conda environment to osx-64 which is intel based instead of osx-arm64 which is arm base for mac silicon chips. You can either set your environment to (atleast in conda) by doing `conda config --env --set subdir osx-64` after you have navigated to your conda environment you wish to use. Then you can install the `arcgis` package.
2. The `arcgis` package is a bit finicky with it's dependencies. Both `geopandas` and `arcgis` install dependencies for the `libtiff` and `lerc` packages, however the arcgis version is outdated and will not work with geopandas, so you might have to install the `libtiff` and `lerc` packages manually after installing those two packages.