#! python3

import requests, os, bs4

url = "https://xkcd.com/"  # starting url
os.makedirs("xkcd", exist_ok=True)  # store comics in ./xkcd

while not url.endswith("#"):
    # Download the page.
    print(f"Downloading page {url}...")
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # Find the URL of the comic image.
    comic_elem = soup.select("#comic img")
    if comic_elem == []:
        print("Could not find comic image.")
    else:
        comic_url = "https:" + comic_elem[0].get("src")
        # Download the image.
        print(f"Downloading image {comic_url}...")
        res = requests.get(comic_url)
        res.raise_for_status()

    # Find the URL of the comic image.
    comic_elem = soup.select("#comic img")
    if comic_elem == []:
        print("Could not find comic image.")
    else:
        comic_url = "https:" + comic_elem[0].get("src")
        # Download the image.
        print(f"Downloading image {comic_url}")

        try:
            res = requests.get(comic_url)
            res.raise_for_status()

            # Save the image to ./xkcd.
            imageFile = open(os.path.join("xkcd", os.path.basename(comic_url)), "wb")
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

        except requests.exceptions.InvalidURL:
            print("Invalid URL, it's probably not a comic. Skipping...")

    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = "https://xkcd.com" + prevLink.get("href")

print("Done.")
