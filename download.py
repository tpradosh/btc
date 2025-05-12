"""

Downloads the data from Kaggle to 
update the dataset / csv file

"""

import kaggle

kaggle.api.authenticate()

# Download latest version
path = "mczielinski/bitcoin-historical-data"

kaggle.api.dataset_download_files(path, path='./data', unzip = True)



