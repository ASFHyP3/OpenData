# AWS Open Data Bucket - ASF SAR Data Products for Disaster Events

Welcome to the AWS Open Data Bucket hosting Synthetic Aperture Radar (SAR) data products provided by the Alaska Satellite Facility (ASF). This repository is dedicated to offering valuable SAR data corresponding to various disaster events. SAR products for each disaster event are collected with their own prefix, making it easy for users to locate and access relevant data.

## Table of Contents
1. [Introduction](#introduction)
2. [Disaster Event Prefixes](#disaster-event-prefixes)
3. [Data Products](#data-products)
4. [Accessing the Data](#accessing-the-data)
5. [License](#license)
6. [Manifest](#manifest)

## Introduction

Synthetic Aperture Radar (SAR) data is a powerful tool for monitoring and assessing disaster events. The Alaska Satellite Facility (ASF) has curated this collection of SAR data products, making it accessible to the public through this AWS Open Data Bucket. The data covers a range of disaster events, providing valuable insights for researchers, scientists, and emergency response teams.

At the 

## Disaster Event Prefixes

The data in this bucket is organized using specific prefixes for each disaster event. These prefixes help users quickly identify and navigate to the data corresponding to a particular event. The prefixes are a combination of the month/year of the disaster event, and the major country affected by the event.

For example, the `jan2024_japan` prefix contains data products relevant for the earthquake that hit Japan on January 1st, 2024.

Users can find the data for a specific disaster event by exploring the corresponding prefix.

## Data Products

The AWS Open Data Bucket contains a variety of SAR data products, including but not limited to:

- **Radiometrically Terrain Corrected (RTC) Data:** Providing near real-time SAR observations for rapid analysis.
    - See [this page](https://hyp3-docs.asf.alaska.edu/guides/rtc_product_guide/) for a detailed overview of this dataset type.
- **Interferometric Synthetic Aperture Radar (InSAR) Data:** Offering insights into ground deformation and displacement.
    - See [this page](https://hyp3-docs.asf.alaska.edu/guides/insar_product_guide/) for a detailed overview of this dataset type.
- **Change Detection Maps:** Highlighting significant changes between SAR acquisitions.

Each disaster event folder includes relevant data products in multiple formats to accommodate different analysis needs.

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

The data in this AWS Open Data Bucket is provided freely and openly under the XX policy. You may use this data for any purpose you would like.

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
