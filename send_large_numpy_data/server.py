from flask import Flask, jsonify, send_file
import numpy as np
from io import BytesIO
import zipfile

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def predict():
    # 3 million test dataset
    sz = 3000000 

    # create 3,000,000 x 6 random floats
    pred = np.random.rand(sz, 6)

    # print first and last values in array
    print("First value: {0}".format(pred[0]))
    print("Last value: {0}".format(pred[-1]))
    
    # convert to bytes
    pred = pred.tobytes()

    # create in memory file
    memory_file = BytesIO() 

    # Create in memory zip file and write byte data
    with zipfile.ZipFile(memory_file, 'w') as zf:
        zf.writestr('pred', pred)
    
    # rewind to start
    memory_file.seek(0)

    # send file
    return send_file(memory_file, attachment_filename='small.zip')

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=1000, debug=True)