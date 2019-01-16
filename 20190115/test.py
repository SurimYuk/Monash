from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("CSVExercise").getOrCreate()
df = spark.read.option("header","true").option("inferSchema","true").csv("age.csv")
df1 = spark.read.option("header","true").option("inferSchema","true").csv("personalNumber.csv")
df2=df.join(df1,'name')
df2.show()

df2.write.format("com.mongodb.spark.sql.DefaultSource").option("spark.mongodb.output.uri","mongodb://localhost:27017/join.csv").save()