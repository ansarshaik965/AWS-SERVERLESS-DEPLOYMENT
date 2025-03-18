import json
import boto3


# Define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
    # Create a DynamoDB object using the AWS SDK
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # put here your region 
    # Use the DynamoDB object to select our table
    table = dynamodb.Table('student_data') # put your dynamodb table name 
    # Extract values from the event object we got from the Lambda service and store in variables
    student_id = event['studentid']
    name = event['name']
    student_class = event['class']
    age = event['age']
    
    headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "OPTIONS, GET, POST",
        "Access-Control-Allow-Headers": "Content-Type"
    }

    # Write student data to the DynamoDB table and save the response in a variable
    response = table.put_item(
        Item={
            'studentid': student_id,
            'name': name,
            'class': student_class,
            'age': age
        }
        
    )
    
    # Return a properly formatted JSON object
    return {
        'statusCode': 200,
        'body': json.dumps('Student data saved successfully!')
    }
