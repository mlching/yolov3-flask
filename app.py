import image
from flask import Flask
from flask_cors import CORS
from flask import request

# instantiate the app
app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=['GET', 'POST'])
def giveDirection():
    filter_data = request.get_json()
    print(filter_data)
    img_path = filter_data['image_path']
    direction = image.navigation(img_path)
    return direction

if __name__ == '__main__':
    app.run(debug=True)