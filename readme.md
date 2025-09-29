# Distribution Repo

This repo consists of two things (note they are kind of intermingled so they are just seperate concepts...)

1. manifests folder
2. a mirror of the folder structure and files you want to distribute

When the update script is invoked, it will check the manifests in this repo. The manifests folder should contain a .md file that lists what should be fetched (which will also be where it will go). That .md files name is the keyword used to fetch its contents when using the scripts.

Explanation by example:

If you run `python .scripts/update.py example-42` then it will try to mirror the files described in manifests/example-42.md

Some example contents for copying meep.txt into the root directory and meep.py into the practicals folder would be as follows:
```
meep.txt
practicals/meep.py
```

Don't stray to far, you'll probably break things...