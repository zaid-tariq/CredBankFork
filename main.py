import logging
from module.CredBankFork import CredBankFork
from module.AppLogger import AppLogger

AppLogger()
logging.info("***** Starting App ******")
dataSetObj = CredBankFork()
dataSetObj.parser()
#dataSetObj.loadDataSet()
#dataSetObj.populateTweetData()
print("*****************************************************")
print("It's Done!")
