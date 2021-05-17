# Databricks notebook source
# MAGIC %md ## DCM Setup
# MAGIC Need to install gdcm from conda. gdcm provides near universal conversion of pixel data from Dicom images

# COMMAND ----------

# MAGIC %fs ls dbfs:/databricks/scripts/

# COMMAND ----------

dbutils.fs.put("dbfs:/databricks/scripts/gdcm-install.sh", 
"""#!/bin/bash
set -ex
/databricks/python/bin/python -V
. /databricks/conda/etc/profile.d/conda.sh
conda activate /databricks/python
conda install -c conda-forge gdcm -y
""", 
overwrite = True)
dbutils.fs.ls("dbfs:/databricks/scripts/gdcm-install.sh")

# COMMAND ----------

dbutils.fs.head("dbfs:/databricks/scripts/gdcm-install.sh")

# COMMAND ----------

# MAGIC %sh cat /dbfs/databricks/scripts/gdcm-install.sh

# COMMAND ----------

