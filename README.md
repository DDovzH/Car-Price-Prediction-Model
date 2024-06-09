# Car Price Prediction Model

## Introduction

This project involved creating a car price prediction model that could be used in a car sales application. Various AWS services such as S3, AWS Glue, SageMaker, Lambda, and API Gateway were utilized in this project.

## Solution Architecture

### Components Description

- **Amazon S3**: Used for storing data such as input and output data of the model, configuration files, etc.
- **AWS Glue and Crawler**: Used for processing and preparing data for modeling. The Crawler automatically discovered and classified data in S3.
- **Amazon SageMaker**: Employed for training the car price prediction model, allowing the use of built-in machine learning algorithms or custom algorithms.
- **AWS Lambda**: A Lambda function was created to fetch input data from the application, process it, and send it to the SageMaker model to obtain the predicted price.
- **Amazon API Gateway**: An API was created to enable the application to communicate with the Lambda function via HTTP.

## Implementation Process

### Data Preparation

Car sales data was collected and stored in S3. AWS Glue was then used to process and clean the data.

### Model Training

The data was split into training and test sets, and SageMaker was used to train the car price prediction model.

### Lambda Function Deployment

A Lambda function was created to fetch input data, process it, and send it to the SageMaker model to get the price prediction.

### API Gateway Configuration

A new API was created in API Gateway, endpoints were configured, and integrations with the Lambda function were set up.

### Testing and Deployment

Each component was individually tested upon implementation, followed by testing the entire process from the application to obtaining the car price prediction.

## Conclusions and Perspectives

- Utilizing AWS services provided flexibility, scalability, and ease of management for the entire process, from data storage to model deployment in a production environment.
- Version control and monitoring capabilities available in SageMaker allowed for continuous model improvement as new data was acquired.
- The easy scalability provided by AWS services will enable handling a larger number of users and improve application performance in the future.

## Summary and Evaluation

The project yielded positive results, enabling the creation of an efficient car price prediction model that can be easily integrated with an application. Utilizing AWS services ensured the flexibility and efficiency of the entire solution. The car price prediction model achieved an average error rate of 5%.






# Setup Guide

This guide will walk you through the setup process for creating an S3 bucket, configuring AWS Glue, setting up an Amazon SageMaker instance, deploying a Lambda function, and creating an API Gateway. Follow the steps carefully to ensure a smooth setup.

## S3 Bucket

1. Create an S3 bucket.
2. Upload the `Ad_table.csv` file to the bucket.

## AWS Glue

1. Navigate to AWS Glue.
2. In the left menu, click on Crawlers under the Data Catalog section.
3. Create a new crawler:
   - Select the S3 bucket you created as the datasource.
   - Choose `LabRole` as the role.
   - Create a new database for the output.
   - Set the frequency to `On Demand`.
4. Select the newly created crawler and click `Run`. Once it completes, a new table should appear under the Tables section in the left menu.
5. Go to the ETL jobs tab under the Data Integration and ETL section.
6. In the Create job block, click on the Script editor:
   - Set the engine to Spark.
   - Choose `Upload script` and upload the `glue_job.py` file.
7. Make the necessary changes to the script. In the job details tab, add the required role, name the job at the top left, click `Save`, and then `Run`. Wait for it to complete. A folder named `transformed-data` with a CSV file should appear in the S3 bucket.

## Amazon SageMaker

1. Navigate to Notebook instances under the Notebook section and create a new instance:
   - Select `ml.t3.xlarge` as the instance type.
   - Wait for the instance to be created.
2. Click on `Open JupyterLab` and upload the `Model.ipynb` file. Follow the steps in the notebook, ensuring you follow the comments closely.
3. If no errors occur, copy the endpoint name from the second to last step. You will need this later.

## Lambda

1. Go to the Functions section.
2. Create a new function:
   - Select `Python 3.12` as the runtime.
   - Change the default execution role to `LabRole`.
3. Click `Upload from`, select `.zip file`, and upload `PredictionService.zip`. Once uploaded, click `Deploy`.
4. Navigate to the Configuration tab, select Environment variables, create a new variable:
   - Set `ENDPOINT_NAME` as the key.
   - Set the copied endpoint name as the value.

## API Gateway

1. Click on `Create API`.
2. Select `Rest API` and click `Build`.
3. Name the API and create it.
4. Once created, click on `Create Resource`, name it, and create it.
5. Select your resource and click `Create Method`.
6. Set the method type to `POST`.
7. Set the integration type to `Lambda function`.
8. Enable Lambda proxy integration.
9. Search for your Lambda function by name and select it.
10. Create the method.
11. Select your method, scroll down to the Test section, and enter the following JSON:
    ```json
    {
      "maker": "Bentley",
      "color": "Silver",
      "reg_year": 2000,
      "bodytype": "Saloon",
      "runned_miles": 60000,
      "engin_size": 6.8,
      "gearbox": "Automatic",
      "fuel_type": "Petrol",
      "seat_num": 5,
      "door_num": 4
    }
    ```
    Ensure it returns a status 200 and a body with a `price` field in float format.
12. If successful, click `Deploy API`, select `new stage`, name it, and click `Deploy`.
13. Click on the `+` next to the stage name, expand all sections until you reach `POST`, and click on it. Copy the Invoke URL. This is your API endpoint. You can test it using Postman or Thunder Client in VS Code.
