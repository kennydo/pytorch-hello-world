from flask import Flask
import torch
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/torchrand')
def torch_rand():
    return str(torch.rand(5, 3))

