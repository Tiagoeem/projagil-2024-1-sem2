from flask import Flask, request
import json

app = Flask("nome_da_minha_aplicacao")

@app.route('/')
def hello_world():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
