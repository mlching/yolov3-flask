import image
from flask import Flask
from flask_cors import CORS
from flask import request

# instantiate the app
app = Flask(__name__)
cors = CORS(app)

@app.route('/', methods=['GET', 'POST'])
def giveDirection():
    if request.method == "POST":
        filter_data = request.get_json()
        try:
            img_path = filter_data['image_path']
            direction = image.navigation(img_path)
            return direction
        except Exception as e:
            return jsonify({"error": str(e)})
    else:
        return 'OK' 


# @app.route('/', methods=['GET', 'POST'])
# def giveDirection2():
#     img_path = 'data/test.jpeg'
#     direction = image.navigation(img_path)
#     return direction

if __name__ == '__main__':
    app.run(debug=True)