import os

def get_package_data():
    paths_test = [os.path.join('data', '*.json')]

    return {'astroquery.mast.tests': paths_test}
