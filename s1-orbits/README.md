# Sentinel-1 Precise Orbit Determination (POD) Products

Sentinel-1 Precise Orbit Determination (POD) products contain auxiliary data on satellite position and velocity for the European Space Agency's (ESA) Sentinel-1 mission. Sentinel-1 is a C-band Synthetic Aperture Radar (SAR) satellite constellation first launched in 2014 as part of the European Union's Copernicus Earth Observation programme. POD products are a necessary auxiliary input for nearly all Sentinel-1 data processing workflows.

This dataset is a mirror of the [Sentinel-1 Orbits](https://documentation.dataspace.copernicus.eu/Data/ComplementaryData/Additional.html#sentinel-1-orbits) dataset hosted in the Copernicus Data Space Ecosystem (CDSE). New files are added within 20 minutes of their publication to CDSE. This dataset includes two types of POD files: RESORB and POEORB.

- RESORB POD files are restituted orbit files generated within 180 minutes from sensing time and published multiple times per day, with accuracy requirement of 10 cm in 2D RMS, but typically below 5 cm. RESORB products from the last 90 days are included in this dataset.

- POEORB POD files are precise orbit files generated with a timeliness of 20 days from sensing time and published once per day, with accuracy requirement of 5 cm in 3D RMS, but typically below 1 cm. Once available, these files supersede the RESORB products, as they contain the same data with better accuracy. POEORB products are available from the entire length of the Sentinel-1 mission.

For more information on the orbit products, see the [POD Sentinel-1 Products Specification](https://sentiwiki.copernicus.eu/web/s1-processing#S1Processing-PODSentinel-1ProductsSpecificationS1-Processing-POD-Sentinel-1-Products-Specification).

[Sentinel-1 POD Products on the Registry of Open Data on AWS](https://registry.opendata.aws/s1-orbits/).

## File Organization

All data files are located in the public `s1-orbits` AWS S3 bucket. Files are organized under two prefixes separating the two file types:

```commandline
s1-orbits/
    AUX_POEORB/
        S1A_OPER_AUX_POEORB_OPOD_20210203T122423_V20210113T225942_20210115T005942.EOF
        S1A_OPER_AUX_POEORB_OPOD_20210204T122413_V20210114T225942_20210116T005942.EOF
        S1A_OPER_AUX_POEORB_OPOD_20210205T122416_V20210115T225942_20210117T005942.EOF
        ...
        S1B_OPER_AUX_POEORB_OPOD_20210203T112353_V20210113T225942_20210115T005942.EOF
        S1B_OPER_AUX_POEORB_OPOD_20210204T112355_V20210114T225942_20210116T005942.EOF
        S1B_OPER_AUX_POEORB_OPOD_20210205T112344_V20210115T225942_20210117T005942.EOF
        ...
    AUX_RESORB/
        S1A_OPER_AUX_RESORB_OPOD_20231002T140558_V20231002T102001_20231002T133731.EOF
        S1A_OPER_AUX_RESORB_OPOD_20231002T154251_V20231002T115846_20231002T151616.EOF
        S1A_OPER_AUX_RESORB_OPOD_20231002T171753_V20231002T133730_20231002T165500.EOF
        ...
```

### File Naming Convention

The file name convention for these products is `sss_OPER_AUX_tttttt_OPOD_creation_Vstart_stop.EOF`, where:
- `sss` is the satellite platform (`S1A` or `S1B`)
- `tttttt` is the orbit type (`POEORB` or `RESORB`)
- `creation` is the creation date of the file, in CCSDS compact format (`YYYYMMDDTHHMMSS`)
- `start` is the validity start time of the data contained in the file, in CCSDS compact format (`YYYYMMDDTHHMMSS`)
- `stop` is the validity stop time of the data contained in the file, in CCSDS compact format (`YYYYMMDDTHHMMSS`)

For example, `S1A_OPER_AUX_POEORB_OPOD_20230821T080724_V20230731T225942_20230802T005942.EOF` is a POEORB POD file for the Sentinel-1A satellite containing data between July 31, 2023 22:59:42 UTC and Aug 2, 2023 00:59:42 UTC. The POD file was created on Aug 21, 2023 at 08:07:24 UTC.

## Tools Supporting Data Access

### AWS S3 Explorer

Browse the contents of the `s1-orbits` bucket in a browser by vising [https://s1-orbits.s3.amazonaws.com/index.html](https://s1-orbits.s3.amazonaws.com/index.html)

### Python Library

[s1_orbits](https://pypi.org/project/s1-orbits/) is a Python library for downloading the best available orbit for a given Sentinel-1 scene.

```python
>>> import s1_orbits

>>> orbit_file = s1_orbits.fetch_for_scene('S1A_IW_SLC__1SDV_20230727T075102_20230727T075131_049606_05F70A_AE0A')
>>> orbit_file
PosixPath('S1A_OPER_AUX_POEORB_OPOD_20230816T080815_V20230726T225942_20230728T005942.EOF')
```

### REST API

For those working outside of Python, [https://s1-orbits.asf.alaska.edu/ui](https://s1-orbits.asf.alaska.edu/ui) provides a REST API for downloading the best available orbit for a given Sentinel-1 scene.

[https://s1-orbits.asf.alaska.edu/scene/S1A_IW_SLC__1SDV_20230727T075102_20230727T075131_049606_05F70A_AE0A](https://s1-orbits.asf.alaska.edu/scene/S1A_IW_SLC__1SDV_20230727T075102_20230727T075131_049606_05F70A_AE0A)

### SNS Subscriptions

The SNS topic `arn:aws:sns:us-west-2:211125554030:s1-orbits-object_created` provides push notifications when new files are added to the `s1-orbits` S3 bucket. The topic supports SQS and Lambda subscriptions.

- To subscribe a Lambda Function, see [Invoking Lambda functions with Amazon SNS notifications](https://docs.aws.amazon.com/lambda/latest/dg/with-sns.html).
- To subscribe an SQS Queue, see [Subscribing a queue to an Amazon SNS topic using the Amazon SQS console](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-subscribe-queue-sns-topic.html).

SNS messages conform to the S3 [event message structure](https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-content-structure.html).

## License

Access to Sentinel data is free, full and open for the broad Regional, National, European and International user community. View [Terms and Conditions](https://dataspace.copernicus.eu/terms-and-conditions).

## Contact

If you have questions about how the data is managed on AWS, please email the [ASF Tools Team](mailto:uaf-asf-apd@alaska.edu).
