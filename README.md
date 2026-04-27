# VTT to TXT
This repo contains a script `main.py` to convert `.vtt` files to `.txt` files. The spoken content only is retained, as one continuous paragraph with no line breaks. It's intented to allow comparison between files (using [Diffchecker](https://www.diffchecker.com/text-compare/) for example), or to get a word count of only spoken content (this is in the output filename).

To use the script:
1. Place your `.vtt` files in the folder `input`.
2. Make sure nothing important is in the `output` folder. Its contents will be deleted.
3. Run `main.py`.
4. Copy the parsed files from the `output` folder.
