# Global 30m HAND dataset

Height Above Nearest Drainage (HAND) is a terrain model that normalizes topography to the relative heights along the drainage network and is used to describe the relative soil gravitational potentials or the local drainage potentials. Each pixel value represents the vertical distance to the nearest drainage. The HAND data provides near-worldwide land coverage at 30 meters and was produced from the 2021 release of the Copernicus GLO-30 Public DEM as distributed in the [Registry of Open Data on AWS](https://registry.opendata.aws/copernicus-dem/).

## Data processing

To generate the GLO-30 HAND, we used the [HydroSAR](https://github.com/HydroSAR/HydroSAR) Python package, which is based on the HydroSAR [Big_Hand_notebook.ipynb](https://github.com/HydroSAR/HydroSAR/blob/v1.0.0/notebooks/instructional/Big_Hand_notebook.ipynb) and uses [PySheds](https://github.com/mdbartos/pysheds), a library for simple and fast watershed delineation in Python. This involves:

* Filling pits (single-cells lower than their surrounding neighbors) in the DEM
* Filling depressions (regions of cells lower than their surrounding neighbors) in the DEM
* Resolving un-drainable flats
* Determining the flow direction using the ESRI D8 routing scheme
* Determining flow accumulation (number of upstream cells)
* Creating a drainage mask using the accumulation threshold
* Calculating HAND

### GLO-30 HAND

The HAND data are provided as a tiled set of Cloud Optimized GeoTIFFs (COGs) with 30-meter (1 arcsecond) pixel spacing. The COGs are organized into the same [1 degree by 1 degree grid tiles](https://copernicus-dem-30m.s3.amazonaws.com/readme.html) as the GLO-30 DEM, and individual tiles are pixel-aligned to the corresponding COG DEM tile. The properties of the COG files:

* 32 floating point data type
* DEFLATE compression using predictor for floating points (PREDICTOR=3)
* average downsampling
* height: 3600 pixels
* TIFF tile size: 1024 × 1024 pixels

| **Longitude spacing** | **Latitude spacing** | **width** | **overview widths** |
|-----------------------|----------------------|-----------|---------------------|
| 0 - 50                | 1x                   | 3600      | 1800, 900, 450      |
| 50 - 60               | 1.5x                 | 2400      | 1200, 600, 300      |
| 60 - 70               | 2x                   | 1800      | 900, 450, 225       |
| 70 - 80               | 3x                   | 1200      | 600, 300, 150       |
| 80 - 85               | 5x                   | 720       | 360, 180, 90        |
| 85 - 90               | 10x                  | 360       | 180, 90, 45         |

## Data structure

Each file is its own object in Amazon S3. The data are organised per tiles into to same [1 degree by 1 degree grid tiles](https://copernicus-dem-30m.s3.amazonaws.com/readme.html) as the GLO-30 DEM. The tiles are contained in an AWS S3 Bucket named:

`glo-30-hand`

And are organised under S3 prefixes like:

`[version]/[DEM release year]`

Where `[version]` indicates the HAND dataset version, and `[DEM release year]` indicates which release of the Copernicus GLO-30 DEM the HAND data was generated from. For example, the tiles are available in the following location: `s3://glo-30-hand/v1/2021/`

The HAND tile files retain the same naming scheme as the original COP-30 DEM tiles like:

`Copernicus_DSM_COG_[resolution]_[northing]_[easting]_HAND.tif`

Where:

* `[resolution]` - resolution in arc seconds (not meters!), which is `10` for GLO-30.

* `[northing]` - In original GLO-30 DEM files as distributed by Copernicus, this is the northing of the center of the bottom-most pixels in decimal degrees where the decimal part is always `00`, e.g. `S50_00`. However, in the GLO-30 DEM COGs and our GLO-30 HAND files, because the bottom-most pixels have been removed, the center of the new bottom-most pixels are one pixel-length (resolution) away to north.

* `[easting]` - The easting of the center of the left-most pixels in decimal degrees where the decimal part is always `00`, e.g. `w125_00`.

## Accessing the GLO-30 HAND data

If you use the AWS Command Line Interface, you can list data in the bucket with the “ls” command:

`aws s3 ls --recursive --summarize s3://glo-30-hand/`

## Contact

If you have questions about the data, please email the [ASF Tools Team](mailto:uaf-asf-apd@alaska.edu).

## License

Copyright 2022 Alaska Satellite Facility (ASF). Produced using the Copernicus WorldDEM™-30 © DLR e.V. 2010-2014 and © Airbus Defence and Space GmbH 2014-2018 provided under COPERNICUS by the European Union and ESA; all rights reserved. The use of the HAND data falls under the terms and conditions of the [Creative Commons Zero (CC0) 1.0 Universal License](https://creativecommons.org/publicdomain/zero/1.0/).

---

[AWS Public Datasets](http://aws.amazon.com/public-datasets)
