# ASF On AWS Open Data

This is a repository to keep a record of and track how the Alaska Satellite Facility (ASF) 
provides and manages data on AWS OpenData.

Below is a list of datasets we currently maintain. For adding a new dataset, see: 
[add-a-new-dataset.md](docs/add-a-new-dataset.md).

## Datasets

### [Disaster Events](asf-event-data)

Synthetic Aperture Radar (SAR) data is a powerful tool for monitoring and assessing disaster events 
and can provide valuable insights for researchers, scientists, and emergency response teams. 
The Alaska Satellite Facility (ASF) curates this collection of (primarily) SAR and SAR-derived satellite data 
products from a variety of data sources for disaster events.

This dataset is hosted in the `s3://asf-event-data` bucket on AWS. For more information, see 
[the listing on AWS OpenData](https://registry.opendata.aws/asf-event-data/), which is manged by 
[this YAML](https://github.com/awslabs/open-data-registry/blob/main/datasets/asf-event-data.yaml).

#### Management

On a merge to main, [deploy-asf-event-data-files.yml](.github/workflows/deploy-asf-event-data-files.yml) 
will upload the following to the `s3://asf-event-data` bucket:
* `asf-event-data/README.html`, which is automatically created from [`asf-event-data/README.md`](asf-event-data/README.md)
* `asf-event-data/index.html`, which is automatically created from [`shared/index.html`](shared/index.html)

### [HAND](glo-30-hand)

Height Above Nearest Drainage (HAND) is a terrain model that normalizes topography to the relative heights 
along the drainage network and is used to describe the relative soil gravitational potentials or the 
local drainage potentials. Each pixel value represents the vertical distance to the nearest drainage. 
The HAND data provides near-worldwide land coverage at 30 meters and was produced from the 2021 release of the 
Copernicus GLO-30 Public DEM as distributed in the Registry of Open Data on AWS.

This dataset is hosted in the `s3://glo-30-hand` bucket on AWS. For more information, see 
[the listing on AWS OpenData](https://registry.opendata.aws/glo-30-hand/), which is manged by 
[this YAML](https://github.com/awslabs/open-data-registry/blob/main/datasets/glo-30-hand.yaml).

#### Management

On a merge to main, [deploy-glo-30-hand-files.yml](.github/workflows/deploy-glo-30-hand-files.yml) will upload 
the following to the `s3://glo-30-hand` bucket:
* `glo-30-hand/readme.html`, which is automatically created from [`glo-30-hand/readme.md`](glo-30-hand/readme.md)
* `glo-30-hand/index.html`, which is automatically created from [`shared/index.html`](shared/index.html)

### [ITS_LIVE](its-live-data)

The Inter-mission Time Series of Land Ice Velocity and Elevation (ITS_LIVE) project has a singular mission: 
to accelerate ice sheet and glacier research by producing globally comprehensive, high resolution, low latency, 
temporally dense, multi-sensor records of land ice and ice shelf change, while minimizing barriers between the data 
and the user.

This dataset is hosted in the `s3://its-live-data` bucket on AWS. For more information, more information, see 
[the listing on AWS OpenData](https://registry.opendata.aws/its-live-data/), which is manged by 
[this YAML](https://github.com/awslabs/open-data-registry/blob/main/datasets/its-live-data.yaml).

On a merge to main, [deploy-its-live-data-files.yml](.github/workflows/deploy-its-live-data-files.yml) will upload 
the following to the `s3://its-live-data` bucket:
* `its-live-data/README.html`, which is automatically created from [`its-live-data/README.md`](its-live-data/README.md)
* `its-live-data/index.html`, which is automatically created from [`shared/index.html`](shared/index.html)

### [S1-Orbits](s1-orbits)

The Sentinel-1 Orbits project aims to create a fast, reliable, and easy-to-access dataset containing POEORB 
and RESORB orbit metadata files for Sentinel-1. This dataset includes all POEORB files, and it also includes 
RESORB files from the last 90 days. The most recent orbit files are added to this dataset within 20 minutes 
of their publication to the [Copernicus Dataspace Ecosystem](https://documentation.dataspace.copernicus.eu/Data/SentinelMissions/Sentinel1.html). 

This dataset is hosted in the `s3://s1-orbits` bucket on AWS. For more information, more information, see 
[the listing on AWS OpenData](https://registry.opendata.aws/s1-orbits/), which is manged by 
[this YAML](https://github.com/awslabs/open-data-registry/blob/main/datasets/s1-orbits.yaml).

#### Management

On a PR to main, [deploy-s1-orbits-files-test.yml](.github/workflows/deploy-s1-orbits-files-test.yml) 
uploads to the `s3://s1-orbits-test` bucket, and on a merge to main, 
[deploy-s1-orbits-files-prod.yml](.github/workflows/deploy-s1-orbits-files-prod.yml) 
uploads the following to the `s3://s1-orbits` bucket:
* `s1-orbits/README.html`, which is automatically created from [`s1-orbits/README.md`](s1-orbits/README.md)
* `s1-orbits/index.html`, which is automatically created from [`shared/index.html`](shared/index.html) 