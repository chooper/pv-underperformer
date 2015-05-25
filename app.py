#!/usr/bin/env python

import os
import csv
from collections import defaultdict
import statistics

HOST_SECTOR_COL = 'Host Customer Sector'
HOST_ZIP_COL    = 'Host Customer Physical Address Zip Code'
APP_ID_COL      = 'Application Number'
PROD_KWH_COL    = 'Period kWh Production'

def mean(list_):
    return statistics.mean(list_)


def stdev(list_):
    return statistics.pstdev(list_)


def import_csv(datafile):
    # Structure: {zip: {application_number: [measurements]}}
    installations = defaultdict(lambda: defaultdict(lambda: list()))

    with open(datafile, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            if row[HOST_SECTOR_COL] != 'Residential':
                continue

            # TODO filter dates

            zip_        = row[HOST_ZIP_COL]
            id_         = row[APP_ID_COL]
            measurement = int(row[PROD_KWH_COL])

            installations[zip_][id_] += [measurement]

    return installations


def mean_for_zip(installations):
    measurements = []
    for m_list in installations.values():
        for m in m_list:
            measurements.append(m)
    return mean(measurements)


def stdev_for_zip(installations):
    measurements = []
    for m_list in installations.values():
        for m in m_list:
            measurements.append(m)
    return stdev(measurements)


def main():
    datafile = os.environ.get('DATAFILE')
    installation_data = import_csv(datafile)

    # generate stats for zips
    zips = {}
    for zip_, installations in installation_data.items():
        zip_average = mean_for_zip(installations)
        zip_stdev  = stdev_for_zip(installations)
        zips[zip_] = (zip_average, zip_stdev)

    # identify under-performing installations
    underperformers = []
    for zip_, installations in installation_data.items():
        for install_id, measurements in installations.items():
            install_mean = mean(measurements)
            if install_mean < zips[zip_][0] - zips[zip_][1]:
                underperformers.append( (install_id, install_mean, zips[zip_][0], zips[zip_][1]) )

    # display the under-performing installation
    for underperformer in underperformers:
        install_id, install_mean, zip_mean, zip_stdev = underperformer[0], underperformer[1], underperformer[2], underperformer[3]
        print("Underperformer! id={0} output={1}kWh zip-mean={2}kWh zip-stdev={3}".format(install_id, install_mean, zip_mean, zip_stdev))


if __name__ == '__main__':
    main()

