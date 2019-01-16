import pandas as pd
from pyspark.sql import SparkSession as ss
from pyspark.sql.types import IntegerType

#read csv file with pandas
reviews1 = pd.read_csv("1.csv")
reviews2 = pd.read_csv("2.csv")
#print(reviews1.shape[0]) #number of rows
#print(reviews1.shape[1]) #number of cols
#두 파일의 길이가 다르다면 두 개의 shape[0] 값 중에서 작은 값을 기준으로 14번째 줄에서 for문을 돌리게 할 수 있음.

#store read data into list
myList = []
for i in range(10):
    myList.append(int(reviews1["number"][i]+reviews2["number"][i]))
#print(myList)

#convert list to spark
spark = ss.builder.getOrCreate()
result = spark.createDataFrame(myList, IntegerType())

#store data in a mongoDB
#result.write.format("com.mongodb.spark.sql.DefaultSource").option("spark.mongodb.output.uri","mongodb://localhost:27017/test.csv").save()