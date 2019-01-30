from __future__ import print_function
import warnings
warnings.filterwarnings('ignore','.*conversion.*')

import os
import zipfile
import shutil
import requests
import numpy as np
from PIL import Image
import argparse
from .gdrive_downloader import gdrive_downloader
from .cuhk03_to_image import cuhk03_to_image

dataset = {
    'CUHK03': '1BO4G9gbOTJgtYIB0VNyHQpZb8Lcn-05m',
    'Market1501': '0B2FnquNgAXonU3RTcE1jQlZ3X0E',
    'Market1501Attribute' : '1YMgni5oz-RPkyKHzOKnYRR2H3IRKdsHO',
    'DukeMTMC': '1qtFGJQ6eFu66Tt7WG85KBxtACSE8RBZ0',
    'DukeMTMCAttribute' : '1eilPJFnk_EHECKj2glU_ZLLO7eR3JIiO'
}


def personreid_dataset_downloader(save_dir, dataset_name):
    
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        
    save_dir_exist = os.path.join(save_dir , dataset_name)

    if not os.path.exists(save_dir_exist):
        temp_dir = os.path.join(save_dir , 'temp')

        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        destination = os.path.join(temp_dir , dataset_name)

        id = dataset[dataset_name]

        print("Downloading %s" % dataset_name)
        gdrive_downloader(destination, id)

        zip_ref = zipfile.ZipFile(destination)
        print("Extracting %s" % dataset_name)
        zip_ref.extractall(save_dir)
        zip_ref.close()
        shutil.rmtree(temp_dir)
        print("Done")
        if dataset_name == 'CUHK03':
            print('Converting cuhk03.mat into images')
            cuhk03_to_image(os.path.join(save_dir,'CUHK03'))
            print('Done')
    else:
        print("Dataset Check Success: %s exists!" %dataset_name)