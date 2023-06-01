# Main Airflow DAG

https://github.com/ris-tlp/audiophile-e2e-pipeline/blob/main/airflow/dags/main_dag.py

The provided link points to an Airflow Directed Acyclic Graph (DAG) file named `main_dag.py`. This file defines a pipeline of tasks that are executed in a particular order, with each task being a node in the graph and the edges representing dependencies between tasks.

Here's a breakdown of what each task in the DAG does:

1. **scrape_audiophile_data:** This task uses a Python script (`scraper.py`) to scrape data from a source (presumably Crinacle's website as mentioned in the repository description).

2. **upload_bronze_csv_s3:** This task uploads the scraped (bronze) data to an AWS S3 bucket using a Python script (`upload_to_s3.py`).

3. **validate_sanitize_bronze_data:** This task validates and sanitizes the bronze data using a Python script (`validate_sanitize_bronze.py`).

4. **upload_silver_csv_s3:** This task uploads the validated and sanitized (silver) data to an AWS S3 bucket using the same `upload_to_s3.py` script.

5. **redshift_load:** This task loads the silver data into an AWS Redshift database using a Python script (`upload_to_redshift.py`).

6. **rds_load:** This task loads the silver data into an AWS RDS database using a Python script (`upload_to_rds.py`).

7. **generate_dbt_profile:** This task generates a dbt profile using a Python script (`generate_dbt_profile.py`). dbt (data build tool) is a command-line tool that enables data analysts and engineers to transform data in their warehouses by writing SQL select statements.

8. **dbt_transform:** This task runs dbt transformations on the data in the warehouse. The transformations are defined in the `/opt/airflow/tasks/dbt_transform/` directory.

9. **dbt_test:** This task runs dbt tests on the transformed data. The tests are also defined in the `/opt/airflow/tasks/dbt_transform/` directory.

## Other python scripts

### upload_to_s3.py
https://github.com/ris-tlp/audiophile-e2e-pipeline/blob/main/airflow/tasks/upload_to_s3.py

* This script is designed to upload CSV files to an AWS S3 bucket.
* The script loads configuration values from a `.env` file located in the same directory as the script. These values are stored in a dictionary named `config`.
* Defines `connect_s3` function. This function creates a `boto3` resource object for interacting with AWS S3. If the script fails to create this object (for example, due to missing AWS credentials), it raises an exception.
* Defines `upload_csv_s3` function. This function uploads the two CSV files to the specified S3 bucket. It does this by calling the `connect_s3` function to get a `boto3` resource object, then calling the `upload_file` method of this object for each file.

## validate_sanitize_bronze.py
https://github.com/ris-tlp/audiophile-e2e-pipeline/blob/main/airflow/tasks/validate_sanitize_bronze.py
* This script is designed to validate and sanitize bronze data (raw scraped data) and convert it into silver data (cleaned and validated data).
* Defines helper functions:
   - `read_csv_as_dicts(filename: str) -> List[dict]`: This function reads a CSV file and returns a list of dictionaries, where each dictionary represents a row in the CSV file.
   - `sanitize_data(data: List[dict]) -> List[dict]`: This function performs rudimentary sanitizations on bronze data. It drops unnecessary columns, removes quotes around signatures, replaces discontinued devices with no price with -1, replaces device prices with question marks with -1, replaces device prices with models embedded in them with only the price, and replaces star text rating with a number. If no stars, it replaces with -1.

* Main execution block: If the script is run as a standalone program, it reads the bronze data from two CSV files (`headphones-bronze.csv` and `iems-bronze.csv`), sanitizes the data, validates the data using Pydantic models (`InEarMonitor` and `Headphone`), and then writes the sanitized and validated data back to CSV files (`iems-silver.csv` and `headphones-silver.csv`).

