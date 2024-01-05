from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
from flask_cors import CORS
from PNG import PNG
import mosaic

app = Flask(__name__)
CORS(app)

@app.route('/api/upload', methods=['POST'])
def upload():
  if 'file' not in request.files:
    return jsonify({"message": "No file part in the request"}), 400

  file = request.files['file']

  if file.filename == '':
    return jsonify({"message": "No file selected for uploading"}), 400
  

  if file and file.filename.endswith('.png'):
    png_file = PNG()
    filename = secure_filename(file.filename)
    file.save(filename)

    png_file.read_from_file(filename)
    mosaic.create_mosaic(png_file, (1,1), '1r2o3y4g3b2i1v')
    png_file.write_to_file('./temp/temp-image-mosaic.png')

    return send_file('./temp/temp-image-mosaic.png', mimetype='image/png')
  else:
    return jsonify({"message": "Uploaded file is not a PNG file"}), 400

if __name__ == '__main__':
    app.run(debug=True)