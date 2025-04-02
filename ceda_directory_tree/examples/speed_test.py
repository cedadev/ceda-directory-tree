# encoding: utf-8
"""
Speed test using the archive spot directory to provide an example
"""
__author__ = 'Richard Smith'
__date__ = '18 Mar 2021'
__copyright__ = 'Copyright 2018 United Kingdom Research and Innovation'
__license__ = 'BSD - see LICENSE file in top-level package directory'
__contact__ = 'richard.d.smith@stfc.ac.uk'


from directory_tree import DatasetNode
import requests
import timeit
import os
from typing import Optional
from datetime import datetime


class SpotMapping:
    """
    Class to hold the data from the spot mapping directory

    Attributes:
        url (str): The URL for the CEDA fileset mapping

    Parameters:
        path_list (List): List of paths from the fileset mapping
        path2spotmap (Dict): Mapping between paths and storage spots
    """
    url = 'https://cedaarchiveapp.ceda.ac.uk/cedaarchiveapp/fileset/download_conf/'

    def __init__(self):

        self.path_list = []
        self.path2spotmap = {}

        self._download_mapping()

    def _download_mapping(self):
        """
        Download the spot directory and build the map
        """

        response = requests.get(self.url)
        spot_mapping = response.text.split('\n')

        self._build_mapping(spot_mapping)

    def _build_mapping(self, spot_mapping: list, sep: str = None):
        """
        Convert the downloaded text into the parameters used within the class

        :param spot_mapping: The downloaded content from the spot mapping endpoint
        :param sep: The separator used in the spot mapping
        """
        for line in spot_mapping:
            if not line.strip(): continue
            spot, path = line.strip().split(sep)

            self.path2spotmap['path'] = spot
            self.path_list.append(path)

    def match_path(self, path: str) -> Optional[str]:
        """
        Recursively knock parts of the path off until a match
        is found

        :param path:
        :return:
        """

        # Check for match
        if path in self.path_list:
            return path

        # Go one level up the tree
        path = os.path.dirname(path)

        # Recursively loop
        while len(path) > 1:
            if path in self.path_list:
                return path

            path = os.path.dirname(path)


def main():
    #######################
    #        Setup        #
    #######################

    spot_mapping = SpotMapping()

    TEST_PATH = '/badc/cmip5/data/cmip5/output1/MIROC/MIROC-ESM/historical/6hr/atmos/6hrLev/r1i1p1/files/ps_20111129/ps_6hrLev_MIROC-ESM_historical_r1i1p1_1950010106-1990010100.nc'

    NUMBER_OF_ITERATIONS = 1000
    #######################
    # DatasetNode Example #
    #######################

    start = datetime.now()
    directory_tree = DatasetNode()

    # Build the tree
    for path in spot_mapping.path_list:
        directory_tree.add_child(path)

    end = datetime.now()

    print('Directory Tree')
    print('=' * 20)
    print(f'* Time to build tree for {len(spot_mapping.path_list)} paths: {end - start}')

    # Test matching
    results = timeit.timeit(lambda: directory_tree.search_name(TEST_PATH), number=NUMBER_OF_ITERATIONS)
    print(f'* Mean time per iteration for {NUMBER_OF_ITERATIONS} iterations:\n\t{results}s/it')

    ###########################
    # Recursive Match Example #
    ###########################
    print()
    print('Recursive Lookup')
    print('=' * 20)
    results = timeit.timeit(lambda: spot_mapping.match_path(TEST_PATH), number=NUMBER_OF_ITERATIONS)
    print(f'* Mean time per iteration for {NUMBER_OF_ITERATIONS} iterations:\n\t{results}s/it')


if __name__ == '__main__':
    main()