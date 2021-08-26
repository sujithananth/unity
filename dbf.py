import sqlite3

def text_in(name):
    sql_query="""
             CREATE TABLE IF NOT EXISTS  """+name+""" (
             id  INTEGER  PRIMARY KEY,
             title TEXT,
             link TEXT);
             """

    execute_query(sql_query)

def execute_query(sql_query):
    with sqlite3.connect('unite') as db:
        csr = db.cursor()
        results=csr.execute(sql_query)
        db.commit()
    return results

def insert_title_into_table(table,title,link):
    sql_query = """ INSERT INTO """+table+""" (title,link) VALUES("%s","%s")"""%(title,link)
    execute_query(sql_query)

       
def select_link_fromtable(table):
    sql_query = """ SELECT link from """+table+""" """
    result = execute_query(sql_query)
    #return(result.fetchall())
    return [result[0] for result in result.fetchall()]


def select_titles_fromtable(table):
    sql_query = """ SELECT title  from """+table+""" """
    result = execute_query(sql_query)
    #return(result.fetchall())
    return [result[0] for result in result.fetchall()]

def select_from_table(table):
    sql_query = """SELECT *  from  """+table+""" """
    result = execute_query(sql_query)
    print(result.fetchall())
    #return [result[0] for result in result.fetchall()]

def delete_from_table(name,song):
    #here query is to  deletes the respective song from the respective table    
    sql_query = """DELETE FROM """+name+""" * """
    #again execute our query                                                    
    execute_query(sql_query)

def delete_tables(table):
    #here query is to  deletes the respective song from the respective table   
    sql_query = """DROP  TABLE IF EXISTS """+table+""" """
    execute_query(sql_query)

def checkda():
    with sqlite3.connect('unite') as db:
        cursor = db.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    print(cursor.fetchall())

    
#checkda()
#select_from_table("NASAclimate")
#select_from_table("eff")
