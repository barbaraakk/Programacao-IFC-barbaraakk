from config import *
from rota import *

with app.app_context():
     db.create_all()
     CORS(app)
     app.run(debug=True)