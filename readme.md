# Face Detection and Recognition using AWS Amazon Rekognition

This project was deployed using AWS EC2 instance and run application on AWS Lambda function. 

Components of Project:
  a. S3 Bucket
  b. Dynamo DB
  c. Amazon Rekognition
  
#Steps to use AWS resources with your system:
1.	Create IAM user with required access. Eg. If you want to use all resources then create IAM role with Admin access. You will get Access key ID and Secret access key.
2.	Download AWS CLI from AWS site.
3.	Type “aws configure” to setup Access key ID, Secret access key and region in which resource will be created.
4.	That’s it !!!


#Face Verification UI options:
1.	Create Face collection in AWS rekognition
2.	Add face to face collection
a.	It automatically stores FaceID in AWS DynamoDB with its name.
b.	It also copies image in S3 Bucket
3.	Delete Complete Face Collection.
4.	Detect faces from input image and compare with face collection.
a.	Draw red boxes on non-identified faces
b.	Draw green boxes on identified faces and display its name 
c.	Store the marked image in S3 Bucket
d.	Store name and time stamp in AWS DynamoDB

#Deployment:
1.	Install “Zappa” in your python environment.
2.	Type “zappa init” . It will create Json configuration file.
3.	Add one argument “ "slim_handler":true” to handle file more than 30 mb.
4.	Type “zappa deploy dev”. It will give you API address.


