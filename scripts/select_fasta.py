#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Auteur : Mégane Boujeant
    But : Write a program (pymetacline/scripts/select_fasta.py) that reads the
    fasta file located in the data/fasta folder of pymetacline package and
    select a user-defined set of sequences identifiers (argument -seq that
    accept a comma separated list of sequence identifiers or a a set of
    identifiers using a positional argument).
"""

import argparse

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputfile', type=str)
    parser.add_argument('-seq', '--sequence', type=str)
    return parser

def main():
    parser = create_parser()
    args = parser.parse_args()
    args = args.__dict__
    print(args['inputfile'])
    seq_select = ""
    with open(args['inputfile']) as multi_sequence_ensembl:
        for line in multi_sequence_ensembl:
            if line.startswith('>'+args['sequence']):
                seq_select += line
                if not line.startswith('>'):
                    seq_select += line


if __name__ == "__main__":
    main()