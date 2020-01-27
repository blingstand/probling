# -*- coding: utf-8 -*-
from flask import request, jsonify, render_template
from app import app
from apiPro7 import Parser, GeoCoding, WikiDatas



@app.route('/')
def index():
    """load welcome page"""
    return render_template('index.html', title='Home')

@app.route("/index/question", methods=["POST"])

def question():
    """Answers the question"""
    data = request.get_json()

    parser = Parser(data["message"])
    parsed_msg = parser.crazy_parser()
    is_response = 0
    if parsed_msg is not None:
        is_response = 1
        geo_tool = GeoCoding(parsed_msg)
        coord = [round(geo_tool.latitude, 5), round(geo_tool.longitude, 5)]

        wiki = WikiDatas(parsed_msg, 200)
        summary, url = wiki.access_page()
        return jsonify({"is_response": is_response,
            "message":parsed_msg,
            "coordinates":coord,
            "summary":summary,
            "url":url})
    else:
        return jsonify({"is_response": is_response})

