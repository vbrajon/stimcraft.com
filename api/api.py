import io
import json
from api.sc2_extract import sc2_extract
from http.server import BaseHTTPRequestHandler
from urllib.error import HTTPError
from urllib.parse import urlsplit
from urllib.request import urlopen

class Encoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, bytes):
      try:
        return obj.decode('utf-8')
      except UnicodeDecodeError:
        return ''
    return json.JSONEncoder.default(self, obj)

# GET /api/st-<id> decodes the Spawning Tool replay <id>
class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    id = urlsplit(self.path).path.removeprefix('/api/st-')
    if not id.isdigit():
      return self.send_error(404)
    try:
      replay = urlopen(f'https://lotv.spawningtool.com/{id}/download/').read()
    except HTTPError as error:
      return self.send_error(error.code)
    body = json.dumps(sc2_extract(io.BytesIO(replay)), cls=Encoder, sort_keys=True).encode()
    self.send_response(200)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Access-Control-Allow-Methods', 'OPTIONS, GET')
    self.send_header('Access-Control-Allow-Headers', '*')
    self.send_header('Cache-Control', 's-maxage=31536000')
    self.send_header('Content-Type', 'application/json')
    self.end_headers()
    self.wfile.write(body)
