# Databricks notebook source
1+3

# COMMAND ----------

hello databricks

# COMMAND ----------

# MAGIC %sh
# MAGIC git rev-parse HEAD

# COMMAND ----------

api_url = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiUrl().get()
host_token = dbutils.notebook.entry_point.getDbutils().notebook().getContext().apiToken().get()
