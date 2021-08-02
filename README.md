# Development Notes
This repository stores useful solutions for problems that I was facing on during developments.

### [Processing data from DynamoDB using Python](dynamodb_data_processing/dynamodb.py)

Amazon Web Services offers many ways for querying data in [DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html):
1. AWS Console for DynamoDB
2. NoSQL Workbench for DynamoDB
3. AWS CLI
4. AWS SDK

There are a lack of flexibility querying data using the AWS Console or NoSQL Workbench. Thus, another way to process
data from DynamoDB is to build a script using AWS SDK. For this situation, I used [boto3](https://github.com/boto/boto3) 
library for Python.
 
This option allows me to build a simple script to retrieve data from DynamoDB table, and process it 
using common libraries such as [pandas](https://github.com/pandas-dev/pandas). This approach gave me a lot of freedom to
test locally and process data in a intuitive way, avoiding the addiction of a new component to the infrastructure, 
such as [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function. 

Another important point: DynamoDB calls through SDK does not have costs associated, while querying data using Console or
Workbench has. 


### [Testing data quality using PyDeequ](data_quality_with_pydeequ/pydeequ.py)
[Deequ](https://github.com/awslabs/deequ) is a AWS library built on top of [Apache Spark](https://github.com/apache/spark)
for defining *unit-test* for data, which measure data quality in
large datasets. Some of data quality metrics available:

- Completeness
- Uniqueness
- Consistency
- Size
    
Deequ provides features like: 
- **Data Profiling:** supports single-column profiling of such data;
- **Constraint Suggestions:** provides built-in functionality to assist users in finding reasonable constraints 
for their data;
- **Metrics Computation:** once we know what to test, we can run tests to compute the metrics;
- **Constraint Verification:** we can put test cases and get result to be used for the reporting.

This tool can be integrated in AWS services, such as [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) 
and [SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/gs.html), or locally using [PyDeequ](https://github.com/awslabs/python-deequ) 
library for Python. 
The evaluation of data quality metrics can be performed in many steps of ETL or ELT pipeline, such as:
    
- Validation of source data
- Validation of source data load
- Validation of transformed data