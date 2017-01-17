

import datetime
import pytz
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import boto
import boto.s3
import sys
from boto.s3.key import Key
import psycopg2
from ConfigParser import SafeConfigParser


           

class RedshiftConnection:

        
    def __init__(self,conn_file=None):
        self.region = 'us-east-1'
        
        self.conn_str = None
        self.creds = {}
        self.connection = None

        if conn_file:
            parser = SafeConfigParser()
            parser.read(conn_file)

            with open(conn_file, 'r') as f:
                lines = f.readlines()
                self.conn_str = parser.get('global','load_conn_string') 
                 
    def get_connection(self):
        if not self.conn_str:
            raise Exception("You haven't defined a database connection string")

        if not self.connection:
            self.connection = psycopg2.connect(self.conn_str)
        return self.connection
 

       




if __name__ == '__main__':

    rs = RedshiftConnection(conn_file='.aws_creds')
    conn = rs.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id,name from location_group")
    for res in cursor.fetchall():
        print "%s: %s" % (res[0],res[1])

