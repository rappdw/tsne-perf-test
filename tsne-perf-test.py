#!/usr/bin/env python3
import argparse
from shutil import copyfile
import subprocess
import shlex


def run_test(tsne_dir, outfile):
    if not subprocess.call(shlex.split('cd {}; make clean all'.format(tsne_dir)), shell=True):
        tsne_command = '/usr/bin/time -f "%e %M %P" -o {} {}/bh_tsne'.format(outfile, tsne_dir)
        subprocess.call(shlex.split(tsne_command), shell=False)


def print_file(file, test_name):
    with open(file, 'r') as fin:
        print('{}: {}'.format(test_name, fin.read()))


parser = argparse.ArgumentParser()
parser.add_argument("dataset", choices=['full.mnist', '2500.mnist', 'iris'], help="dataset to use",
                    default='full.mnist')
args = parser.parse_args()

data_file = "/sandbox/data.{}.dat".format(args.dataset)

copyfile(data_file, 'data.dat')

out_rappdw = '/sandbox/time.rappdw.out'
out_10x = '/sandbox/time.10XDev.out'
out_lvdmaaten = '/sandbox/time.lvdmaaten.out'

run_test('/sandbox/tsne.rappdw/tsne/bh_sne_src', out_rappdw)
run_test('/sandbox/tsne.10XDev/tsne/bh_sne_src', out_10x)
run_test('/sandbox/tsne.lvdmaaten', out_lvdmaaten)

print('==========================================================')
print('\n\n')
print_file(out_rappdw, 'rappdw')
print_file(out_10x, '10XDev')
print_file(out_lvdmaaten, 'lvdmaaten')

