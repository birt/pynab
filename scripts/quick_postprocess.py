import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

import pynab.tvrage
import pynab.imdb


def local_postprocess():
    pynab.tvrage.process(0, False)
    pynab.imdb.process(0, False)


if __name__ == '__main__':
    print('This script will attempt to post-process releases against local databases.')
    print('After importing or collecting a large batch of releases, you can run this once prior to start.py.')
    print('This will check all local matches first, leaving start.py to just do remote matching.')
    print('It\'ll really just save some time.')
    print()
    input('To continue, press enter. To exit, press ctrl-c.')
    local_postprocess()