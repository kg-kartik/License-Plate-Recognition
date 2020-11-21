from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin
import shutil
import requests
from werkzeug.datastructures import Headers
from detection import plate, ocr
from PIL import Image
import os


app = Flask(__name__)
CORS(app)
api = Api(app)

class Detection(Resource):
    def post(self):
        
        try:
            os.mkdir("detection/IMG_UPLOAD/")
        except Exception as e:
            print(e, " dorectory already exists")

        try:
            os.mkdir("detection/IMG_CROP/")
        except Exception as e:
            print(e, " dorectory already exists")

        image = request.files["image"]
        image_name = image.filename
        PATH_UPLOAD = os.path.join(os.getcwd(), "detection/IMG_UPLOAD")
        PATH_CROP = os.path.join(os.getcwd(), "detection/IMG_CROP")
        image.save(os.path.join(PATH_UPLOAD, image_name))
        plate.run_detections()
        result = ocr.plate_to_sting()
        # os.remove(os.path.join(PATH_UPLOAD, image_name))
        shutil.rmtree(PATH_UPLOAD)
        shutil.rmtree(PATH_CROP)
        URL = "http://shrouded-falls-48764.herokuapp.com/vehicle-info/" + result
        response = requests.get(URL, headers={"API-Key": "a2bfed7a222b469d99ca258b1f340712"}).json()
        return response

api.add_resource(Detection, "/upload")

if __name__ == "__main__":
    app.run(debug=True,port=5000)