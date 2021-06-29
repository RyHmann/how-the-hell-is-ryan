import os
from dotenv import load_dotenv
import psycopg2
from configparser import ConfigParser
load_dotenv()



class Config(object):
    DEBUG = False
    DEVELOPMENT = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY", "this-is-the-default-key")
    DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True


class TestingConfig(Config):
    TESTING = True


weather_api_key = "id=2179537&appid=a84b5238c6d1533e7f7baaf8023abca4"
twit_api_key = "Qv7h5Pb8esnq0E4IKNTvdSDj0"
twit_api_secret_key = "9NYfLxhOhr6uvzSCgWXl0qSJds1TMCSCHXzdSEaio3Y4UzDkva"
twit_bearer_token = "AAAAAAAAAAAAAAAAAAAAAAEOPAEAAAAAJFU77d2OW4yzgMo54HNNRPevsco%3D3r53kxgLBDp7pu2v1FVZxmHwgCxUYyHM3QJwlel86WbRivH3p5"
twit_access_token = "1250237559826829313-WGoqSlEVdNMyBmvyKCOjUR1HbpQYlH"
twit_access_token_secret = "jN06fb20ad1a4XVcgTBcjjeivP0AenmM3NZ5anO1vh92N"

#DATABASE_URL = "postgres://localhost/howsryan"
#DATABASE_URL = "postgres://xqavmmnyymsrrz:96f0e788de4b96051aaa9b0ea455ba53c53c00af910cba5bc8659dd794743e5a@ec2-3-218-71-191.compute-1.amazonaws.com:5432/d1ikimune7ckeo"]


