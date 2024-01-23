# AWS Open Data managed by the Alaska Satellite Facility's Tools Team

This is a repository to keep a record of and track how we provide and manage data on AWS OpenData.

Below is a list of datasets we currently maintain. For adding a new dataset, see: [add-a-new-dataset.md](docs/add-a-new-dataset.md).

## Datasets

### [Disaster Events](asf-event-data)

synthetic Aperture Radar (SAR) data is a powerful tool for monitoring and assessing disaster events and can provide valuable insights for researchers, scientists, and emergency response teams. The Alaska Satellite Facility (ASF) curates this collection of (primarily) SAR and SAR-derived satellite data products from a variety of data sources for disaster events.

This dataset is hosted in the `s3://asf-event-data` bucket on AWS. For more information, see: [the listing on AWS OpenData](https://registry.opendata.aws/asf-event-data/), which is manged by [this YAML](https://github.com/awslabs/open-data-registry/blob/main/datasets/asf-event-data.yaml).

#### Management

On a merge to main, [deploy-asf-event-data-files.yml](.github/workflows/deploy-asf-event-data-files.yml) will upload to the `s3://asf-event-data` bucket:
* `asf-event-data/README.html`, which is automatically created from [`asf-event-data/README.md`](asf-event-data/README.md)
* `asf-event-data/index.html`, which is automatically created from [`shared/index.html`](shared/index.html)

### [HAND](glo-30-hand)

Height Above Nearest Drainage (HAND) is a terrain model that normalizes topography to the relative heights along the drainage network and is used to describe the relative soil gravitational potentials or the local drainage potentials. Each pixel value represents the vertical distance to the nearest drainage. The HAND data provides near-worldwide land coverage at 30 meters and was produced from the 2021 release of the Copernicus GLO-30 Public DEM as distributed in the Registry of Open Data on AWS.

This dataset is hosted in the `s3://glo-30-hand` bucket on AWS. For more information, see: [the listing on AWS OpenData](https://registry.opendata.aws/glo-30-hand/), which is manged by [this YAML](https://github.com/awslabs/open-data-registry/blob/main/datasets/glo-30-hand.yaml).

#### Management

On a merge to main, [deploy-glo-30-hand-files.yml](.github/workflows/deploy-glo30-hand-files.yml) will upload to the `s3://glo-30-hand` bucket:
* `glo-30-hand/readme.html`, which is automatically created from [`glo-30-hand/readme.md`](glo-30-hand/readme.md)
* `glo-30-hand/index.html`, which is automatically created from [`shared/index.html`](shared/index.html)

### [ITS_LIVE](its-live-data)

The Inter-mission Time Series of Land Ice Velocity and Elevation (ITS-LIVE) project has a singular mission: to accelerate ice sheet and glacier research by producing globally comprehensive, high resolution, low latency, temporally dense, multi-sensor records of land ice and ice shelf change, while minimizing barriers between the data and the user.

This dataset is hosted in the `s3://its-live-data` bucket on AWS. For more information, more information, see: [the listing on AWS OpenData](https://registry.opendata.aws/its-live-data/), which is manged by [this YAML](https://github.com/awslabs/open-data-registry/blob/main/datasets/its-live-data.yaml).

On a merge to main, [deploy-its-live-data-files.yml](.github/workflows/deploy-its-live-data-files.yml) will upload to the `s3://its-live-data` bucket:
* `its-live-data/README.html`, which is automatically created from [`its-live-data/README.md`](its-live-data/README.md)
* `its-live-data/index.html`, which is automatically created from [`shared/index.html`](shared/index.html)
