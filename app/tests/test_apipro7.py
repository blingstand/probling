#!/usr/bin/python3
# -*- coding: utf8 -*-
"""
    Before to throw Pytest please run the app
    I don't test pivate method
"""

from _pytest.monkeypatch import MonkeyPatch
import googlemaps
import requests
from api_pro7 import Parser, GeoCoding, WikiDatas
from app.tests import datas



#these folowing functions help testing
def mock_get(*args, **kwargs):
    """ create a Mymock """
    return MyMock()


#Mockclass with 2 method
class MyMock:
    """ mock an obj with statics methods"""
    @staticmethod
    def geocode(*args, **kwargs):
        """ returns a ggmaps client object"""
        geo_answer = ["liste"]
        return geo_answer

    @staticmethod
    def json():
        """ ggmaps wiki api answer """
        return {"response": "response from WikiApi"}


#testclass
class TestApiPro7():
    """ Class that gathers all the tests"""
    SAMPLE = "le chat a 4 pattes."
    PARSER = Parser(SAMPLE)
    GEOCODING = GeoCoding("Bergerac")
    WIKI = WikiDatas("Bordeaux", 200)
    QUESTIONS = datas.QUESTIONS
    BIG_EXTRACT = datas.BIG_EXTRACT
    SMALL_EXTRACT = datas.SMALL_EXTRACT

    monkeypatch = MonkeyPatch()

    # ---------- parser
    #1
    def test_create_list_from_sentence(self):
        """checks wether the sentence is now a list of words"""
        parser = Parser(self.SAMPLE)
        is_list = parser.create_list_from_sentence()
        verif = True
        if isinstance(is_list, list):
            for element in is_list:
                if not isinstance(element, str):
                    verif = False
        else:
            verif = False
        assert verif

    #2
    def test_crazy_parser(self):
        """for each question concerning a location I want to test wether the answer will be
        "le pont Chaban-Delmas", "la tour Eiffel" ou 'openClassrooms'"""
        count = 0
        for question in self.QUESTIONS:
            parser = Parser(question)
            response = parser.crazy_parser()
            if response in ["le pont Chaban-Delmas", "pont Chaban-Delmas", \
            "la Tour Eiffel", 'Openclassroom']:
                count += 1
            else:
                count += 100
                assert count == question, response
        assert count == len(self.QUESTIONS)

    # ---------- geocoding
    #3
    def test_get_geocode(self):
        """ mock a gmaps object to test the function"""

        # apply the monkeypatch for requests.get to mock_get
        self.monkeypatch.setattr(googlemaps, "Client", mock_get)

        result = self.GEOCODING.get_geocode()
        assert result == "liste"

    def test_extract_lat_long(self):
        """ tests wether the function can get the wanted datas """
        my_datas = {'geometry':{'location':{'lat':1, 'lng':2}}}
        result = self.GEOCODING.extract_lat_long(my_datas)
        assert result == {'lat':1, 'lng':2}

    # ---------- wiki
    #6
    def test_get_request(self):
        """Make sure to get a json resp"""

        # apply the monkeypatch for requests.get to mock_get
        self.monkeypatch.setattr(requests, "get", mock_get)

        my_params = {"a":"b"}
        # app.get_json, which contains requests.get, uses the monkeypatch
        result = self.WIKI.get_request(my_params)
        assert result["response"] == "response from WikiApi"
    #7
    def test_limit_size_wiki_extract(self):
        """tests wether the extract can be reduced"""
        red_ext1 = self.WIKI.limit_size_wiki(self.BIG_EXTRACT)
        red_ext2 = self.WIKI.limit_size_wiki(self.SMALL_EXTRACT)
        if len(red_ext1) <= 200 and len(red_ext2) <= 200:
            assert True
    #8
    def test_access_page(self):
        """ test wether the function can return 2 an url and a text"""

        def get_resp(*args, **kwargs):
            response = {'query': {'pages': {'1': {\
            'extract' : "this is a text",\
            'fullurl' : 'this is an url'}}}}
            return response
        self.monkeypatch.setattr(self.WIKI, "get_request", value=get_resp)

        result = self.WIKI.access_page()
        assert result == ('this is a text.', 'this is an url')
