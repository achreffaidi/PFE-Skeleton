### PFE Template 

This document contains the skeleton of my end-of-study dissertation written on Latex.
I had to remove most of the paragraphs to protect company private information. 

### Structure

In the root folder there's a file called `Report.tex`. It's used to reference all the other documents on the `\files` directory. 

`\figures` contains figures usedd in the project. 

`\scripts` contains a small script I wrote to extract abbreviations from the PDF file and generate a latex document out of them. you can use the extractor.py script to extract the abbreviation, then you can copy them to a json file and use Replace-All to update all `",` to `":"description",`. Then use the `generate.py` script to generate the Latex file.

### Generating PDF

I am using vs-code latex extensions with MikTex Console to generate pdf files. (Tested only on MacOS). If you're using Overleaf, you can copy section to your overleaf document. Just be careful about dependency and imports. Most of the imports are in the Report.tex file.

### Remarks I got

Structure and balance are Good. 

Describing all figures and tables is Good

Need to reference all tables and figures using words like "Following Figure" "Following Table" ... 

Need to add resume in French and English (Arabic wasn't required).