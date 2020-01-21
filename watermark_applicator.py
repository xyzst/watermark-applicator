"""
Watermark Applicator

A small utility module which applies a watermark to all pages in a PDF

__author__ = "Darren Rambaud"
__email__ = "xyzst@users.noreply.github.com"
"""
import os
import sys

import PyPDF2


def apply_watermark(pdf):
    """
    Given a tuple of paths to pdf files, will apply the second pdf as a watermark to all pages in the first pdf

    :param pdf: A tuple of strings, first index points to the pdf to modify, the second index points to the watermark
    :return: None
    """
    pdf_to_modify = PyPDF2.PdfFileReader(open(pdf[0], 'rb'))
    watermark_to_apply = PyPDF2.PdfFileReader(open(pdf[1], 'rb'))
    output = PyPDF2.PdfFileWriter()

    for page in range(pdf_to_modify.getNumPages()):
        p = pdf_to_modify.getPage(page)
        p.mergePage(watermark_to_apply.getPage(0))
        output.addPage(p)

        with open(os.path.splitext(pdf[0])[0] + '_watermarked.pdf', 'wb') as w:
            output.write(w)

    print('[INFO] Successfully applied \'%s\' to all pages in \'%s\'' % (pdf[1], pdf[0]))


def validate_files(pdf, watermark):
    if not os.path.exists(pdf) or not os.path.exists(watermark):
        print('[ERR] The PDF at %s does not exist' % pdf)
        sys.exit(-1)

    return pdf, watermark


if __name__ == '__main__':
    apply_watermark(validate_files(sys.argv[1], sys.argv[2]))
