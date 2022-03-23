from sqlalchemy import create_engine
from config import config as cfg

def create_sqlalchemy_engine_conn():
    ts_engine = create_engine('postgresql://' + cfg.TIMESCALE_USERNAME + ':' +
                              cfg.TIMESCALE_PASSWORD + '@' +
                              cfg.TIMESCALE_HOST + ':' +
                              cfg.TIMESCALE_PORT + '/' +
                              cfg.TIMESCALE_SOCIAL_MEDIA_DB)
    return ts_engine


if __name__ == '__main__':
    conn = create_sqlalchemy_engine_conn()
    print('Successfully connected to TimescaleDB')
    print (conn.name)
