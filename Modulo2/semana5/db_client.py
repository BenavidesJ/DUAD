import psycopg2

class DBClient:
  def __init__(self, db_name, user, password, host, port=5432):
    self.db_name = db_name
    self.user = user
    self.password = password
    self.host = host
    self.port = port
    
    self.connection = self.create_connection()
    if self.connection:
      print("Connected to the database successfully")
      self.cursor = self.connection.cursor()
    
  def create_connection(self):
    try:
      conn = psycopg2.connect(
        dbname=self.db_name,
        user=self.user,
        password=self.password,
        host=self.host,
        port=self.port
      )
      return conn
    except Exception as err:
      print(f"Error connecting to the database: {err}")
      return None
   
  def close_connection(self):
    if self.cursor:
      self.cursor.close()
    if self.connection:
      self.connection.close()
      print("Connection closed successfully")
  
  def execute_query(self, query, *args):
    try:
        self.cursor.execute(query, args)
        if query.strip().lower().startswith("select"):
            result = self.cursor.fetchall()
        else:
            self.connection.commit()
            result = self.cursor.rowcount
        return result
    except Exception as err:
        print(f"Error executing query: {err}")
        return None

