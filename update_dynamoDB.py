import boto3
import datetime

dynamodb = boto3.client('dynamodb')

def update_index(tableName,faceId, fullName):
    response = dynamodb.put_item(
        TableName=tableName,
        Item={
            'RekognitionId': {'S': faceId},
            'FullName': {'S': fullName}
            }
        )

def update_faces(tableName,faceId, fullName):
    current_time_stmp = str(datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S"))
    response = dynamodb.put_item(
        TableName=tableName,
        Item={
            'face_id': {'S': faceId},
            'FullName': {'S': fullName},
            'TimeStamp': {'S': current_time_stmp}
            }
        )