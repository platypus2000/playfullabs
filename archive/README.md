# Playfull Labs — migrated content (rebuilt from Squarespace XML export)

This version was regenerated from the official Squarespace WordPress export,
so the text is the authoritative original (not a web scrape) and the images
point to full-resolution originals.

## Contents
- content/posts/*.md  — all 10 published posts (front matter: title, date,
  and an `aliases` entry preserving the old Squarespace URL so existing links
  still resolve). Images already rewritten to /images/...
- content/contact.md, content/missives.md, content/together.md — the three
  content pages that had real text in the export.
- download_images.py — downloads all 34 images (full-res) into static/images/.

## Use
1. Copy `content` into your Hugo site (merging into the existing content/).
2. From the site root:  pip install requests  &&  python download_images.py
3. hugo server   then open http://localhost:1313

## Notes
- The original prose uses "---" (three hyphens) where the author meant an em
  dash. This is preserved exactly as written. If you'd rather render real em
  dashes, do a find-and-replace of --- with the dash character; otherwise leave
  it and it stays faithful to the source.
- The export contained 4 DRAFT posts that were never published (and aren't on
  the live site), so they're excluded. Only one had any text ("This week in
  Playfull media in the news"). Say the word if you want any pulled in.
- The "Read Me" and "Blog" pages in the export are Squarespace template
  boilerplate / the auto-generated post list, so they're intentionally left out
  — Hugo builds the post list for you.
- The homepage scrolling hero ("Our imagination / is limitless") is a template
  effect, not content, so it isn't here.
# playfullabs
