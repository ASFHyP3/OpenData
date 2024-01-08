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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', choices=['open', 'data'])
    args = parser.parse_args()

    manifest_path = {
        'open': 's3-inventory//its-live-open/its-live-open-inventory/2024-01-08T01-00Z/manifest.json',
        'data': 's3-inventory//its-live-data/its-live-data-inventory-new/2024-01-08T01-00Z/manifest.json',
    }[args.cmd]

    path = download_inventory(args.cmd, manifest_path)

    total_size = 0
    total_keys = 0
    gzfiles = glob(f'{path}/*.csv.gz')
    for count, gzfile in enumerate(gzfiles, start=1):
        print(f'{count}/{len(gzfiles)} {gzfile}')
        subprocess.run(['gunzip', '--keep', gzfile], check=True)
        csvfile = gzfile.removesuffix('.gz')
        with open(csvfile) as f:
            for line in f:
                row = line.strip('\n').split(',')
                total_size += int(row[2].strip('"'))
                total_keys += 1
                print(total_size, total_keys, end='\r')
        print()
        os.remove(csvfile)
    print(f'Total size: {total_size}')
    print(f'Total keys: {total_keys}')


if __name__ == '__main__':
    main()
