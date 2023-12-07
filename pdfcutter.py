# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 19:13:14 2022

@author: Siddhant
"""

from pdfrw import PdfReader, PdfWriter

def cutter(input_path,output_path,extract):
    pages = PdfReader(input_path).pages
    output = PdfWriter(output_path)
    if type(extract) == int:
        output.addpage(pages[extract-1])
    elif type(extract) in [tuple, list]:
        for pagenum in extract:
            output.addpage(pages[pagenum-1])
    elif '-' in extract:
        start, end = list(map(int, extract.split('-')))
        for pagenum in range(start,end+1):
            output.addpage(pages[pagenum-1])
    elif ',' in extract:
        extract = list(map(int, extract.split(',')))
        for pagenum in extract:
            output.addpage(pages[pagenum-1])
    elif extract != '' and extract is not None:
        extract = int(extract)
        output.addpage(pages[extract-1])
    output.write()
    return

if __name__ == '__main__':
    input_path = 'C:\\Users\\siddh\\Downloads\\guddu_shaadi\\guddu_boards.pdf'
    
    for i in [3,4,5,7,8,10]:
        extract = str(i)
        output_path = 'C:\\Users\\siddh\\Downloads\\guddu_shaadi\\guddu_boards' + extract + '.pdf'
        cutter(input_path,output_path,extract)