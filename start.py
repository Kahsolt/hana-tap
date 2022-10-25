#!/usr/bin/env python3
# Author: Armit
# Create Time: 2022/10/25 

from flask import Flask
from flask import send_file

app = Flask('hana-tap')


@app.route('/')
def root():
  return send_file('index.html')


if __name__ == '__main__':
  app.run(host='127.0.0.1', debug=True)
