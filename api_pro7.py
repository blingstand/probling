""" script with 3 classes usefull for views.py """

#!/usr/bin/python3
# -*- coding: utf8 -*-

import googlemaps
import requests

class Parser():
    #class that handles the parsing methods
    COURTESY = ["stp", "s'il te plait", "s'il te plaît", "svp", "s'il vous plaît", \
     "s'il vous plait"]
    CONNAITRE = ["connais", "connaissez", "connais-tu", "Connais-tu", \
    "connaissez-vous", "Connaissez-vous"]
    POUVOIR = ["peux-tu", "Peux-tu", "pouvez-vous", "Pouvez-vous"]
    SAVOIR = ["sais-tu", "Sais-tu", "savez-vous", "Savez-vous"]
    AVOIR = ["as-tu", "As-tu", "avez-vous", "Avez-vous"]

    def __init__(self, sentence): #2 methods and 8 pivate methods
        self.sentence = sentence
        self.list_of_words = self.create_list_from_sentence()


    def _take_off_ponctuation(self, sentence):
        """returns a sentence without ponctuation"""
        for ponctuation in ".!?;":
            sentence = sentence.replace(ponctuation, " ")
        return sentence
    def _take_off_courtesy(self, sentence):
        """returns a sentence without ponctuation"""
        for courtesy in self.COURTESY:
            sentence = sentence.replace(courtesy, "")
        return sentence

    def create_list_from_sentence(self):
        """returns a list of words for parser without ponctuation signe"""
        sentence = self.sentence
        sentence = self._take_off_ponctuation(sentence)
        sentence = self._take_off_courtesy(sentence)
        #no space
        list_of_words = sentence.split(" ")
        print("list_of_words : ", list_of_words)
        try:
            list_of_words.remove("")
            
        except Exception as e:
            pass
        response = []
        for word in list_of_words:
            if len(word) > 0:
                response.append(word)
        return response

    def _whereparser(self, index, list_of_words):
        """ extract the important expression in a where case"""
        if list_of_words[index+1 : index+3] in (['se', 'trouve'], ['se', 'situe']):
            return list_of_words[index+3:]
        elif list_of_words[index+1] in ("est", "trouve-t'on"):
            return list_of_words[index+2:]


    def _in_doyouknow(self, index, list_of_words):
        """ deals with complex cases of _doyouknow cases"""
        if "propos" in list_of_words:
            new_index = list_of_words.index("propos")
            if list_of_words[new_index-1] == "à":
                return list_of_words[new_index+2:]
        elif "sur" in list_of_words:
            new_index = list_of_words.index("sur")
            if list_of_words[new_index-2: new_index] == ["quelque", "chose"] or \
            list_of_words[new_index-1] in ["informations", "infos"]:
                return list_of_words[new_index+1:]
        return list_of_words[index+1:]

    def _doyouknow(self, index, list_of_words):
        """ extract the important expression in a _doyouknow case"""
        response = ""
        if list_of_words[index+1] == "l'adresse":
            if list_of_words[index+2] == ['de', 'du', 'des']:
                response = list_of_words[index+3:]
            response = list_of_words[index+2:]
        elif list_of_words[index+1] in ["de", "du", "des"] and \
        list_of_words[index+2] != "informations":
            return list_of_words[index+2:]
        else:
            response = self._in_doyouknow(index, list_of_words)
        return response

    def _canyoutalkabout(self, index, list_of_words):
        """ extract the important expression in a _canyoutalkabout case"""
        response = ""
        if list_of_words[index+1 : index+3] == ['me', 'parler']:
            response = list_of_words[index+4:]
        return response

    def _check_presence_extra_proposition(self, response):
        """ in presence of extra proposition in response returns list of word
        before relative pronoun"""
        to_return = response
        for index, word in enumerate(response):
            if word == "qui":
                to_return = response[:index]
        return to_return

    def _canyouspeakabout(self, index, list_of_words):
        """ extract the important expression in a _canyouspeakabout case"""
        response = ""
        if list_of_words[index+1] == 'sur':
            response = list_of_words[index+2:]
        return response

    def crazy_parser(self):
        """extract the subject of the future search from a sentence"""
        response = ""
        list_of_words = self.list_of_words
        for index, word in enumerate(list_of_words):
            #is-there interrogative word ?
            if word in [u"où", u"Où"]:
                response = self._whereparser(index, list_of_words)
            elif word in self.CONNAITRE or word in self.SAVOIR or word in self.AVOIR:
                response = self._doyouknow(index, list_of_words)
            elif word in self.POUVOIR:
                response = self._canyoutalkabout(index, list_of_words)
            elif word == "dire":
                response = self._canyouspeakabout(index, list_of_words)
            else:
                pass

        if response in ("", None):
            print("pb : ", list_of_words) #for debug
        else:
        #Be carefull : crazy_parser has to return a string
            to_return = ""
            checked_response = self._check_presence_extra_proposition(response)
            for element in checked_response:
                to_return += element + " "
            to_return = to_return[:len(to_return)-1]

            if to_return[:2] == "d'":
                return to_return[2:]
            if to_return[:2] == "du":
                return to_return[3:]
            return to_return

class GeoCoding(): #2 methods
    """ Class that handles with GGM API"""
    def __init__(self, exp_to_search):
        self.api_key = "AIzaSyCsqS4MLqsrTTmTkSCUNX97625NBJ4jXuI"
        self.exp_to_search = exp_to_search + ", france"
        #use ggm to get coordinate from a given expression
        self.geocode = self.get_geocode() 
        self.coordinates = self.extract_lat_long(self.geocode)
        #define lat and long
        self.latitude = self.coordinates["lat"]
        self.longitude = self.coordinates["lng"]

    def get_geocode(self):
        """ asks gmaps api for geocode, using an expression  """
        gmaps = googlemaps.Client(key=self.api_key)
        geocode_result = gmaps.geocode(self.exp_to_search)
        geocode = geocode_result[0]
        return geocode

    def extract_lat_long(self, dico):
        """ returns the location datas from a given code """
        geo = dico["geometry"]
        location = geo["location"]
        return location

class WikiDatas(): #3 methods
    """ class that handles with WikiApi """
    def __init__(self, title, size):
        self.title = title
        self.size = size
        self.base = "https://fr.wikipedia.org/w/api.php?"

    def get_request(self, params):
        """ returns a JSON response from a given API """
        params['format'] = "json"
        params['action'] = "query"
        response = requests.get(self.base, params=params)
        return response.json()

    def limit_size_wiki(self, my_text):
        """limits the size of the wiki text and
        add ... at the end"""

        if len(my_text) >= self.size:
            reduced_text = ""
            for caracter in my_text:
                if len(reduced_text) <= self.size: #to add "..." at the end
                    reduced_text += caracter
                else:
                    if reduced_text[-1] == ".":
                        reduced_text += ".."
                        return reduced_text
                    else:
                        reduced_text = reduced_text[:-1] + "..."
                        return reduced_text
        my_text += "."
        return my_text

    def access_page(self):
        """ returns the summary and the url of the page

            1/ call get_request
            2/ get the page id
            3/ get the url and the summary
            4/ reduce the size of the summary

            """
        params = {
            'prop' : 'extracts|info',
            'exlimit' : 1,
            'inprop': 'url',
            'ppprop': 'disambiguation',
            'redirects': '',
            'exintro' : "",
            'explaintext' : "",
            'titles' : self.title
        }
        response = self.get_request(params)
        get_id = response['query']['pages']
        for i in get_id:
            pageid = i
        big_summary = response['query']['pages'][pageid]['extract']
        url = response['query']['pages'][pageid]['fullurl']

        summary = self.limit_size_wiki(big_summary)
        return summary, url
        