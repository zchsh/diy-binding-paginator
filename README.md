# DIY Binding Paginator

I have a PDF with a bunch of pages that I want to print and bind myself.

One of the parts that I'm not looking forward to is figuring out how to efficient lay out the individual pages into folios and signatures. I'm sure there are programs out there I could lean on to do this for me... but I thought it might be fun and fulfilling to try to write something myself.

## Notes

### 2024-12-05 at 15:30 - thinking about what tools to use

- <https://github.com/py-pdf/pypdf>, specifically <https://pypdf.readthedocs.io/en/stable/modules/PageObject.html#pypdf._page.PageObject.merge_translated_page> seems like one way to merge two pages together.
- The above "translation only" approach would work on the assumption that the source pages to merge would each be the same size, and that size would be small enough to fit on the destination medium while allowing for print margins. I think a good default is that each page must be small enough to fit on 8.5 by 11 minus 0.25 inches all around, so each page must be max 4 inches by 5.25 inches.

Things I wanna figure out:

- [ ] Can I grab the first 2 pages of a big PDF so I can have a more manageable example?
- [ ] Can I parse the size of each page? And throw an error if pages are different sizes, or if their one consistent size is too small for the final page size?
- [ ] Can I join 2 pages into a single PDF?
- [ ] Can I add custom positions to those 2 pages as I join them?
- [ ] Can I expand the above tooling to work on a 16-page PDF, joining pages to allow double-sided printing of all the folios needed for two 8-page signatures, each consisting of 4 double-sided folios?
