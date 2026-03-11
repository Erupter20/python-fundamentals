from bs4 import BeautifulSoup


def extract_stats(html):

    soup = BeautifulSoup(html, "lxml")

    stats = {}

    rows = soup.find_all("tr")

    for row in rows:

        cols = row.find_all("td")

        if len(cols) >= 2:

            name = cols[0].get_text(strip=True)
            value = cols[1].get_text(strip=True)

            if "$" in value:

                clean = value.replace("$", "")
                clean = clean.replace(",", "")
                clean = clean.replace("M", "000000")

                try:
                    stats[name] = int(clean)
                except:
                    continue

    return stats