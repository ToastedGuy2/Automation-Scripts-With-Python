import urllib3


def get_podcast_titles():
    http = urllib3.PoolManager()
    r = http.request(
        'GET', 'https://darknetdiaries.com/darknet-diaries-all-episode-links.txt')
    if r.status == 200:
        return r.data.decode('utf-8').strip().split("\n")


def download_podcast():
    http = urllib3.PoolManager()
    url = get_podcast_titles()[100]
    r = http.request('GET', url, preload_content=False)
    with open('/home/toastedguy2/Development/Personal Projects/Automation-Scripts-With-Python/Darknet-Diaries-Podcast-Downloader/podcast.mp3', 'wb') as out:
        while True:
            data = r.read(65536)
            if not data:
                break
            out.write(data)
    r.release_conn()


download_podcast()
