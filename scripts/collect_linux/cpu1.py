#!/usr/bin/env Python


from __future__ import print_function
from collections import OrderedDict
import pprint


def CPUinfo():
    """ Return the information in /proc/CPUinfo
    as a dictionary in the following format:
    CUP_info['proc0']={...}
    CPU_indo['proc1']={...}
     """
    CPUinfo = OrderedDict()
    procinfo = OrderedDict()

    nprocs = 0
    with open('cpuinfo.txt') as f:
        for line in f:
            if not line.strip():
                # end of one processor
                CPUinfo['proc%s' % nprocs] = procinfo
                print(CPUinfo)
                nprocs += 1
                # Reset
                procinfo =  OrderedDict()
            else:
                if len(line.split(':')) == 2:
                    print(line)
                    procinfo[line.split(':')[0].strip()] = line.split(':')[1].strip()
                else:
                    procinfo[line.split(':')[0].strip()] = ''
    return CPUinfo


if __name__ == '__main__':
    CPUinfo = CPUinfo()
    for processor in CPUinfo.keys():
        print(CPUinfo[processor]['model name'])










