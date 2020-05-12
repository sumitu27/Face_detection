import boto3

def search_face_in_database(bucket, collectionId, fileName):

    threshold = 70
    maxFaces = 2

    client = boto3.client('rekognition')

    response = client.search_faces_by_image(CollectionId=collectionId,
                                            Image={'S3Object': {'Bucket': bucket, 'Name': fileName}},
                                            FaceMatchThreshold=threshold,
                                            MaxFaces=maxFaces)

    print(response)
    faceMatches = response['FaceMatches']
    print('Matching faces')
    for match in faceMatches:
        print('FaceId:' + match['Face']['FaceId'])
        print('Similarity: ' + "{:.2f}".format(match['Similarity']) + "%")

