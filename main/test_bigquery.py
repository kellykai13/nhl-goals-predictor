from google.cloud import bigquery
from google.oauth2 import service_account
from datawrangle import standings_df 
from credentials import KeyPath
# Replace with the path to your JSON key
KEY_PATH = KeyPath

# Authenticate and create a client
credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
client = bigquery.Client(credentials=credentials, project=credentials.project_id)

# # List datasets in your project
# datasets = client.list_datasets()

# # Print the names of all datasets
# for dataset in datasets:
#     print(dataset.dataset_id)

# print("BigQuery client created successfully.")



table_id = "nhl-project-457702.nhl_data.standings"  # Replace with your dataset and table
job_config = bigquery.LoadJobConfig(write_disposition="WRITE_TRUNCATE")

job = client.load_table_from_dataframe(standings_df, table_id, job_config=job_config)
job.result()

print(f"✅ Uploaded {job.output_rows} rows to {table_id}")

