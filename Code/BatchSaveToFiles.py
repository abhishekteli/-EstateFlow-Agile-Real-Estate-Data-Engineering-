from Transform import Gold
from datetime import date
import time


class SaveToFiles:

    def __init__(self):
        self.basedir_files = (f"/Users/abhishekteli/Documents/Projects/RealEstate/processedData/"
                              f"year={date.today().year}/month={date.today().month}/day={date.today().day}/")

    def saveDataToFiles(self, realEstateDF):
        print(f"\nWriting Data on the Files...", end='')
        (realEstateDF
         .write
         .option('header', 'true')
         .format("csv")
         .mode("overwrite")
         .partitionBy('propertyType')
         .save(f"{self.basedir_files}/")
         )
        print('done')
        time.sleep(20)


if __name__ == "__main__":
    gd = Gold()
    savefile = SaveToFiles()
    realestateDF = gd.processData()
    savefile.saveDataToFiles(realestateDF)
