#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser


parser = ArgumentParser(usage="Software for graph analysis")
parser.add_argument("-i", "--input_file(s)", nargs='*', dest="input", metavar="Input file(s)",
                    help="Supply input path(s) of input file(s)")
parser.add_argument("-p", "--pivot_mode", metavar="Pivot mode", choices=["max", "random"],
                    help="Choose pivot mode: Either 'max' or 'random'")
parser.add_argument("-a", "--anchor", metavar="Anchor graph", default=[],
                    help="Supply anchor graph file (path)!")
parser.add_argument("-o", "--output_file", metavar="Output file (path)", nargs='?', const=1,
                    help="Saves graph as .graph file. If a path (in quotation marks! is provided, graph will be saved "
                         "there. If a .graph file name is provided, it will be saved with that name in the current "
                         "working directory. Else it will be saved in the current working directory using its name "
                         "attribute.")
parser.add_argument("-mp", "--modular_product", action="store_true", help="Forms the modular product of two graphs.")
parser.add_argument("-bk", "--bron_kerbosch", action="store_true", help="Invokes maximal clique finding on input "
                                                                        "graph.")
parser.add_argument("-ga", "--graph_alignment", nargs="*", metavar="Type of matching algorithm",
                    help="Choose matching algorithm: Either 'bk' for bron-kerbosch or 'mb' for matching-based. If "
                         "bron-kerbosch was chosen, also provide the number of cliques on which the matching should be "
                         "expanded (e.g. 'bk 5').")
parser.add_argument("-rg", "--random_graph", nargs=3,
                         help="Create a random graph. Supply the number of vertices (N, integer), the mean relative "
                              "connectivity (p, float) and whether it should be directed (either 'True' or 'False') as "
                              "e.g. '10 0.8 True'.")
parser.add_argument("-rc", "--random_cluster", nargs=4, type=int,
                         help="Create a random clustered graph. Supply the number of vertices (N, integer), the desired "
                              "degree at each node (d, integer), how many vertices you want to delete form the cluster"
                              "(del_vert, integer) and finally how mandy edges you want to delete(del_edges, integer)"
                              "e.g. '20 3 2 2'.")
parser.add_argument("-gt", "--guide_tree", nargs='?', metavar="Comparison function", const="density",
                    help="Choose the comparison function/attribute for guide tree building: 'density' for graph "
                         "density")
parser.add_argument("syntax", nargs="?", help="Only a dummy attribute to help using correct syntax...")

def parse_command_line():
    args = parser.parse_args()
    return args

