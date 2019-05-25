import io
import json
from api.sc2_extract import sc2_extract
from http.server import BaseHTTPRequestHandler
from urllib.request import urlopen

class Encoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, bytes):
      try:
        return obj.decode('utf-8')
      except:
        return ''
    return json.JSONEncoder.default(self, obj)

class handler(BaseHTTPRequestHandler):
  def do_GET(self):
    if (self.path[:8] == '/api/gg-'): url = f'http://ggtracker.com/matches/{self.path[8:]}/replay'
    if (self.path[:8] == '/api/rs-'): url = f'http://sc2replaystats.com/download/{self.path[8:]}'
    if (self.path[:8] == '/api/st-'): url = f'http://lotv.spawningtool.com/{self.path[8:]}/download/'
    raw = sc2_extract(io.BytesIO(urlopen(url).read()))
    del raw['gameevents'] # HACK: Need to find a wait around zeit 5m content size limit
    self.send_response(200)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Access-Control-Request-Method', '*')
    self.send_header('Access-Control-Allow-Methods', 'OPTIONS, GET')
    self.send_header('Access-Control-Allow-Headers', '*')
    self.send_header('Cache-Control', 's-maxage=31536000')
    self.send_header('Content-Type', 'application/json')
    self.end_headers()
    self.wfile.write(json.dumps(raw, cls=Encoder, indent=2, sort_keys=True).encode())
    return
