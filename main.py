import image
from flask import Flask
from flask_cors import CORS
from flask import request, jsonify
import tensorflow as tf
from datetime import datetime

# instantiate the app
app = Flask(__name__)
cors = CORS(app)

# Loading model before receiving request
loading_time = datetime.now()
print('Time at which the model and weights are loaded: ',loading_time)
model, class_names = image.load_model_weights(loading_time)

@app.route('/', methods=['GET', 'POST'])
def giveDirection():
    Start_time = datetime.now()
    if request.method == "POST":
        file = request.files.get('file')
        if file is None or file.filename == "":
            return jsonify({"error": "no file"})
        try:
            file_name = file.read()
            img_tensor = tf.io.decode_image(file_name)
            direction = image.navigation(img_tensor, Start_time, model, class_names)
            return direction
        except Exception as e:
            return jsonify({"error": str(e)})
    else:
        return 'OK' 


if __name__ == '__main__':
    app.run(debug=True, port=5000)