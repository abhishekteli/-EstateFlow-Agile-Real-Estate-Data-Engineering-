# Real Estate Data Pipeline

## Phase 1: Real Estate Batch Processing

### Introduction
The primary objective of this project is to streamline the acquisition and processing of real estate data from Zillow's API, subsequently organizing this information into accessible formats for analytical purposes. By systematically extracting data, transforming it for consistency and clarity, and then persisting it to both flat files and a relational database, we aim to facilitate informed decision-making and analysis for stakeholders interested in real estate market trends.

The business requirement underpinning this initiative is to provide a robust, scalable, and automated pipeline that enables continuous monitoring and analysis of real estate listings and trends. This will empower our organization to make data-driven decisions, identify market opportunities, and track real estate performance with a high degree of accuracy and efficiency.

### System Architecture

#### Data Extraction (Bronze class)
The Bronze class is responsible for interacting with the Zillow API to fetch real estate data. It initializes by setting a base directory for raw data storage structured by date. The class has methods like getRequest to communicate with the Zillow API, getTotalPages to determine the number of pages of data available, and extractAndSaveRawData to retrieve and store data in JSON format. Data extraction iterates over pages of API responses and saves each page as a JSON file, adhering to rate limits by pausing between requests.

#### Data Transformation (Gold class)
The Gold class manages data transformation using PySpark. It starts by defining a Spark session and a schema for the real estate data. The getData method reads raw JSON files into a DataFrame, applying the predefined schema. The transformData function then cleanses and transforms this data, including parsing addresses, filling missing values, and calculating derived columns. The transformed data is prepared for persistence, with unnecessary columns removed and data types standardized.

#### Data Persistence
Saving to Files (SaveToFiles class)
The SaveToFiles class outlines the process for exporting transformed data to CSV files. It specifies a base directory for processed data and utilizes the PySpark DataFrame API to write data into partitioned CSV files based on the property type. This step enables efficient storage and future querying by categorizing the data into relevant subsets.

#### Saving to Database (SaveToDatabase class)
The SaveToDatabase class focuses on persisting transformed data to a PostgreSQL database. It establishes a JDBC connection using environment variables for authentication and configures the write operation to either overwrite or append data based on the load date. Before saving, it removes columns not needed in the database context, ensuring a clean and relevant dataset is stored.

#### Airflow Orchestration
While specific Airflow code is not provided, Apache Airflow can be used to orchestrate these batch processing tasks. Airflow DAGs (Directed Acyclic Graphs) would be configured to manage dependencies and execution order, starting with data extraction (Bronze), followed by transformation (Gold), and then persistence through file saving (SaveToFiles) and database insertion (SaveToDatabase). Each task would be represented as a node in the DAG, with edges defining their execution sequence, ensuring the entire pipeline is executed smoothly and efficiently.

<img width="973" alt="Screenshot 2024-03-13 at 10 08 06 PM" src="https://github.com/abhishekteli/-EstateFlow-Agile-Real-Estate-Data-Engineering-/assets/26431142/025bccea-90a0-4cb1-8016-513cd290fda5">
