import requests
import zipfile
from io import BytesIO
import time
import numpy as np


start_time = time.time()

response = requests.get('http://localhost:1000/predict')

print('Elapsed time: {0} seconds'.format(time.time()-start_time))

zf = zipfile.ZipFile(BytesIO(response.content))
a = zf.read('pred')

# convert to numpy array
data = np.frombuffer(a, dtype='float')

# reshape to original data size
data = data.reshape((3000000, 6))


print('Data shape: ', data.shape)
print('First value: ', data[0])
print('Last value: ', data[-1])
