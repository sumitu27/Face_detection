from flask import Flask, render_template, request
from flask import jsonify
from flask_cors import CORS
import os
from add_face_in_collection import add_faces_to_collection
from s3_bucket import store_image_into_s3_bucket
from show_list_of_faces import list_faces_in_collection
from detect_faces_from_image import detect_faces_in_image

app = Flask(__name__)
CORS(app)

@app.route('/upload')
def upload_file():
    return render_template('DetectFaces.html')

@app.route('/add_face', methods=['GET', 'POST'])
def add_face_in_collection():

    f = request.files["file"]
    upload_file_name = "./added_face/" + f.filename
    f.save("./added_face/" + f.filename)
    file_name, ext = os.path.splitext(os.path.basename(upload_file_name))

    store_image_into_s3_bucket(upload_file_name, file_name, os.path.basename(upload_file_name))

    add_faces_to_collection('my-personal-data-sumit', os.path.basename(upload_file_name), "family_collection")

    return "Face Added Successfully"


@app.route('/list_of_faces', methods=['GET', 'POST'])
def list_of_faces():
    collection_id = 'family_collection'

    faces_count = list_faces_in_collection(collection_id)

    return jsonify(faces_count)


@app.route('/detect_faces', methods=['GET', 'POST'])
def detect_faces():

    f = request.files["file"]
    upload_file_name = "./detect_faces/" + f.filename
    f.save("./detect_faces/" + f.filename)
    file_name, ext = os.path.splitext(os.path.basename(upload_file_name))

    store_image_into_s3_bucket(upload_file_name, file_name, os.path.basename(upload_file_name))

    return_response = detect_faces_in_image(os.path.basename(upload_file_name), 'my-personal-data-sumit', upload_file_name)

    return jsonify(return_response)

if __name__ == '__main__':
    app.run(debug=True, port="1001", host="0.0.0.0")