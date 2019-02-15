# A Simple Tool for Downloading Popular Person ReID Datasets (CUHK03, Market1501, DuketMTMC)
## [Demo](https://github.com/LinShanify/PersonReID_Dataset_Downloader/blob/master/demo.ipynb)

### Currently 3 reid datasets and 2 attributes datasets are available
* CUHK03
* Market1501
* DuketMTMC
* MSMT17
* Market1501Attribute
* DukeMTMCAttribute

Download from my google drive and can be modified to your personal google drive files.

Make life much easier when deploying the training on the server.
____
### PersonReID_Dataset_Downloader Function: 2 inputs
1. save_dir: Saving Directory for the dataset (string)
2. dataset_name: Dataset name listed above (string)

``` python
from PersonReID_Dataset_Downloader import PersonReID_Dataset_Downloader
# Download CUHK03 Dataset into the datasets folder
PersonReID_Dataset_Downloader('./datasets','CUHK03')

# Download Market1501 Dataset into the datasets folder
PersonReID_Dataset_Downloader('./datasets','Market1501')

# Download DukeMTMC Dataset into the datasets folder
PersonReID_Dataset_Downloader('./datasets','DukeMTMC')

# Download MSMT17 Dataset into the datasets folder
PersonReID_Dataset_Downloader('./datasets','MSMT17')

# Download Market1501 Attribute Dataset into the datasets folder
PersonReID_Dataset_Downloader('./datasets','Market1501Attribute')

# Download DukeMTMC Attribute Dataset into the datasets folder
PersonReID_Dataset_Downloader('./datasets','DukeMTMCAttribute')
```
____
### `PersonReID_Dataset_Downloader` function can also be called from Command Line
``` Bash
python PersonReID_Dataset_Downloader.py ./datasets DukeMTMCAttribute
```
___
## You can add, delete or replace the dataset by editing the  `dataset` dictionary in the `PersonReID_Dataset_Downloader.py`

Dataset_name: Google_Drives_File_ID

``` python
dataset = {
    'CUHK03': '1BO4G9gbOTJgtYIB0VNyHQpZb8Lcn-05m',
    'Market1501': '0B2FnquNgAXonU3RTcE1jQlZ3X0E',
    'Market1501Attribute' : '1YMgni5oz-RPkyKHzOKnYRR2H3IRKdsHO',
    'DukeMTMC': '1qtFGJQ6eFu66Tt7WG85KBxtACSE8RBZ0',
    'DukeMTMCAttribute' : '1eilPJFnk_EHECKj2glU_ZLLO7eR3JIiO',
    'MSMT17':'18EFJN4gfgv18ayL01S7EUm-kSvQvyNmE',
}
```