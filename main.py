import geopandas
import arcgis
import os
import csv
import zipfile
from zipfile import ZipFile
from dotenv import load_dotenv
from assets.process_logging import ProcessLogging

process_logging = ProcessLogging(
    process_name = "data_upload",
    log_folder_path = "logs"
)

process_logging.logger.info("Loading environment variables")
load_dotenv('local.env')
AGOL_USERNAME = os.getenv("AGOL_USERNAME")
AGOL_PASSWORD = os.getenv("AGOL_PASSWORD")
process_logging.logger.info("Environment variables loaded")

process_logging.logger.info(f"Logging into {AGOL_USERNAME}'s AGOL... this may take a minute")
gis = arcgis.gis.GIS(
    url = "https://www.arcgis.com",
    username = AGOL_USERNAME,
    password = AGOL_PASSWORD
)
process_logging.logger.info(f"{gis} is your login result portal")

#import data


#run imported data quality checks

#create alias dictionary



#run upload