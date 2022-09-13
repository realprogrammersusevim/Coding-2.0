#! python3

import requests, os, bs4, threading
from tqdm import tqdm

url = "https://xkcd.com/"  # starting url
os.makedirs("xkcd", exist_ok=True)  # store comics in ./xkcd


def download_comic(start_url, end_url):
    global url
    # Download the page.
    for url_num in tqdm(range(start_url, end_url)):
        res = requests.get(f"{url}/{url_num}/")
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, "html.parser")

        # Find the URL of the comic image.
        comic_elem = soup.select("#comic img")
        if comic_elem == []:
            print("Could not find comic image.", end="\r")
        else:
            comic_url = "https:" + str(comic_elem[0].get("src"))
            # Download the image.
            res = requests.get(comic_url)
            res.raise_for_status()

        # Find the URL of the comic image.
        comic_elem = soup.select("#comic img")
        if comic_elem == []:
            print("Could not find comic image.")
        else:
            comic_url = "https:" + str(comic_elem[0].get("src"))
            # Download the image.

            try:
                res = requests.get(comic_url)
                res.raise_for_status()

                # Save the image to ./xkcd.
                imageFile = open(
                    os.path.join("xkcd", os.path.basename(comic_url)), "wb"
                )
                for chunk in res.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()

            except requests.exceptions.InvalidURL:
                print("Invalid URL, it's probably not a comic. Skipping...")

        # Get the Prev button's url.
        prevLink = soup.select('a[rel="prev"]')[0]
        url = "https://xkcd.com" + str(prevLink.get("href"))


# Create and start the Thread objects.
threads = []
for i in range(0, 140, 10):
    start = i
    end = i + 10
    if start == 0:
        start = 1

    download_thread = threading.Thread(target=download_comic, args=(start, end))
    threads.append(download_thread)
    download_thread.start()

# Wait for all threads to end.
for thread in threads:
    thread.join()

print("Done.")
