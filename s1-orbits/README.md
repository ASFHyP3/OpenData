# Sentinel-1 Precise Orbit Determination (POD) Products

Sentinel-1 Precise Orbit Determination (POD) products contain auxiliary data on satellite position/velocity for the European Space Agency's (ESA) Sentinel-1 satellite constellation and are a necessary input for nearly all Sentinel-1 data processing workflows. Sentinel-1 is a C-band Synthetic Aperture Radar (SAR) satellite constellation first launched by ESA in 2014 as part of the European Union's Copernicus Earth Observation programme.

This dataset includes two types of POD files that are both redistributed from ESA; RESORB and POEORB. RESORB POD files are restituted orbit files generated within 180 min from sensing time and distributed daily, with accuracy requirement of 10 cm in 2D RMS, but typically below 5 cm. RESORB POD files from the last 90 days are included in this dataset. POEORB POD files are precise orbit files generated with a timeliness of 20 days from sensing time and distributed daily, with accuracy requirement of 5 cm in 3D RMS, but typically below 1 cm. Once available, these files supersede the RESORB products, as they contain the same data with better accuracy. These products are available from the entire length of the Sentinel-1 mission. The most recent POD files are added to this dataset within 20 minutes of their publication to the [Copernicus Dataspace Ecosystem](https://documentation.dataspace.copernicus.eu/Data/ComplementaryData/Additional.html#sentinel-1-orbits).
  For more information on the orbit products, see the [POD Sentinel-1 Products Specification](https://sentiwiki.copernicus.eu/web/s1-processing#S1Processing-PODSentinel-1ProductsSpecificationS1-Processing-POD-Sentinel-1-Products-Specification).

[Sentinel-1 POD Orbit Products on the Registry of Open Data on AWS](https://registry.opendata.aws/s1-orbits/).

## File Organization

TODO - naming convention
TODO - include lifecycle for RESORB

The Sentinel-1 Orbits dataset is located in the public `s1-orbits` AWS S3 bucket. The dataset is organized into two folders seperating the two orbit types:
* `POEORB/`: The precise orbit ephemerides (POE) data. This is the most precise orbit data and can take a couple days to be created.
* `RESORB/`: The restituded orbit data. This data is less precise and is uploaded the same day as an aquisition. 

### File Naming Convention
The file name convention for these products is:

`sss_OPER_AUX_tttttt_OPOD_creation_Vstart_stop.EOF`

Where:
- `sss` is the satellite platform (`S1A` or `S1B`)
- `tttttt` is the orbit type (`POEORB` or `RESORB`)
- `creation` is the creation date of the file, in CCSDS compact format (`YYYYMMDDTHHMMSS`)
- `start` is the validity start time of the data contained in the file, in CCSDS compact format (`YYYYMMDDTHHMMSS`)
- `stop` is the validity stop time of the data contained in the file, in CCSDS compact format (`YYYYMMDDTHHMMSS`)

For example, `S1A_OPER_AUX_POEORB_OPOD_20230821T080724_V20230731T225942_20230802T005942.EOF` Is a POEORB POD file for the Sentinel-1A satellite containing data between July 31, 2023 22:59:42 UTC and Aug 2, 2023 00:59:42 UTC. The POD file was created on Aug 21, 2023 at 08:07:24 UTC.

## Tools

### AWS S3 Explorer

Browse the contents of the `s1-orbits` bucket in a browser by vising https://s1-orbits.s3.amazonaws.com/index.html

### Python Library

[s1_orbits](https://pypi.org/project/s1-orbits/) is a Python library for downloading the best available orbit for a given Sentinel-1 scene.

```python
>>> import s1_orbits

>>> orbit_file = s1_orbits.fetch_for_scene('S1A_IW_SLC__1SDV_20230727T075102_20230727T075131_049606_05F70A_AE0A')
>>> orbit_file
PosixPath('S1A_OPER_AUX_POEORB_OPOD_20230816T080815_V20230726T225942_20230728T005942.EOF')
```

### REST API

For those working outside of Python, https://s1-orbits.asf.alaska.edu/ui provides a REST API for downloading the best available orbit for a given Sentinel-1 scene.

`https://s1-orbits.asf.alaska.edu/scene/S1A_IW_SLC__1SDV_20230727T075102_20230727T075131_049606_05F70A_AE0A`

### SNS Subscriptions

We provide an SNS topic providing push notifications when new file are added to the `s1-orbits` S3 bucket. The topic supports SQS and Lambda subscriptions. 

Topic ARN: `arn:aws:sns:us-west-2:211125554030:s1-orbits-object_created`

You can subscribe to this topic using the [sns subscribe](https://docs.aws.amazon.com/cli/latest/reference/sns/subscribe.html) method of the [AWS CLI](https://aws.amazon.com/cli/):

```commandline
# lambda subscription
aws sns subscribe --topic-arn arn:aws:sns:us-west-2:211125554030:s1-orbits-object_created --protocol lambda --notification-endpoint <lambda_arn>

# sqs subscription
aws sns subscribe --topic-arn arn:aws:sns:us-west-2:211125554030:s1-orbits-object_created --protocol sqs --notification-endpoint <queue_arn>
```

## License

TODO

## Contact

If you have questions about how the data is managed on AWS, please email the [ASF Tools Team](mailto:uaf-asf-apd@alaska.edu).
