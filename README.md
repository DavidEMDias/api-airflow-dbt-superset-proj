# 🌦️ Weather Data Engineering Pipeline

Role: Data Engineer
Tools Used: Airflow, Docker, PostgreSQL, SQL-based transformation (dbt), Python scripts and DAGs, Apache Superset.

An end-to-end **ELT (Extract, Load, Transform)** data pipeline that ingests live weather data, loads it into PostgreSQL, transforms and enriches it using dbt, and produces analytical visualizations — fully automated and containerized.

---

## 📌 Problem

Weather data is commonly exposed through external APIs in raw and semi-structured formats. While this data is valuable, it is not immediately suitable for analytics, reporting, or decision-making.

Key challenges addressed by this project include:
- Reliable ingestion of live weather data
- Storing raw data for traceability and reprocessing
- Transforming and enriching data for analytical use cases
- Automating pipeline execution
- Making insights accessible through visualizations

---

## 🎯 Objectives

The main objectives of this project are to:

- Ingest live weather data from a public API
- Load raw weather data directly into PostgreSQL
- Transform and enrich data using dbt
- Orchestrate and automate the ELT pipeline
- Create visualizations for data exploration and insight generation
- Provide a reproducible, containerized setup

---

## 🛠️ Solution Approach

This project implements a modern **ELT (Extract, Load, Transform)** architecture using industry-standard data engineering tools.

### Architecture Overview

In construction

### Pipeline Components

1. **Extract**
   - Live weather data is pulled from an external Weather API using Python.
   - Data is ingested in its raw form without upfront transformations.

2. **Load**
   - Raw weather data is first loaded into a PostgreSQL database.
   - This preserves source data for auditing, backfills, and reprocessing.

3. **Transform (dbt)**
   - dbt is used to transform raw data directly inside PostgreSQL.
   - Transformations include:
     - Data cleaning and normalization
     - Unit conversions (e.g., temperature, wind speed)
     - Timestamp standardization
     - Creation of analytics-ready models

4. **Orchestration & Automation**
   - Apache Airflow orchestrates the entire ELT workflow.
   - dbt runs are triggered as downstream tasks after data loading.

5. **Reporting & Visualization**
   - Transformed dbt models are used to power dashboards and charts.
   - Enables trend analysis and data-driven insights, in our case leveraging Apache Superset.

6. **Containerization**
   - Docker is used to containerize all components of the pipeline.
   - Ensures consistent environments across development and deployment.

---

## 📊 Key Results

- ✅ Fully automated ELT weather data pipeline  
- ✅ Raw data preserved in PostgreSQL for traceability  
- ✅ Scalable, SQL-based transformations powered by dbt  
- ✅ Orchestrated and monitored using Apache Airflow  
- ✅ Analytics-ready datasets and meaningful visualizations using Apache Superset  
- ✅ Reproducible and portable deployment using Docker  

---

This repository demonstrates a **production-style ELT pipeline** for real-time weather analytics, leveraging PostgreSQL and dbt for scalable and maintainable data transformations.
