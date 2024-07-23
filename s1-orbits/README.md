# Sentinel-1 Orbit Data

The Sentinel-1 Orbits project aims to create a fast, reliable, and easy to access dataset containing POEORB and RESORB orbit metadata files for Sentinel-1. This dataset includes all POEORB files, and it also includes RESORB files from the last 90 days. The most recent orbit files are added to this dataset within 20 minutes of their publication to the [Copernicus Dataspace Ecosystem](https://documentation.dataspace.copernicus.eu/Data/SentinelMissions/Sentinel1.html). 

For more information on the orbit products, see the [Copernicus POD Specification](https://sentinels.copernicus.eu/documents/d/sentinel/copernicus-pod-service-file-format-specification).

## Accessing the Sentinel-1 Orbit Data

The Sentinel-1 Orbits dataset is located in the public `s1-orbits` AWS S3 bucket. The dataset is organized into two folders seperating the two orbit types:
* `POEORB/`: The precise orbit ephemerides (POE) data. This is the most precise orbit data and can take a couple days to be created.
* `RESORB/`: The restituded orbit data. This data is less precise and is uploaded the same day as an aquisition. 

## Contact

...

## License

...

---

[Registry of Open Data on AWS](https://registry.opendata.aws/)