import boto3
import json, os
import cv2
from serach_face_with_name import  search_face_with_name
from s3_bucket import store_image_into_s3_bucket

def detect_faces_in_image(photo, bucket, upload_file_name):
    client = boto3.client('rekognition')
    image = cv2.imread(upload_file_name)
    h, w, c = image.shape
    response = client.detect_faces(Image={'S3Object': {'Bucket': bucket, 'Name': photo}}, Attributes=['ALL'])
    count = 1
    return_response = []
    print('Detected faces for ' + photo)
    for faceDetail in response['FaceDetails']:
        #print('The detected face is between ' + str(faceDetail['AgeRange']['Low'])
        #     + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
        #print('Here are the other attributes:')
        #print(json.dumps(faceDetail, indent=4, sort_keys=True))
        start_point = (int(faceDetail['BoundingBox']['Left'] * w), int(faceDetail['BoundingBox']['Top'] * h))
        end_point = (int((faceDetail['BoundingBox']['Left'] + faceDetail['BoundingBox']['Width']) * w),
                     int((faceDetail['BoundingBox']['Top'] + faceDetail['BoundingBox']['Height']) * h))
        count += 1
        crop_img = image[start_point[1]:end_point[1], start_point[0]:end_point[0]]
        crop_file_name = r"./detect_faces/" + str(count) + ".jpeg"
        cv2.imwrite(crop_file_name, crop_img)

        face_identified = search_face_with_name(crop_file_name)
        if face_identified.strip():
            image = cv2.rectangle(image, start_point, end_point, (0, 255, 0), 3)
            return_response.append(face_identified)
        else:
            image = cv2.rectangle(image, start_point, end_point, (0, 0, 255), 3)

    output_image = r"./output/" + os.path.basename(upload_file_name)
    cv2.imwrite(output_image, image)
    store_image_into_s3_bucket(output_image, os.path.basename(upload_file_name), "index/" + os.path.basename(upload_file_name))

    return return_response

