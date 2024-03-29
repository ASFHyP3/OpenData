# Inter-mission Time Series of Land Ice Velocity and Elevation (ITS_LIVE) dataset

The Inter-mission Time Series of Land Ice Velocity and Elevation (ITS_LIVE) project has a singular mission: to accelerate ice sheet and glacier research by producing globally comprehensive, high resolution, low latency, temporally dense, multi-sensor records of land ice and ice shelf change while minimizing barriers between the data and the user.

ITS_LIVE data consists of:
* NetCDF Level-2 scenes-pair ice flow products posted to a standard 120 m grid derived from Landsat 4/5/7/8/9, Sentinel-2 optical scenes, and Sentinel-1 SAR scenes.
* A set of Zarr datacubes containing all scene pair data cloud-optimized for time-series analysis, with a suite of user tools available to query the data effectively.
* A suite of Level 3 products, including:
  * regional and ice-sheet-wide velocity mosaics calculated monthly and annually as Cloud-Optimized GeoTIFFs
  * Antarctic 1985-2020 satellite-derived monthly elevation change
  * Antarcitc 1992–2017 satellite-derived 3-month ice shelf thickness and basal melt posted at 3km

For more information about the ITS_LIVE project, please see <https://its-live.jpl.nasa.gov/>.

## Accessing the ITS_LIVE data

The ITS_LIVE data are all stored in the public `its-live-data` AWS S3 bucket, which is located in the `us-west-2` (Oregon) AWS Region, and organized under a collection of prefixes (folders) to ease access:
* `autorift_parameters/`: A collection of [autoRIFT](https://github.com/nasa-jpl/autoRIFT/) input parameter files used by the ITS_LIVE project to product the netCDF velocity image pairs
* `catalog_geojson/`: GeoJSON catalog of the NetCDF velocity image pairs
* `composites/`: Zarr mean annual velocities derived from the Zarr Datacubes
* `datacubes/`: Zarr DataCubes of merged image velocity data which have been cloud-optimized for time-series analysis
* `rgb_mosaics/`: Cloud-optimized GeoTIFF images derived from the NetCDF velocity mosaics for easy use in GIS applications
* `vel_web_tiles/`: [Tiled web map](https://en.wikipedia.org/wiki/Tiled_web_map) PNG images derived from the NetCDF mosaics for easy use in web applications
* `velocity_image_pair/`: NetCDF velocity images derived from optical and SAR satellite image pairs using [autoRIFT](https://github.com/nasa-jpl/autoRIFT/)
* `velocity_mosaic/`: NetCDF regionally compiled, mean annual surface velocities for major glacier-covered regions derived from the Zarr Datacubes

To list all the top-level bucket prefixes, run:

```shell
aws s3 ls s3://its-live-data/
```

> [CAUTION!]
> There are over 1 billion objects in the `its-live-data` bucket. Recursively listing the whole bucket is **not** recommended.

## Contact

If you have questions about the data itself or the processing methods used, please post in the [ITS_LIVE Community gitter](https://app.gitter.im/#/room/#its_live_community:gitter.im).

If you have questions about how the data is managed on AWS, please email the [ASF Tools Team](mailto:uaf-asf-apd@alaska.edu).

## License

The use of the ITS_LIVE data falls under the terms and conditions of the [Creative Commons Zero (CC0) 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) license.

---

[Registry of Open Data on AWS](https://registry.opendata.aws/)
