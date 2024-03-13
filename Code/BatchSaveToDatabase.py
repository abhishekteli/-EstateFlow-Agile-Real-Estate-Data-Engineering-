import os
from Transform import Gold
import time
from pyspark.sql.functions import udf, current_date
from pyspark.sql.types import StringType
from datetime import date
from dotenv import load_dotenv

load_dotenv()


class SaveToDatabase:

    def saveDatatoDatabase(self, realEstateDF):
        url = "jdbc:postgresql://localhost:5432/realestate"
        properties = {
            "user": os.getenv('USERNAME'),
            "password": os.getenv('DATABASE_PASSWORD'),
            "driver": "org.postgresql.Driver"
        }
        realEstateDF = realEstateDF.drop('imgSrc', 'detailUrl')
        load_date_to_compare = realEstateDF.select('loadDate').first()[0]
        mode = 'overwrite' if load_date_to_compare == date.today() else 'append'
        try:
            realEstateDF.write \
                .jdbc(url=url, table='houses', mode=mode, properties=properties)
        except Exception as e:
            print(f"error occurred: {e}")

        time.sleep(20)


if __name__ == "__main__":
    saveDB = SaveToDatabase()
    gd = Gold()

    realestateDF = gd.processData()
    saveDB.saveDatatoDatabase(realestateDF)