# GAF server Falcon-boilerplate 

A Python 3 boilerplate for the [Falcon](https://github.com/falconry/falcon) framework. Uses [gunicorn](https://github.com/benoitc/gunicorn) as the WSGI HTTP server and [meinheld](https://github.com/mopemope/meinheld) as the gunicorn worker. It also uses [Vyper](https://github.com/admiralobvious/vyper) for [12-factor](https://12factor.net/).

## Using

```
$ git clone https://github.com/vvitsenets/VICTORIA.git gaf_server
$ cd gaf_server
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r dev_requirements.txt
$ python run.py
```

To run the tests:

```
$ nose2 tests
```

# TODO
 - queue
 - requests to Police DB (stolen cars)
 - DB for users/images
 - game balance logic
 - deploy on Heroku


# VICTORIA

GAF - (grand auto finder). It's taken from the famous GTA. Only there was an theft auto . We will have a searcher of stolen cars.

The idea of the project is aimed to solve a social problem of stolen cars just by the most simple way. Especial using the mobile application.
