""" script that gets a HTTP request and answer the browser """
#!/usr/bin/python3
# -*- coding: utf8 -*-
from flask import request, jsonify, render_template, url_for
from app import app
from api_pro7 import Parser, GeoCoding, WikiDatas



@app.route('/')
def index():
    """load welcome page"""
    url_ggle = "https://maps.googleapis.com/maps/api/js?key=AIzaSyCsqS4MLqsrTTmTkSCUNX97625NBJ4jXuI&language=fr"
    return render_template('index.html', title='Home', url_google = url_ggle)

@app.route("/index/question", methods=["POST"])
def question():
    """Answers the question"""
    data = request.get_json()
    parser = Parser(data["message"])
    parsed_msg = parser.crazy_parser()
    is_response = True
    print("Mot recherché >", parsed_msg)
    if parsed_msg is not None:
        try : 
            geo_tool = GeoCoding(parsed_msg)
            coord = [round(geo_tool.latitude, 5), round(geo_tool.longitude, 5)]
            wiki = WikiDatas(parsed_msg, 200)
            summary, url = wiki.access_page()
            return jsonify({"is_response": is_response, "message":parsed_msg, "coordinates":coord, \
                "summary":summary, "url":url})
        except:
            is_response = False
            message = "Désolé je ne connais pas cet endroit ... \nPeut-être pourrais-tu reformuler ou me poser une autre question ?"
            return jsonify({"is_response": is_response, "message": message })
    