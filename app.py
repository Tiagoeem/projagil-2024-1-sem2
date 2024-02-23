from flask import Flask, request
import psycopg2
import json

app = Flask("nome_da_minha_aplicacao")

conn = psycopg2.connect(
    dbname="",
    user="",
    password="",
    host=""
)

@app.route('/')
def hello_world():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
