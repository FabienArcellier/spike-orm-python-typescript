import os
import unittest

import requests

class TestSportsBackendTypescript(unittest.TestCase):
    def setUp(self):
        pass

    def test_players_query_should_returns_a_list_of_twenty_players(self):
        # Acts
        query = {'query': '{players {id, full_name}}'}
        host = os.getenv('SPORTSDB_BACKEND_TYPESCRIPT_HOSTS', 'localhost')
        r = requests.post(f'http://{host}:5000', json=query)

        # Assert
        self.assertEqual(200, r.status_code, f'output : {r.text}')

        reply = r.json()
        players = reply['data']['players']
        self.assertEqual(20, len(players))

def main():
    unittest.main()

if __name__ == '__main__':
    main()
