#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The compute_tx_len.py program written for Python 3 computes the genomic size of
a transcript (exon + intron).
"""

import re


def get_tx_genomic_length(input_file=None):
    """ This function computes the genomic size of each transcript presents in a
     GTF file.

    :param input_file: GTF file as input
    :return: print: transcript id and its length
    """
    transcript_start = dict()
    transcript_end = dict()
    file_handler = open(input_file)
    for line in file_handler:
        token = line.split("\t")
        start = int(token[3])  # start of the current element
        end = int(token[4])  # end of the current element
        # identifier of the transcript

        tx_id = re.search('transcript_id "([^"]+)"', token[8]).group(1)

        if tx_id not in transcript_start:
            transcript_start[tx_id] = start
            transcript_end[tx_id] = end
        else:
            if start < transcript_start[tx_id]:
                transcript_start[tx_id] = start
                if end > transcript_end[tx_id]:
                    transcript_end[tx_id] = end

    for tx_id in transcript_start:
        print(tx_id + "\t" + str(transcript_end[tx_id] - transcript_start[tx_id]
                                 + 1))


if __name__ == '__main__':
    get_tx_genomic_length(input_file='../pymetacline/data/gtf/simple.gtf')
