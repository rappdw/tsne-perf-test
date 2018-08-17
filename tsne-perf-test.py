#!/usr/bin/env python3
import argparse
import datetime
import os
import subprocess
import shlex


def run_test(venv, tsne_dir, outfile, python_test_output):
    if tsne_dir:
        print("Starting test {}: {}".format(venv, datetime.datetime.now()))
        if not subprocess.call(shlex.split('cd {}; make clean all'.format(tsne_dir)), shell=True):
            tsne_command = '/usr/bin/time -f "%e %M %P" -o {} {}/bh_tsne'.format(outfile, tsne_dir)
            print("running command: {}".format(tsne_command))
            subprocess.call(shlex.split(tsne_command), shell=False)
        print("Finished with test {}: {}".format(venv, datetime.datetime.now()))
    if python_test_output:
        print("Starting test py-{}: {}".format(venv, datetime.datetime.now()))
        python_command  = 'source activate {}; cd /sandbox; /usr/bin/time -f "%e %M %P" -o {} ./python-tsne-perf-test.py /sandbox/data.dat'.format(venv, python_test_output)
        print("running command: {}".format(python_command))
        subprocess.run(python_command, shell=True, executable='/bin/bash')
        print("Finished with test py-{}: {}".format(venv, datetime.datetime.now()))


def print_file(file, test_name):
    with open(file, 'r') as fin:
        print('{}: {}'.format(test_name, fin.read()))

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("dataset", choices=['cifar', 'full.mnist', '2500.mnist', 'iris'], help="dataset to use",
                        default='full.mnist')
    args = parser.parse_args()

    data_file = "/sandbox/data.{}.dat".format(args.dataset)

    os.rename(data_file, '/sandbox/data.dat')

    comparisons = [
        # the 'py3x' environments are for inclusion of specific wheels that are not part of the
        # standard comparison set. Uncomment the following line to include them in the test
        # ('resero-labs', None, None, '/sandbox/py.time.resero-labs.out'),
        # ('py36', None, None, '/sandbox/py.time.resero-labs.out'),
        ('resero-labs', '/sandbox/tsne.resero-labs/', '/sandbox/time.resero-labs.out', '/sandbox/py.time.resero-labs.out'),
        ('10XDev', '/sandbox/tsne.10XDev/', '/sandbox/time.10XDev.out', '/sandbox/py.time.10XDev.out'),
        ('pypi', '/sandbox/tsne.danielfrg/', '/sandbox/time.danielfrg.out', '/sandbox/py.time.danielfrg.out'),
        # ('resero-labs.noopenmp', '/sandbox/tsne.resero-labs.noopenmp/', '/sandbox/time.resero-labs.noopenmp.out', None),
        ('lvdmaaten', '/sandbox/tsne.lvdmaaten', '/sandbox/time.lvdmaaten.out', None),
    ]

    for comparison in comparisons:
        run_test(comparison[0], comparison[1], comparison[2], comparison[3])
        print('==========================================================')

    os.rename('/sandbox/data.dat', data_file)

    print('\n\n')
    for comparison in comparisons:
        if comparison[2]:
            print_file(comparison[2], comparison[0])
        if comparison[3]:
            print_file(comparison[3], "python-{}".format(comparison[0]))
