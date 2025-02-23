# DIY Binding Paginator

I have a PDF with a bunch of pages that I want to print and bind myself.

One of the parts that I'm not looking forward to is figuring out how to efficiently lay out the individual pages into folios and signatures. I'm sure there are programs out there I could lean on to do this for me... but I thought it might be fun and fulfilling to try to write something myself.

## Next steps

- [x] Make binding script accept inputFile and outputFile command line arguments
- [ ] Make split even odd script accept inputFile command line argument
- [ ] Add scaling option to binding script
- [ ] Add gutter option to binding script
- [ ] Add sewing dots option, with positioning, to binding script

## Setup

```sh
# Set up an activate a virtual environment
python3 -m venv venv
source venv/bin/activate
# Install dependencies
python3 -m pip install -r requirements.txt
```

## Usage

```sh
python3 pdf_diy_binding_paginator.py
```

With this tool in its very half-done state, the sequence of commands I'm currently testing is:

```sh
python3 pdf_diy_binding_paginator.py
python3 pdf_split_even_odd.py 
```

## Testing

Tests are located in the `tests` folder. To run these tests, run:

```sh
python3 -m unittest discover -s tests
```

> [!NOTE]
> I'm new to python, so there's probably a better way to organize and run tests... but this works for me, for now!

## Notes

### 2024-12-05 at 15:30 - thinking about what tools to use

- <https://github.com/py-pdf/pypdf>, specifically <https://pypdf.readthedocs.io/en/stable/modules/PageObject.html#pypdf._page.PageObject.merge_translated_page> seems like one way to merge two pages together.
- The above "translation only" approach would work on the assumption that the source pages to merge would each be the same size, and that size would be small enough to fit on the destination medium while allowing for print margins. I think a good default is that each page must be small enough to fit on 8.5 by 11 minus 0.25 inches all around, so each page must be max 4 inches by 5.25 inches.

Things I wanna figure out:

- [x] Can I grab the first 2 pages of a big PDF so I can have a more manageable example?
- [x] Can I parse the size of each page?
- [x] Can I write a function that takes in a PDF file path, confirms whether pages are all the same size, and returns the consistent page size, or throws an error if page size isn't consistent?
- [x] Can I write the above function as a python "module" or whatever and import it into another file?
- [x] Can I write a function to compare one page size to see if it'll fit as a diptych in a user-provided final page size?
- [x] Can I join 2 pages into a single PDF?
  - Possible approach... first [create_blank_page](https://pypdf.readthedocs.io/en/stable/modules/PageObject.html#pypdf._page.PageObject.create_blank_page) with the user's provided size, this is our base page. Then use [merge page](https://pypdf.readthedocs.io/en/stable/modules/PageObject.html#pypdf._page.PageObject.merge_page), specifically [merge_translated_page](https://pypdf.readthedocs.io/en/stable/modules/PageObject.html#pypdf._page.PageObject.merge_translated_page), to position the first of the diptych pages onto the new blank page, this is the new base page. Then use [merge_translated_page](https://pypdf.readthedocs.io/en/stable/modules/PageObject.html#pypdf._page.PageObject.merge_translated_page) again to stack the second of the diptych pages into the merged document.
- [x] Implement `get_signature_guide.py`
- [x] Implement `offset_page_numbers.py` (takes in guide, offsets pages, like `offstPageNumbers(guide, offset)`)
- [x] Implement `get_signatures.py` (like `getSignatures(pageCount)`)
- [ ] Can I expand the above tooling to work on a 16-page PDF, joining pages to allow double-sided printing of all the folios needed for two 8-page signatures, each consisting of 4 double-sided folios?
  - Pseudo-code started in `pdf_diy_binding_paginator.py`
- [ ] Bonus for later... can I merge 8 different arbitrary file types (jpeg, png, pdf, etc) of arbitrary sizes into a single letter page in the classic 8-panel-page zine style? Could imagine using a source file that's a scanned letter page with the panels in "human readable" order... then slice it up with crop functions, and remix it into the printable zine mode. This could maybe tie in nicely with the whole "datamarks" thing... maybe there'd be a way to have an app on your phone that could use the camera to "scan" a page you just scribbled on, run that slice-and-dice transformation, and have a zine PDF ready to print?
