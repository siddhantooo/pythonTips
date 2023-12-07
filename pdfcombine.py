# -*- coding: utf-8 -*-
"""
Created on Fri Aug 18 13:54:54 2023

@author: Siddhant
"""

from pdfrw import PdfReader, PdfWriter
from pdfcutter import cutter

def combine(input_path1,input_path2,output_path):
    
    pages1 = PdfReader(input_path1).pages
    pages2 = PdfReader(input_path2).pages
    output = PdfWriter(output_path)
    
    for page in pages1:
        output.addpage(page)
    for page in pages2:
        output.addpage(page)
    output.write()
    return

if __name__ == '__main__':
    input_path1 = r"C:\Users\siddh\Dropbox\northwestern\jm2324\Misc\SiddhantAgarwal_JMP.pdf"
    input_path2 = r"C:\Users\siddh\Dropbox\northwestern\jm2324\Misc\SiddhantAgarwal_RedistributingTeachersUsingLocalTransfers.pdf"
    output_path = r"C:\Users\siddh\Dropbox\northwestern\jm2324\Misc\ResearchSamples.pdf"
    
    combine(input_path1,input_path2,output_path)