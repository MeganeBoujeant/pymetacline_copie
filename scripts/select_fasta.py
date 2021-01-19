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

from Bio import SeqIO


def create_parser():
    """ Function which create arguments for execute this program.
    This function collect and return arguments entered by the user.

    :return: arguments:
        -i: inputfile (fasta file) whose whe want to extract the sequence of
        particular(s) identifier(s)
        -seq: sequence identifier(s)
    """
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument('-i', '--inputfile',
                        help="Enter fasta file whose you want extract \
                             sequence(s).", type=str, required=True)
    parser.add_argument('-seq', '--sequence',
                        help="Enter one or more sequence identifier(s).\
                        If you enter more than one identifier, separate them \
                        whith a comma.",
                        type=str, required=True)
    return parser


def main():
    """ Function which search and return sequence(s) of sequence identifier(s)
    previously entered by the user.

    :return: dictionary of sequence identifier(s) and his (their) sequence(s)
    """
    parser = create_parser()
    args = parser.parse_args()
    args = args.__dict__
    print(args['inputfile'])
    seq_id = args['sequence'].split(',')
    with open(args['inputfile']) as multi_sequence_ensembl:
        for record in SeqIO.parse(multi_sequence_ensembl, "fasta"):
            if record.name in seq_id:
                print(record.name + "\n" + record.seq + "\n")


if __name__ == "__main__":
    main()
