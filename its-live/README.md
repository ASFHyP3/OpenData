# Inter-mission Time Series of Land Ice Velocity and Elevation (ITS-LIVE) dataset

The Inter-mission Time Series of Land Ice Velocity and Elevation (ITS-LIVE) project has a singular mission: to accelerate ice sheet and glacier research by producing globally comprehensive, high resolution, low latency, temporally dense, multi-sensor records of land ice and ice shelf change, while minimizing barriers between the data and the user.

ITS-LIVE data consists of:
* NetCDF Level-2 scenes-pair ice flow products posted to a standard 120 m grid derived from Landsat 4/5/7/8/9 and Sentinel-2 optical scenes, and Sentinel-1 SAR scenes.
* A set of Zarr datacubes containing all scene pair data cloud-optimized for time-series analysis, with a suite of user tools available to effectively query the data.
* A suite of Level 3 products, including: quarterly and annual ice-sheet and regional velocity mosaics as Cloud-Optimized GeoTIFFs


## Accessing the ITS-LIVE data

The ITS-LIVE data is all stored is the public `its-live-data` AWS S3 bucket, which is located in the `us-west-2` (Oregon) AWS Region. 

```shell
aws s3 ls s3://its-live-data/
```

> [CAUTION!]
> There are over 1 billion objects in the `its-live-data` bucket. Recursively listing the whole bucket is **not** recommended.

The data is organized under a collection of prefixes (folders) to ease access, which are described below. We've **bolded** the prefixes which are typically of the most interest to users:

* `L7_PV_fix/`: 
* `NSIDC/`: 
* `Test/`: 
* `autorift_parameters/`: 
* `catalog_geojson/`: 
* `catalog_geojson_latest/`: 
* `catalog_geojson_original/`: 
* `composites/`: 
* `datacubes/`: 
* `documentation/`: 
* `elevation/`: 
* `height_change/`: 
* `ice_masks/`: 
* `ice_shelf/`: 
* `isce_autoRIFT/`: 
* `month-data-logs/`: 
* `mosaics/`: 
* `qgis_project/`: 
* `rgb_mosaics/`: 
* `test/`: 
* `test_datacubes/`: 
* **`vel_web_tiles/`**: 
* **`velocity_image_pair/`**: 
* **`velocity_mosaic/`**: 


## License

The use of the ITS-LIVE data falls under the terms and conditions of the [Creative Commons Zero (CC0) 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) license.

---

[AWS Public Datasets](http://aws.amazon.com/public-datasets)
