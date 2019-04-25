#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 09:36:55 2019

@author: yaoxinzhi
"""

import xml.etree.ElementTree as etree
import os
import argparse


def ex_summary(result_path, out):
    
    count = 0
    
    if not os.path.exists(out):
        os.mkdir(out)
    
    # brief summary
    wf = open('{0}/{1}_summary'.format(out, result_path.split('/')[-1].split('_')[0]), 'w')
    
    file_list = os.listdir(result_path)
    for file in file_list:
        tree = etree.parse('{0}/{1}'.format(result_path, file))
        root = tree.getroot()
        text = None
        for textblock in root.findall('brief_summary'):
            text = textblock.find('textblock').text
            text = text.replace('\n', '').replace('   ', '')
            if text:
                count += 1
                wf.write('{0}\n'.format(text))
    print ('Get {0} brief Summary'.format(count))
    
    # detailed description
    wf = open('{0}/{1}_description'.format(out, result_path.split('/')[-1].split('_')[0]), 'w')
    
    file_list = os.listdir(result_path)
    for file in file_list:
        tree = etree.parse('{0}/{1}'.format(result_path, file))
        root = tree.getroot()
        text = None
        for textblock in root.findall('detailed_description'):
            text = textblock.find('textblock').text
            text = text.replace('\n', '').replace('   ', '')
            if text:
                count += 1
                wf.write('{0}\n'.format(text))
    print ('Get {0} detailed desctiption'.format(count))
    
    wf.close()
    
if __name__ == '__main__':
    parse = argparse.ArgumentParser()
    parse.add_argument('-r', '--r-path', help='result path',
                        dest='rpath', required=True)                      
    parse.add_argument('-w', '--w-path', help='ouput file',
                        dest='wpath', required=True)
    args = parse.parse_args()
    
    ex_summary(args.rpath, args.wpath)
    