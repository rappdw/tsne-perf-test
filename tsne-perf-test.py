#!/usr/bin/env python3
import argparse
from shutil import copyfile
import subprocess
import shlex


def run_test(tsne_dir, outfile):
    if not subprocess.call(shlex.split('cd {}; make clean all'.format(tsne_dir)), shell=True):
        tsne_command = '/usr/bin/time -f "%e %M %P" -o {} {}/bh_tsne'.format(outfile, tsne_dir)
        print("running command: {}".format(tsne_command))
        subprocess.call(shlex.split(tsne_command), shell=False)


def print_file(file, test_name):
    with open(file, 'r') as fin:
        print('{}: {}'.format(test_name, fin.read()))

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", choices=['full.mnist', '2500.mnist', 'iris'], help="dataset to use",
                        default='full.mnist')
    args = parser.parse_args()

    data_file = "/sandbox/data.{}.dat".format(args.dataset)

    copyfile(data_file, 'data.dat')

    comparisons = [
        ('rappdw', '/sandbox/tsne.rappdw/', '/sandbox/time.rappdw.out'),
        ('rappdw.noopenmp', '/sandbox/tsne.rappdw.noopenmp/', '/sandbox/time.rappdw.noopenmp.out'),
        ('danielfrg', '/sandbox/tsne.danielfrg/', '/sandbox/time.danielfrg.out'),
        ('10XDev', '/sandbox/tsne.10XDev/', '/sandbox/time.10XDev.out'),
        ('lvdmaaten', '/sandbox/tsne.lvdmaaten', '/sandbox/time.lvdmaaten.out'),
    ]

    for comparison in comparisons:
        run_test(comparison[1], comparison[2])

    print('==========================================================')
    print('\n\n')
    for comparison in comparisons:
        print_file(comparison[2], comparison[0])

