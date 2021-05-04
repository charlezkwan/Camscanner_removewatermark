#!/usr/bin/env python

'''
usage:   extract.py <some.pdf>

Locates Form XObjects and Image XObjects within the PDF,
and creates a new PDF containing these -- one per page.

Resulting file will be named extract.<some.pdf>

'''

import sys
import os

from pdfrw import PdfReader, PdfWriter
from pdfrw.findobjs import page_per_xobj


inpfn, = sys.argv[1:]
outfn = 'pdf_' + os.path.basename(inpfn)
pages = list(page_per_xobj(PdfReader(inpfn).pages, margin=0.5*72))
pages = pages[1::2]
if not pages:
    raise IndexError("No XObjects found")
writer = PdfWriter(outfn)


writer.addpages(pages)

writer.write()