om flask_mysqldb import MySQL,MySQLdb
import js2py

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Asd-1098#'
app.config['MYSQL_DB'] = 'inter'
mysql = MySQL(app