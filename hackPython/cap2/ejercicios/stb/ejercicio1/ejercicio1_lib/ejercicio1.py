# -*- coding: utf-8 -*-

import argparse
import logging

logging.basicConfig(format="[%(asctime)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
log = logging.getLogger(__name__)


# ----------------------------------------------------------------------
def main():

    from .api import run_console, GlobalParameters

    examples = '''
Examples:

    * Scan target using default 50 most common plugins:
        %(tool_name)s TARGET
    '''  % dict(tool_name="ejercicio1")

    parser = argparse.ArgumentParser(description='%s security tool' % "ejercicio1".capitalize(), epilog=examples,
                                     formatter_class=argparse.RawTextHelpFormatter)

    # Main options
    parser.add_argument("--target", '-T', dest='target', required=True, metavar="TARGET", nargs="*",
                        help="Target ip to analyze")
    parser.add_argument("-v", "--verbosity", dest="verbose", action="count", help="verbosity level: -v, -vv, -vvv.",
                        default=1)
    parser.add_argument('--port', '-P', dest='port', nargs='*', help='Tarjet port to analyze')
    parser.add_argument('--open', '-O', dest='open', action='store_true', help='Show just opened ports')


    parsed_args = parser.parse_args()

    # Configure global log
    log.setLevel(abs(5 - parsed_args.verbose) % 5)

    # Set Global Config
    config = GlobalParameters(parsed_args)

    try:
        run_console(config)
    except KeyboardInterrupt:
        log.warning("[*] CTRL+C caught. Exiting...")
    except Exception as e:
        log.critical("[!] Unhandled exception: %s" % str(e))

if __name__ == "__main__" and __package__ is None:
    # --------------------------------------------------------------------------
    #
    # INTERNAL USE: DO NOT MODIFY THIS SECTION!!!!!
    #
    # --------------------------------------------------------------------------
    import sys
    import os
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(1, parent_dir)
    import ejercicio1_lib
    __package__ = str("ejercicio1_lib")

    del sys, os

    main()
