import subprocess
import sys
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
install("fuzzywuzzy")

from fuzzywuzzy import fuzz
from pyspark import SparkContext
from pyspark.sql import SparkSession, Row
from pyspark.sql import functions as f
import os
from pyspark.sql.types import (StructType, StructField,
                               StringType, ArrayType, IntegerType, DateType, BooleanType)


sc = SparkContext("local[*]", "test").getOrCreate()
sc.setLogLevel("ERROR")
spark = SparkSession.builder.master("local[*]").getOrCreate()


# Constants
REF_PATH = ""
HOM_PATH = ""
BASE_SOURCE = ""


# TABLE PARAMETERS
COLUMNS = []
REF_COLUMN = ""
DESCR_COLUMN = ""
WEIGHT_COLUMN = ""
dfs = {}

# Util functions

select_weight = f.udf(lambda cols: fuzz.ratio(*cols), IntegerType())

def select_homol(df, val):
    
    def select_est_df(row, val):

        if row[0] is not None or int(row[1]) <= val:
            val += 1
            salida = (val, row[3])
        else:
            salida = (row[1], row[3])
        return salida

    select_est_udf = f.udf(lambda row: select_est_df(
        row, val=val), ArrayType(StringType()))

    return df.withColumn("temp_col", select_est_udf(
        f.array(REF_COLUMN, "{}_{}".format(REF_COLUMN, source),
                DESCR_COLUMN, "{}_{}".format(DESCR_COLUMN, source)))).cache()\
        .withColumn(REF_COLUMN, f.col("temp_col").getItem(0))\
        .withColumn(DESCR_COLUMN, f.col("temp_col").getItem(1))\
        .drop("temp_col")


for source, df in dfs.items():


    # Define weights
    mdm = base.join(df, on=base[REF_COLUMN] == df["{}_{}".format(REF_COLUMN, source)], how="full")\
        .withColumn(WEIGHT_COLUMN, select_weight(f.array(DESCR_COLUMN, "{}_{}".format(DESCR_COLUMN, source))))\
        .filter(f.col("{}_{}".format(REF_COLUMN, source)).isNotNull())

    main = mdm.filter(f.col(WEIGHT_COLUMN) >= 50)
    new = mdm.filter(f.col(WEIGHT_COLUMN) < 50)

    # Chack data type
    acc = max([int(str(val[REF_COLUMN]).strip())
               for val in base.select(REF_COLUMN).collect()])

    newAdd = select_homol(new, acc)

    # Union
    homol = main.union(newAdd)

    print(source)
    homol.show(100)

    base = base.union(newAdd.select(REF_COLUMN, DESCR_COLUMN))
    base.show(100)
