import boto3


def list_faces_in_collection(collection_id):
    maxResults = 2
    faces_count = 0
    tokens = True

    client = boto3.client('rekognition')
    response = client.list_faces(CollectionId=collection_id,
                                 MaxResults=maxResults)

    print('Faces in collection ' + collection_id)
    return_response = []
    while tokens:

        faces = response['Faces']

        for face in faces:
            print(face)
            return_response.append(face)
            faces_count += 1
        if 'NextToken' in response:
            nextToken = response['NextToken']
            response = client.list_faces(CollectionId=collection_id,
                                         NextToken=nextToken, MaxResults=maxResults)
        else:
            tokens = False
    return return_response

