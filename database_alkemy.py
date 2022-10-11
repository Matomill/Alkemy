from sqlalchemy import create_engine, sessionmaker, database_exist, create_database
from postgresql_setting import postgresql as settings
from data_process import df_unique, df_total_prov_cat, teatros_norm

def get_engine(user, passwd, host, port, db):
    url = create_engine(f'postgresql://{user}:{passwd}@{host}:{port}/{db}')
    if not database_exist(url):
        create_database(url)
    engine = create_engine(url, pool_size=50, echo=False)
    return engine

engine = get_engine(settings['pguser'],
                    settings['pgpasswd'],
                    settings['pghost'],
                    settings['pgport'],
                    settings['pgdb'])

def get_engine_from_settings():
    keys = ['pguser', 'pgpasswd', 'pghost', 'pgport', 'pgdb']
    if not all(key in keys for key in settings.keys()):
        raise Exception('see settings config')
    return get_engine(settings['pguser'],
                      settings['pgpasswd'],
                      settings['pghost'],
                      settings['pgport'],
                      settings['pgdb'])

def get_session():
    engine = get_engine_from_settings()
    session = sessionmaker(bind=engine)
    return session

session = get_session()

#get_engine(user_name, passwd_fill, host_number, port_number, db_name)

df_unique.to_sql('unified_table', con=engine, if_exists='replace')
df_total_prov_cat.to_sql('category_table', con=engine, if_exists='replace')
teatros_norm.to_sql('teatro_table', con=engine, if_exists='replace')
