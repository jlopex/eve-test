eve-test
========

curl -d '[{"filename": "first_file", "fasplink": "fasp://test.test", "provider": "12345"}]' -H 'Content-Type: application/json'  http://127.0.0.1:5000/downloads

curl -X GET 'http://127.0.0.1:5000/downloads?where="provider"=="12345"'


