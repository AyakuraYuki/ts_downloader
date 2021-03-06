# -*- coding: utf-8 -*-

import os
from time import sleep

from driver import chrome, process
from proxy import ProxyOption
from util import cleanup_download_temporary_cache, create_folder, validate

m3u8_url = ''
key_url = ''
user_home = os.path.expanduser('~')
download_dir = os.path.join(user_home, 'Music', 'ts_radio_music_life')


def main():
    driver = chrome(download_dir, proxy=ProxyOption())
    driver.get(key_url)
    driver.get(m3u8_url)
    process(driver=driver, dest_dir=download_dir, m3u8_url=m3u8_url, host_url='', min_wait=3, max_wait=5)


if __name__ == '__main__':
    create_folder(download_dir)
    while True:
        try:
            cleanup_download_temporary_cache(download_dir)
            main()
        except Exception as e:
            print('Exception occurred, restarting...')
            print(f'Error: {e}')
            cleanup_download_temporary_cache(download_dir)
            sleep(10)
        else:
            break
    validate(download_dir)
    print('Done!')
