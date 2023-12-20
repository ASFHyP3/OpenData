import json
import os
import subprocess
from glob import glob


def download_inventory(name: str, manifest_path: str) -> str:
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
        print(f'{count}/{len(keys)} {key}')
        subprocess.run(
            ['aws', '--profile', 'its-live', 's3', 'cp',
             f's3://its-live-project/{key}',
             f'{name}-inventory/'],
            check=True
        )

    return f'{name}-inventory'


def main():
    path = download_inventory(
        'open',
        's3-inventory//its-live-open/its-live-open-inventory/2023-12-19T01-00Z/manifest.json'
    )
    total = 0
    gzfiles = glob(f'{path}/*.csv.gz')
    for count, gzfile in enumerate(gzfiles, start=1):
        print(f'{count}/{len(gzfiles)} {gzfile}')
        subprocess.run(['gunzip', gzfile], check=True)
        csvfile = gzfile.removesuffix('.gz')
        with open(csvfile) as f:
            for line in f:
                total += int(line.strip('\n').split(',')[2].strip('"'))
                print(total, end='\r')
        print()
        os.remove(csvfile)
    print(f'Total size: {total}')


if __name__ == '__main__':
    main()
