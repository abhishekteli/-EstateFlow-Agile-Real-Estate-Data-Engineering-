# Real Estate Data Pipeline

## Phase 1: Real Estate Batch Processing

### Introduction
This section provides an in-depth overview of Phase 1, focusing on batch processing of real estate data from Zillow's API using Python, PySpark, PostgreSQL, and orchestrated with Apache Airflow.

### System Architecture
#### Data Extraction (Bronze class)
Details on how the Bronze class interacts with the Zillow API to fetch real estate data, including initialization, API interaction, and data storage.

#### Data Transformation (Gold class)
Explains the data processing steps undertaken by the Gold class using PySpark, such as schema definition, data loading, and transformation.

### Data Persistence
Describes how transformed data is persisted:

#### Saving to Files (SaveToFiles class): Outlines file export configurations and data writing process.
#### Saving to Database (SaveToDatabase class): Discusses database connection and data insertion strategies.

### Airflow Orchestration
Illustrates how Apache Airflow orchestrates the execution of batch processing tasks within this phase.

<img width="973" alt="Screenshot 2024-03-13 at 10 08 06 PM" src="https://github.com/abhishekteli/-EstateFlow-Agile-Real-Estate-Data-Engineering-/assets/26431142/025bccea-90a0-4cb1-8016-513cd290fda5">
