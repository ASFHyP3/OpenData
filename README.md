# AWS Open Data managed by the Alaska Satellite Facility's Tools Team

This is a repository to keep a record of and track how we provide and manage data on AWS OpenData.

## Datasets

### [Disaster Events](asf-event-data)

synthetic Aperture Radar (SAR) data is a powerful tool for monitoring and assessing disaster events and can provide valuable insights for researchers, scientists, and emergency response teams. The Alaska Satellite Facility (ASF) curates this collection of (primarily) SAR and SAR-derived satellite data products from a variety of data sources for disaster events.

This dataset is hosted in the `s3://asf-event-data` bucket on AWS. For more information, see: [the listing on AWS OpenData](https://registry.opendata.aws/asf-event-data/), which is manged by [this YAML](https://github.com/awslabs/open-data-registry/blob/main/datasets/asf-event-data.yaml).

#### Management

On a merge to main, [deploy-asf-event-data-files.yml](.github/workflows/deploy-events-readme.yml) will upload to the `s3://asf-event-data` bucket:
* `asf-event-data/README.html`, which is automatically created from [`asf-event-data/README.md`](asf-event-data/README.md)
* `asf-event-data/index.html`, which is automatically created from [`shared/index.html`](shared/index.html)

### HAND

Height Above Nearest Drainage (HAND) is a terrain model that normalizes topography to the relative heights along the drainage network and is used to describe the relative soil gravitational potentials or the local drainage potentials. Each pixel value represents the vertical distance to the nearest drainage. The HAND data provides near-worldwide land coverage at 30 meters and was produced from the 2021 release of the Copernicus GLO-30 Public DEM as distributed in the Registry of Open Data on AWS.

For more information, see: [the listing on AWS OpenData](FIXME), which is manged by [this YAML](FIXME)
