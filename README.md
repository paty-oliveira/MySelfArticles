# Development Notes
This repository store useful solutions for problems that I was facing on during developments.

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
