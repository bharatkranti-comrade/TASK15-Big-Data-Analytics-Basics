from pyspark.sql import SparkSession

# Start the Spark Big Data tool
spark = SparkSession.builder.appName("Task15").getOrCreate()

# Create a sample list of server logs
logs_data = [
    ("INFO", "User logged in successfully"),
    ("ERROR", "Database connection failed"),
    ("WARN", "High memory usage"),
    ("ERROR", "Page not found 404")
]

# Convert the list into a clean table with columns
df = spark.createDataFrame(logs_data, ["Type", "Message"])

# Filter the table to keep ONLY the ERROR lines
errors = df.filter(df.Type == "ERROR")

# Show the final filtered table on the screen
errors.show()

# Stop the tool safely
spark.stop()
