# CPR Algorithm <img src="src/readme/logo.png" align="right" width="200" />

### Description

The Colour Pattern Regression
(CPR) algorithm complement for QGIS is presented for determining and
quantifying the relationship between aerial images and raster maps. Aerial
images can be readily decomposed into their standard RGB spaces that assign
numerical values to their colours. According to them, a linear regression can
be established to correlate raster values with the colour patterns, and if the
model performance is considered satisfactory, the final result will provide a
raster interpolation with finest resolution according to colour nuances within
the aerial image. The CPR Algorithm allow both, the calculation of the
regression coefficient and the evaluation of the goodness of fit of the model.
The use of the CPR-QGIS plugin could enable the study of the relationships of
aerial images and earth surface products – e.g. soil moisture content,
landcover, vegetation and forests, soils, urban heat islands – or marine
products – e.g. chlorophyll, total suspended solids. The tool is open source
and will be readily adapted with additional features and improved general
performance ratings thresholds for the physical problems to be solved.The Colour Pattern Regression (CPR) algorithm complement for QGIS is
presented for determining and quantifying the relationship between aerial
images and raster maps. Aerial images can be readily decomposed into their
standard RGB spaces that assign numerical values to their colours. According
to them, a linear regression can be established to correlate raster values
with the colour patterns, and if the model performance is considered satisfactory,
the final result will provide a raster interpolation with finest resolution
according to colour nuances within the aerial image. The CPR Algorithm
allow both, the calculation of the regression coefficient and the evaluation
of the goodness of fit of the model. The use of the CPR-QGIS complement
could enable the study of the relationships of aerial images and earth surface
products – e.g. soil moisture content, landcover, vegetation and forests,
soils, urban heat islands – or marine products – e.g. chlorophyll, total suspended
solids. The tool is open source and will be readily adapted with
additional features and improved general performance ratings thresholds for
the physical problems to be solved.

## Installation

* Download the last version available
  "last_version.zip".
* Open QGIS v3.x.
* Select Plugins\Manage and Install Plugins
* Select the option Install from ZIP.
* Browse the route to the “last_version.zip” file
  and press the install button.

## How does it work

### Model Inputs

* Area of interest (shp): Defines the outer
  interpolation polygon with a shape file.
* Area for calibration (shp): Defines a sub-polygon with a
  shape file for calculation of the initial values.
* Aerial image input: A three-banded (RGB) raster
  map with the aerial image of the study area.
* Raster data input: A raster map with the
  numerical values that can be correlated with colours.
* Results folder: Defines the calculations route.

### Model Calculations

* Variability RGB: Defines the variability around
  the initial RGB values for the high-resolution loop calculation.
* Initial values loop variability: Number of
  iterations that will be carried out for the calculation of the initial RGB
  values in the calibration area.
* High resolution loop variability: Number of
  iterations that will be carried out for the calculation of the final RGB
  values in the interest area.
* Performance statistics thresholds: Defines the
  thresholds for *Very good*, *Good*, *Satisfactory* and *Unsatisfactory*
  performance for the statistics NNSE, KGE and PBIAS.

### Model outputs

* RGB Coefficient: Present the calculated RGB parameters
  of the linear regression.
* Statistics performance (%Area): Presents the
  percentage of area from every model performance type defined in the
  Calculations section for the statistics NNSE, KGE and PBIAS.

## Case study

The information provided
includes the necessary information to reproduce an example of the correlation
between the aerial image from Sentinel 2 and a raster map of Total Suspended
Matter (TSM) from Sentinel 3.

In this case, Mar Menor lagoon
area was selected as part of the H2020 SMARTLAGOON project (GA 101017861).

## Add your files to CPR

- [ ] [Create](https://docs.github.com/en/repositories/working-with-files/managing-files/creating-new-files) or upload files
- [ ] [Add files using the command line](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://github.com/vielca/CPR
git branch -M main
git push -uf origin main
```

## Authors

- [@Pablo Blanco-Gómez](https://orcid.org/0000-0001-9465-2912)
- [@Constancio Amurrio-García](https://www.vielca.com/)
- [@Jose Luis Jimenez Garcia](https://orcid.org/0000-0001-6619-9057)
- [@Jose M. Cecilia](https://orcid.org/0000-0001-5648-214X)

### Acknowledgments

This work has been supported by the European Union’s Horizon 2020 research
and innovation programme under grant agreement No 101017861 and by the Ramon y
Cajal Grant RYC2018-025580-I, funded by MCIN/AEI/ 10.13039/501100011033 and
“ERDF A way of making Europe” and FSE invest in your future.

Moreover, authors acknowledge Vicente M. Candela Canales for supporting the
R&D investment and programs within the Vielca companies.
