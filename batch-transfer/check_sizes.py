import argparse
import json
import os
import subprocess
from glob import glob


def download_inventory(name: str, manifest_path: str) -> str:
    if not os.path.exists(f'{name}-inventory/'):
        os.mkdir(f'{name}-inventory/')

    subprocess.run(
        ['aws', '--profile', 'its-live', 's3', 'cp',
         f's3://its-live-project/{manifest_path}',
         f'{name}-manifest.json'],
        check=True
    )
    with open(f'{name}-manifest.json') as f:
        manifest = json.load(f)

    keys = [file['key'] for file in manifest['files']]
    for count, key in enumerate(keys, start=1):
        print(f'{count}/{len(keys)}')
        if not os.path.exists(f'{name}-inventory/{key.split("/")[-1]}'):
            subprocess.run(
                ['aws', '--profile', 'its-live', 's3', 'cp',
                 f's3://its-live-project/{key}',
                 f'{name}-inventory/'],
                check=True
            )
        else:
            print('Already exists, skipping download')

    return f'{name}-inventory'


def include_key_open(key: str) -> bool:
    return True


def include_key_data_for_open(key: str) -> bool:
    open_prefixes = [
        'autorift_parameters/',
        'catalog_geojson/',
        'composites/',
        'datacubes/',
        'documentation/',
        'height_change/',
        'ice_masks/',
        'mosaics/',
        'qgis_project/',
        'rgb_mosaics/',
        'vel_web_tiles/',
        'velocity_image_pair/landsatOLI/',
        'velocity_image_pair/sentinel1/',
        'velocity_image_pair/sentinel2/',
        'velocity_mosaic/',
    ]
    return any(key.startswith(prefix) for prefix in open_prefixes)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', choices=['actual-open', 'expected-open'])
    args = parser.parse_args()

    if args.cmd == 'actual-open':
        path = download_inventory(
            'open',
            's3-inventory//its-live-open/its-live-open-inventory/2024-01-03T01-00Z/manifest.json'
        )
        include_key = include_key_open
    elif args.cmd == 'expected-open':
        path = download_inventory(
            'data',
            's3-inventory/its-live-data/its-live-data-inventory/2024-01-02T01-00Z/manifest.json'
        )
        include_key = include_key_data_for_open
    else:
        raise ValueError(f'Command {args.cmd} not recognized')

    total = 0
    gzfiles = glob(f'{path}/*.csv.gz')
    for count, gzfile in enumerate(gzfiles, start=1):
        print(f'{count}/{len(gzfiles)} {gzfile}')
        subprocess.run(['gunzip', '--keep', gzfile], check=True)
        csvfile = gzfile.removesuffix('.gz')
        with open(csvfile) as f:
            for line in f:
                row = line.strip('\n').split(',')
                key = row[1].strip('"')
                if include_key(key):
                    total += int(row[2].strip('"'))
                    print(total, end='\r')
        print()
        os.remove(csvfile)
    print(f'Total size: {total}')


if __name__ == '__main__':
    main()
