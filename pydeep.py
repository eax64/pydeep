#!/usr/bin/env python3

import logging
import argparse

list_tree = []
args = None

def print_dic(d, indent, path):
    for k in d:
        if not isinstance(k, str):
            logging.info(" "*2*indent + repr(k) + " (ignored)")
            continue
        if not args.full and k.startswith("_"):
            continue
        list_tree.append(id(k))
        if list_tree.count(id(k)) > 2:
            logging.info(" "*2*indent + k + " (skip rec)")
            continue
        
        if k in args.warning:
            logging.warning("WARNING: %s (%s)" % (k, ".".join(path + [k])))
            continue
        
        if isinstance(d[k], dict):
            logging.info(" "*2*indent + k)
            print_dic(d[k], indent+1, path + [k])
        elif callable(d[k]):
            logging.info(" "*2*indent + k)
        elif hasattr(d[k], "__dict__"):
            logging.info(" "*2*indent + k)
            print_dic(d[k].__dict__, indent+1, path + [k])
        else:
            s = str(k)
            if len(s) > 30:
                s = s[:30] + "..."
            logging.info(" "*2*indent + s)
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--warning',  action='store', default='sys,os', help='list of module that must emit a warning (comma separated)')
    parser.add_argument('-v', '--verbose', action="store_true", help='print all the tree')
    parser.add_argument('-f', '--full', action="store_true", help='Search inside private attribute')
    parser.add_argument('modname', help='The module where you want to search for os/sys')
    args = parser.parse_args()


    args.warning = args.warning.split(",")
    logging.basicConfig(format='%(message)s', level=[logging.WARNING, logging.INFO][args.verbose])
    mod = __import__(args.modname)
    
    print_dic(mod.__dict__, 0, [args.modname])
