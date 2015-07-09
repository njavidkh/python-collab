"""
    The main script file to launch the pysines application
"""
import sys
import argparse

def check_options(options):
    """
    Check that the options are sane and restricted to the project specs
    :param options: An `argparse.Namespace` object
    :return:
    """

def create_parser():
    """
    Create the Argument Parser for this script
    :return:  An `argparse.ArgumentParser` instance
    """
    parser = argparse.ArgumentParser('pysines', description="")
    
    return parser

def parse_args(args):
    """
    Perform the actual argument parsing, useful for testing the parser
    :param args: The list of arguments to parse, something like `sys.argv`
    :return: An `argparse.Namespace` object
    """
    parser = create_parser()
    return parser.parse_args(args)


import os
import numpy as np
from matplotlib import pyplot as plt

def run(options):
    """
    Run the actual script
    :param options: An `argparse.Namespace` object
    :return:
    """

    # Do some additional check on the options
    check_options(options)
    
    
    print "Figure(1)"
    Numberofsins = options.num
    Destfile = options.file
    
    for i in range(Numberofsins):
        time = np.linspace(0, 4 * np.pi)
        data = np.sin(time/i) 
        plt.plot(time, data)
        plt.title('sin. waves')
        plt.xlabel('Time')
        plt.ylabel('sin. waves')
    
    

    pass


if __name__ == '__main__':
    # Script has been launched

    options = parse_args(sys.argv)
    run(options)