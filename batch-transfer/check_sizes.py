import json
import os
import subprocess


def download_inventory(name: str, manifest_path: str) -> None:
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
    print('Unzipping...')
    subprocess.run(['gunzip', f'{name}-inventory/*.gz'], check=True)


def main():
    download_inventory(
        'open',
        's3-inventory//its-live-open/its-live-open-inventory/2023-12-19T01-00Z/manifest.json'
    )


if __name__ == '__main__':
    main()
