from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
from flask_cors import CORS
from mosaic_runner import create_mosaic_file

app = Flask(__name__)
CORS(app)

@app.route('/api/upload', methods=['POST'])
def upload():
  x = request.args.get('x')
  y = request.args.get('y')
  pattern = request.args.get('pattern')

  if not pattern:
    return jsonify({"message": "No pattern provided"}), 400
  
  if not x or not y:
    return jsonify({"message": "No coordinates provided"}), 400
  
  try:
    x = int(x)
    y = int(y)
  except:
    return jsonify({"message": "Invalid coordinates"}), 400

  if 'file' not in request.files:
    return jsonify({"message": "No file part in the request"}), 400

  coordinates = (x, y)
  file = request.files['file']

  if file.filename == '':
    return jsonify({"message": "No file selected for uploading"}), 400
  

  if file and file.filename.endswith('.png'):
    filename = secure_filename(file.filename)
    file.save('./images/' + filename)

    try:
      transformed_filename = create_mosaic_file(filename, coordinates, pattern)
    except:
      return jsonify({"message": "Error creating mosaic"}), 500
    return send_file(transformed_filename, mimetype='image/png')
  else:
    return jsonify({"message": "Uploaded file is not a PNG file"}), 400

if __name__ == '__main__':
    app.run(debug=True)