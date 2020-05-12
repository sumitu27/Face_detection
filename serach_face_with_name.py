import boto3
import io
from PIL import Image
from update_dynamoDB import update_faces

rekognition = boto3.client('rekognition', region_name='us-east-2')
dynamodb = boto3.client('dynamodb', region_name='us-east-2')

def search_face_with_name(input_img_name):
    image = Image.open(input_img_name)
    stream = io.BytesIO()
    image.save(stream, format="JPEG")
    image_binary = stream.getvalue()
    threshold = 80
    maxFaces = 10

    response = rekognition.search_faces_by_image(
        CollectionId='family_collection',
        Image={'Bytes': image_binary},
        FaceMatchThreshold=threshold,
        MaxFaces=maxFaces
    )

    #print(response)
    return_response = ""
    for match in response['FaceMatches']:
        #print(match['Face']['FaceId'], match['Face']['Confidence'])

        face = dynamodb.get_item(
            TableName='family_collection',
            Key={'RekognitionId': {'S': match['Face']['FaceId']}}
        )

        if 'Item' in face:
            #print(face['Item']['FullName']['S'])
            return_response = face['Item']['FullName']['S']
            print("Face Identified::: ", return_response)
            update_faces("face_search_result", match['Face']['FaceId'], face['Item']['FullName']['S'])
        else:
            print('no match found in person lookup')

    return return_response