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

## Phase 2: Real-Time Data Processing

### Stream Extraction (streamingBronze class)
Explains the operation of the streamingBronze class for real-time data extraction from the Zillow API and streaming into Kafka.

### Stream Transformation and Load (streamingGold class)
Describes how the streamingGold class consumes Kafka data, applies transformations, and loads it into PostgreSQL for real-time analysis.

### Integration and Workflow
Outlines the workflow integrating real-time data capture, processing, and user interaction for timely insights into the real estate market.

## Phase 3: Future Enhancements

### Advanced House Price Valuation
Describes the planned integration of a predictive model for property valuation to provide market trend insights and investment guidance.

### AI-Driven Real Estate Chatbot
Details the development of an AI-powered chatbot to offer an interactive platform for users to query real estate data.

## Conclusion
Summarizes the project's current achievements and future roadmap, emphasizing the envisioned enhancements to transform the data pipeline into a comprehensive analytical tool.
