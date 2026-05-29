#!/usr/bin/env python3
# Downloads all Playfull Labs images (full-resolution) into static/images/.
# No installs needed. Run from your Hugo site root:  python3 download_images.py
import os, urllib.request

os.makedirs("static/images", exist_ok=True)
IMAGES = [
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1445548564899-FXR5JOICJQ4YTFBFO2LC/image-asset.jpeg?format=original", "sifting-the-silence-a-sarajevo-story-1.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1445548646141-WONCFW9MS0RXXJIY1WIO/image-asset.jpeg?format=original", "sifting-the-silence-a-sarajevo-story-2.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1445552794983-NT2HD1E1ZW8H8YBAVF9A/image-asset.jpeg?format=original", "sifting-the-silence-a-sarajevo-story-3.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1445552472616-117YSZOVP0T96UOK53C1/image-asset.jpeg?format=original", "sifting-the-silence-a-sarajevo-story-4.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1437430370869-D95VCF36UO1C8MVWRS19/image-asset.jpeg?format=original", "feetprints-r-us-1.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1437436059011-5SO7OMFF6Z5LT6RWG3V6/image-asset.jpeg?format=original", "feetprints-r-us-2.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1437436289151-W3CF3YZ58NY6OY9E9L3T/image-asset.jpeg?format=original", "feetprints-r-us-3.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1437436389085-VDIPFP95QG5X5VOH411R/image-asset.jpeg?format=original", "feetprints-r-us-4.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1437436520566-DQE0ZFKS1MGJOXCV0MSO/image-asset.jpeg?format=original", "feetprints-r-us-5.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1437436654354-R33EUSV6KSUGDL3O7IPC/image-asset.jpeg?format=original", "feetprints-r-us-6.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1437436718279-Z3YDS09O1HY56PZJYC5H/image-asset.jpeg?format=original", "feetprints-r-us-7.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1437436765130-ZDS9MQW1JOMIL2VYLGY7/image-asset.jpeg?format=original", "feetprints-r-us-8.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1437436959292-Q4EVP4AHZCY30UJJXAVJ/static1.squarespace-8.jpg?format=original", "feetprints-r-us-9.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1437437092503-M254FEC8ZD2K8ZM1MYHB/image-asset.jpeg?format=original", "feetprints-r-us-10.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1437437042294-S4I2NTLYWWJ2VSEP7T0Y/image-asset.jpeg?format=original", "feetprints-r-us-11.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1437436992522-7R9XKPOQOKJHW4JY44JO/image-asset.jpeg?format=original", "feetprints-r-us-12.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1437437243706-M996IRIPEJXRWJPR18J2/image-asset.jpeg?format=original", "feetprints-r-us-13.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1437437263776-8E579RSSWJGDRQ1KCZIG/image-asset.jpeg?format=original", "feetprints-r-us-14.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1437437586439-YMFOPLJEK5140EMBG4PI/image-asset.jpeg?format=original", "feetprints-r-us-15.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1437437344869-SBSDTKWL45HTK7OV671G/image-asset.jpeg?format=original", "feetprints-r-us-16.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1437437437021-858DVLY4IJX9ZV39ACYN/image-asset.jpeg?format=original", "feetprints-r-us-17.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1437437815987-C1ZRJ8JTY10ISE6UY6EU/image-asset.jpeg?format=original", "feetprints-r-us-18.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1437437844082-OGRRBJKMU9B21PAE1Q9S/image-asset.jpeg?format=original", "feetprints-r-us-19.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1453230488509-K72FTO57MDGMY6FHYY7F/image-asset.jpeg?format=original", "sliced-bread-and-bananas-1.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1453407102379-08UQ4C9GRP23ANU9WO7H/image-asset.png?format=original", "david-bowie-heroes-of-invention-1.png"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1455666226165-ZB5MFYLRQY28ID7LJJF8/image-asset.png?format=original", "intersecting-theatrics-and-gameplay-1.png"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1508161400879-RJ5UAT6274F59P710347/IMG_2132.jpg?format=original", "a-world-of-joy-and-colored-pencils-1.jpg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1501338303337-Q8QSZRNS2O44RF0RCA3A/image-asset.png?format=original", "tenacity-of-an-entrepreneurial-spirit-1.png"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1501339074619-PZWRNGU5ZEIM7Y9UAMCY/image-asset.jpeg?format=original", "tenacity-of-an-entrepreneurial-spirit-2.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1501339270827-K9DBF4I12BNNO6RS7280/image-asset.jpeg?format=original", "tenacity-of-an-entrepreneurial-spirit-3.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1501763664372-HI0Z68GJRPBCN15GE8MI/image-asset.jpeg?format=original", "tenacity-of-an-entrepreneurial-spirit-4.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1501764166294-VFNKL7NM6C9PZEJ8VD6F/image-asset.jpeg?format=original", "tenacity-of-an-entrepreneurial-spirit-5.jpeg"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1523277169322-YDQ2PHL1JOW0020MGHPQ/IMG_0600.png?format=original", "design-re-imagined-1.png"),
    ("https://images.squarespace-cdn.com/content/v1/5565f3eee4b05ab00974ecf1/1588615126528-PF7A53XPN2HOQH5J92RR/Kindergarten_Tangshui_China_SAKOArchitects.jpg?format=original", "a-letter-to-our-futures-futurists-1.jpg"),
]

ok=fail=0
for url, fname in IMAGES:
    dest = os.path.join("static", "images", fname)
    if os.path.exists(dest):
        print("skip (already have)", fname); ok+=1; continue
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read()
        with open(dest, "wb") as f:
            f.write(data)
        print("saved", fname, "(%d KB)" % (len(data)//1024)); ok+=1
    except Exception as e:
        print("FAILED", fname, "->", e); fail+=1

print("\nDone. %d ok, %d failed, %d total." % (ok, fail, len(IMAGES)))
