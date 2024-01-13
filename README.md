# AWS Open Data managed by the Alaska Satellite Facility's Tools Team

This is a repository to keep a record of and track how we provide and manage data on AWS OpenData.

## Datasets

### [Disaster Events](events)

synthetic Aperture Radar (SAR) data is a powerful tool for monitoring and assessing disaster events and can provide valuable insights for researchers, scientists, and emergency response teams. The Alaska Satellite Facility (ASF) curates this collection of (primarily) SAR and SAR-derived satellite data products from a variety of data sources for disaster events.

This dataset is hosted in the `s3://asf-event-data` bucket on AWS. For more information, see: [the listing on AWS OpenData](https://registry.opendata.aws/asf-event-data/), which is manged by [this YAML](https://github.com/awslabs/open-data-registry/blob/main/datasets/asf-event-data.yaml).

#### Management

On a merge to main, [deploy-events-readme.yml](.github/workflows/deploy-events-readme.yml) will upload to the `s3://asf-event-data` bucket:
* `events/README.html`, which is automatically created from [`events/README.md`](events/README.md)
* `events/index.html`, which is automatically created from [`shared/index.html`](shared/index.html)
