import sys
sys.path.insert(0, './api')
from index import app

from mangum import Mangum
handler = Mangum(app)
