import boto3

def store_image_into_s3_bucket(img_name, metainfo, file_name):
    s3 = boto3.resource('s3')

    file = open(img_name,'rb')
    object = s3.Object('my-personal-data-sumit', file_name)
    ret = object.put(Body=file,
                    Metadata={'FullName':metainfo}
                    )


def retrive_from_s3_bucket(filename):
    s3 = boto3.resource('s3')
    local_file_name = 'my_localimage.jpg'
    s3.Bucket('my-personal-data-sumit').download_file(filename, local_file_name)

    return local_file_name