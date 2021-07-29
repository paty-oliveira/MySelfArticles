def connect_dynamodb():
    import boto3

    aws_session = boto3.Session()
    dynamodb_client = aws_session.resource("dynamodb")

    return dynamodb_client


def obtain_dynamodb_table(dynamodb_client, table_name):
    table = dynamodb_client.Table(table_name)

    return table


def query_dynamodb_table(table, filter_expression):
    response = table.query(KeyConditionExpression=filter_expression)

    return response['Items']


def convert_to_pandas_dataframe(data):
    import pandas as pd

    df = pd.DataFrame.from_dict(data)

    return df


def main():
    from boto3.dynamodb.conditions import Key

    dynamodb_client = connect_dynamodb()

    table_name = "test_dynamodb"
    raw_data = obtain_dynamodb_table(dynamodb_client, table_name)

    filter_expression = Key("execution_date").eq("2021-07-07")
    filtered_data = query_dynamodb_table(raw_data, filter_expression)

    df = convert_to_pandas_dataframe(filtered_data)
    df.head(10)


if __name__ == "__main__":
    main()
