import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import *

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

datasource0 = glueContext.create_dynamic_frame.from_catalog(
    database="data", # Встав сюди назву своєї бази даних
    table_name="data_bucket_0f3324", # Встав сюди назву своєї таблиці в базі
    transformation_ctx="datasource0"
)


df = datasource0.toDF()

columns_to_drop = ['genmodel', 'genmodel_id', 'adv_id', 'adv_year', 'adv_month']
df = df.drop(*columns_to_drop)

df = df.withColumn('engin_size', regexp_replace(col('engin_size'), 'L', '').cast('float'))

df = df.withColumn('runned_miles', col('runned_miles.long'))

df = df.withColumn('price', col('price.long'))

df = df.replace('', None)
df = df.dropna(how='any')

# Заміни data-bucket-0f3324 на назву свого бакета

df.write.format('csv').option('header', 'true').save('s3://data-bucket-0f3324/transformed-data')

job.commit()