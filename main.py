from flask import Flask, request, jsonify,render_template
import util
from flask_cors import CORS, cross_origin


app=Flask(__name__)
CORS(app) 
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/',methods=['GET','POST'])
@cross_origin()
def hello():
   return render_template('app.html')

@app.route('/classify_image',methods=['GET','POST'])
@cross_origin()
def classify_image():
    image_data=request.form['image_data']

    response= jsonify(util.classify_image(image_data))

    return response


if __name__=='__main__':
    util.load_saved_artifacts()
    app.run(port=5000,debug=True)