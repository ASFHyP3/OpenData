# AWS Open Data Bucket - ASF SAR Data Products for Disaster Events

Welcome to the AWS Open Data Bucket hosting Synthetic Aperture Radar (SAR) data products provided by the 
Alaska Satellite Facility (ASF). This repository is dedicated to offering valuable SAR data supporting responses 
to a range of disaster events. 

This repository contains a number of different prefixes, some supporting specific response efforts, and others 
supporting general disaster response services. 

## Table of Contents
1. [Introduction](#introduction)
2. [Data Products](#data-products)
3. [Disaster Support Services](#disaster-support-services)
4. [Disaster Event Prefixes](#disaster-event-prefixes)
5. [Accessing the Data](#accessing-the-data)
6. [License](#license)
7. [Manifest](#manifest)

## Introduction

Synthetic Aperture Radar (SAR) data is a powerful tool for monitoring and assessing disaster events. 
The Alaska Satellite Facility (ASF) has curated this collection of SAR data products, making it accessible 
to the public through this AWS Open Data Bucket. The data covers a range of disaster events, providing valuable 
insights for researchers, scientists, and emergency response teams.

## Data Products

The AWS Open Data Bucket contains a variety of SAR data products, including but not limited to:

- **Radiometrically Terrain Corrected (RTC) Data:** Providing near real-time SAR observations for rapid analysis.
    - See [ASF's RTC On Demand Product Guide](https://hyp3-docs.asf.alaska.edu/guides/rtc_product_guide/) 
      for a detailed overview of this dataset type.

- **Interferometric Synthetic Aperture Radar (InSAR) Data:** Offering insights into ground deformation and displacement.
    - See [ASF's InSAR On Demand Product Guide](https://hyp3-docs.asf.alaska.edu/guides/insar_product_guide/) 
      for a detailed overview of this dataset type.

- **Change Detection Maps:** Products highlighting significant changes between SAR acquisitions.

Each disaster event folder includes relevant data products in multiple formats to accommodate different analysis needs.

## Disaster Support Services

These datasets are generated by ASF in support of ongoing monitoring services. They include ASF's standard 
[Sentinel-1 On-Demand RTC](https://storymaps.arcgis.com/stories/2ead3222d2294d1fae1d11d3f98d7c35) products, 
along with surface water extent products generated using the [HydroSAR](https://github.com/HydroSAR/HydroSAR) workflow. 

The products include the following:
- **VH.tif** - Sentinel-1 RTC image in VH polarization
- **VV.tif** - Sentinel-1 RTC image in VV polarization
- **VV.tif.xml** - Metadata file for the VV GeoTIFF, including information about the Sentinel-1 source raster 
  and the processing workflow
- **WM.tif** - Surface water extent raster
- **WM_HAND.tif** - Height Above Nearest Drainage, used to generate the WM product
- **dem.tif** - Copy of the Digital Elevation Model used to process the RTC product 
  ([Copernicus GLO-30 DEM](https://dataspace.copernicus.eu/explore-data/data-collections/copernicus-contributing-missions/collections-description/COP-DEM) 
  with an ellipsoid correction applied)
- **rgb.tif** - False-color [RGB Decomposition](https://github.com/ASFHyP3/hyp3-lib/blob/main/docs/rgb_decomposition.md), 
  combining both VV and VH returns

Note that the WM (surface water extent) products have only been 
[validated in the Hindu Kush Himalayan region](https://www.mdpi.com/2072-4292/16/17/3244). 
While they are available for other areas, they may not perform well in all cases. Use caution when referencing these 
products, as areas with very dry or frozen soils may be classified as surface water. 

These products can be explored and accessed through interactive web applications, which are regularly updated to 
include new acquisitions. They are hosted in the following prefixes:
- image-services/RTC_services
- HKHwatermaps

### RTC Services

The files in the image-services/RTC_services prefix are generated to support the 
[NASA Earth Science Applied Science Disasters](https://appliedsciences.nasa.gov/what-we-do/disasters) 
program. These products cover the east and west coasts of the United States and the entire state of Alaska. 

ASF has published image services for the VV, VH, and RGB products hosted under this prefix. These image services 
allow the data to be available immediately to disaster response personnel, without any additional processing. 
They can be explored interactively in 
[this web map](https://asf-daac.maps.arcgis.com/home/webmap/viewer.html?webmap=3dd8d25559db4ba6aa0e1b6e8cb5d39a).

New Sentinel-1 acquisitions are processed to RTC and transferred to this prefix every three hours, and image 
services are updated daily.

Mosaic-level overviews in Cloud Raster Format (CRF) are generated for these services and hosted in the `image-service-overviews` prefix.

WM products are also available, and can be explored in 
[this web map](https://asf-daac.maps.arcgis.com/apps/mapviewer/index.html?webmap=faa83e4ccfe64bb8a99c13ef70b19b8f), 
but use caution when interpreting the images, especially in arid regions and shoulder seasons where 
ground may be frozen or saturated. 

### HKHwatermaps

The HKHwatermaps prefix includes products generated over the Hindu Kush Himalayan (HKH) region in support of 
[ICIMOD](https://www.icimod.org/), which maintains image services and a 
[web application](https://geoapps.icimod.org/FloodInundation/) for flood monitoring.

New Sentinel-1 acquisitions are processed to RTC and transferred to this prefix every three hours. 

## Disaster Event Prefixes

Some prefixes in this bucket reference a particular event. These prefixes help users quickly identify 
and navigate to the data corresponding to a particular event. The prefixes are a combination of the month/year 
of the disaster event, and the location affected by the event.

For example, the `jan2024_japan` prefix contains data products relevant for the earthquake in Japan on 
January 1st, 2024.

Users can find the data for a specific disaster event by exploring the corresponding prefix.

## Accessing the Data

To access the data, users can utilize the AWS S3 API or AWS Command Line Interface (CLI). The data is stored in the following structure:

```
s3://asf-event-data/{disaster_event_prefix}/{data_product}
```

For example:
```
s3://asf-event-data/jan2024_japan/S1A_IW_20231218T205948_DVP_RTC10_G_gpuned_AE77.zip
```
This structure allows for efficient and organized access to the SAR data products.

You can explore the contents of one of these prefixes using a command like:

```
aws s3 ls s3://asf-event-data/jan2024_japan/
```

To download a single product to your local directory, you can use a command like:

```
aws s3 cp s3://asf-event-data/jan2024_japan/S1A_IW_20231218T205948_DVP_RTC10_G_gpuned_AE77.zip .
```

## License

The data in this AWS Open Data Bucket is provided freely and openly under the [Creative Commons Zero (CC0) 1.0 Universal License](https://creativecommons.org/publicdomain/zero/1.0/). You may use this data for any purpose you would like.

Thank you for using the AWS Open Data Bucket for ASF SAR Data Products! If you have any questions or feedback, feel free to reach out to us.

## Manifest
This section contains a list of all data products available for each disaster event. Please refer to the [Data Products](#data-products) if you want to learn more about each product type.

### jan2024_japan

- InSAR
    - S1AA_20231225T205124_20240106T205124_VVR012_INT40_G_weF_D0E5.zip
    - S1AA_20231225T205152_20240106T205151_VVR012_INT40_G_weF_F454.zip
- RTC
    - S1A_IW_20231218T205948_DVP_RTC10_G_gpuned_AE77.zip
    - S1A_IW_20231225T205124_DVR_RTC10_G_gpuned_52B6.zip
    - S1A_IW_20231225T205152_DVR_RTC10_G_gpuned_B454.zip
    - S1A_IW_20231230T205948_DVR_RTC10_G_gpuned_564C.zip
    - S1A_IW_20240106T085056_DVR_RTC10_G_gpuned_2DEA.zip
    - S1A_IW_20240106T205124_DVR_RTC10_G_gpuned_57A0.zip
    - S1A_IW_20240106T205151_DVR_RTC10_G_gpuned_1A88.zip

---

[Registry of Open Data on AWS](https://registry.opendata.aws/)
