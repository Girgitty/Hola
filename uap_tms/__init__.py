"""
uap_tms package initializer.

This file installs PyMySQL as a replacement for MySQLdb when PyMySQL
is used as the DB driver on Windows. It is safe to keep this file even
if you use mysqlclient instead.
"""
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except Exception:
    # If pymysql is not installed yet, we silently ignore here; the
    # import will raise later when Django tries to connect if needed.
    pass
