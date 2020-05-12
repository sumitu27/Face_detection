import boto3
from create_collection_for_face import create_collection
from search_face_in_database import search_face_in_database
from add_face_in_collection import add_faces_to_collection
from detect_faces_from_image import detect_faces



if __name__ == "__main__":

    bucket = 'my-personal-data-sumit'
    collectionId = 'family_collection'
    fileName = 'family.jpg'
    threshold = 70
    maxFaces = 2

    # Create collection to store faces
    create_collection(collectionId)

    # Add Faces to database
    indexed_faces_count = add_faces_to_collection(bucket, fileName, collectionId)
    print("Faces indexed count: " + str(indexed_faces_count))


    # Detect faces in image
    face_count = detect_faces(fileName, bucket)
    print("Faces detected: " + str(face_count))


    # Search faces in database
    search_face_in_database(bucket, collectionId, fileName)

