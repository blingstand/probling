import requests
from flask import Flask
from flask_testing import TestCase

class MyTest(TestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True

        # Set to 0 to have the OS pick the port.
        app.config['LIVESERVER_PORT'] = 0

        return app

    def test_server_is_up_and_running(self):
        response = requests.get(self.get_server_url())
        self.assertEqual(response.code, 200)
"""
I ran pytest and got the folowing output.
output : 
(env) blingstand@blingstand-CX61-2QF:~/Bureau/openclassrooms/projets/probling$ pytest================================ test session starts ================================
platform linux -- Python 3.8.0, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
rootdir: /home/blingstand/Bureau/openclassrooms/projets/probling
collected 1 item                                                                    

app/tests/test_user_story.py F                                                [100%]

===================================== FAILURES ======================================
_______________________ MyTest.test_server_is_up_and_running ________________________

self = <app.tests.test_user_story.MyTest testMethod=test_server_is_up_and_running>

    def test_server_is_up_and_running(self):
>       response = requests.get(self.get_server_url())
E       AttributeError: 'MyTest' object has no attribute 'get_server_url'

app/tests/test_user_story.py:17: AttributeError
================================= warnings summary ==================================
env/lib/python3.8/site-packages/flask/_compat.py:139
  /home/blingstand/Bureau/openclassrooms/projets/probling/env/lib/python3.8/site-packages/flask/_compat.py:139: DeprecationWarning: 'flask.json_available' is deprecated and will be removed in version 2.0.0.
    self._warn()

-- Docs: https://docs.pytest.org/en/latest/warnings.html
"""
