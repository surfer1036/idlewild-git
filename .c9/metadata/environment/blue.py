{"changed":true,"filter":false,"title":"blue.py","tooltip":"/blue.py","value":"import random, requests, json\n#import requests_oauthlib\nimport flask\nimport os\n\n\napp = flask.Flask(__name__)\n\n\napi_token = '3yEHJrYc03grMh7SUZsRlZKDlQv-3NK0EyJ3iZQquV69HlpaCU9p28OoUejFOLu5'\n\nurl = \"https://api.genius.com/search?q=Outkast\"\n\nmy_headers = {\n    \"Authorization\": \"Bearer qiICws1IclXFRZmTwrTJI7k4m8vWoOwy2smTaAmQ2RuyiWztfrPPijT9ea2i2nA-\"\n}\n\nresponse = requests.get(url, headers=my_headers)\njson_body = response.json()\n\n\n\n@app.route(\"/\")  \ndef index(): \n    r = random.randint(1, 20)\n    photo = json_body[\"response\"][\"hits\"][r][\"result\"][\"song_art_image_url\"]\n    title = json_body[\"response\"][\"hits\"][r][\"result\"][\"full_title\"]\n    artist = json_body[\"response\"][\"hits\"][r][\"result\"][\"image_url\"]\n    return flask.render_template(\n       \"index.html\",\n        album_src=photo, title_src=title, artist_src=artist) \n   \n        \n#    title = json_body[\"response\"][\"hits\"][0][\"result\"][\"full_title\"]\n#    return flask.render_template(\n#        \"index.html\",\n#        title_src=title)\n    \n\n\napp.run(\n    port=int(os.getenv('PORT', 8080)),\n    host=os.getenv('IP', '0.0.0.0')\n)\n\n\n\n\n\"\"\" \nurl = \"https://api.twitter.com/1.1/account/verify_credentials.json\"\noauth = requests_oauthlib.OAuth1(\n    \"C7naPh6NBJhMYBX1JMAnLX67d\", \n    \"AkZqf5Dq6cnVlpVfMYDuGTaA3y0SLOxjGcS98swGs94ItLH1EL\",\n    \"3846948017-Vsqn57lvX9zmjtslCoA0gENtbs3jJP21OkyPvYQ\",\n    \"EVunEKabWXO69Kqi6uqkgIhxgUkzSwWayk1JsT9y77R1G\"\n)\n\n\n\nresponse = requests.get(url, auth=oauth)\n\n#print(response.json())\n\n\"\"\"\n","undoManager":{"mark":97,"position":100,"stack":[[{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "],"id":500}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"insert","lines":["#"],"id":501}],[{"start":{"row":31,"column":1},"end":{"row":31,"column":2},"action":"insert","lines":["#"],"id":502}],[{"start":{"row":32,"column":1},"end":{"row":32,"column":2},"action":"insert","lines":["#"],"id":503}],[{"start":{"row":32,"column":0},"end":{"row":32,"column":1},"action":"remove","lines":[" "],"id":504}],[{"start":{"row":31,"column":0},"end":{"row":31,"column":1},"action":"remove","lines":[" "],"id":505}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":1},"action":"remove","lines":["#"],"id":506}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"remove","lines":["#"],"id":507}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"insert","lines":["#"],"id":508}],[{"start":{"row":29,"column":1},"end":{"row":29,"column":2},"action":"insert","lines":["#"],"id":509}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":1},"action":"remove","lines":[" "],"id":510}],[{"start":{"row":50,"column":0},"end":{"row":51,"column":0},"action":"remove","lines":["",""],"id":511},{"start":{"row":49,"column":0},"end":{"row":50,"column":0},"action":"remove","lines":["",""]},{"start":{"row":48,"column":0},"end":{"row":49,"column":0},"action":"remove","lines":["",""]},{"start":{"row":47,"column":0},"end":{"row":48,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":35,"column":0},"end":{"row":35,"column":1},"action":"insert","lines":["#"],"id":512}],[{"start":{"row":36,"column":0},"end":{"row":36,"column":1},"action":"insert","lines":["#"],"id":513}],[{"start":{"row":37,"column":0},"end":{"row":37,"column":1},"action":"insert","lines":["#"],"id":514}],[{"start":{"row":38,"column":0},"end":{"row":38,"column":1},"action":"insert","lines":["#"],"id":515}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":1},"action":"remove","lines":["#"],"id":516}],[{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"remove","lines":["#"],"id":517}],[{"start":{"row":31,"column":0},"end":{"row":31,"column":1},"action":"remove","lines":["#"],"id":518}],[{"start":{"row":32,"column":0},"end":{"row":32,"column":1},"action":"remove","lines":["#"],"id":519}],[{"start":{"row":29,"column":2},"end":{"row":29,"column":3},"action":"remove","lines":[" "],"id":520},{"start":{"row":29,"column":1},"end":{"row":29,"column":2},"action":"remove","lines":[" "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":1},"action":"remove","lines":[" "]},{"start":{"row":28,"column":3},"end":{"row":29,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":28,"column":3},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":521},{"start":{"row":29,"column":0},"end":{"row":29,"column":3},"action":"insert","lines":["   "]}],[{"start":{"row":29,"column":2},"end":{"row":29,"column":3},"action":"remove","lines":[" "],"id":522},{"start":{"row":29,"column":1},"end":{"row":29,"column":2},"action":"remove","lines":[" "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":1},"action":"remove","lines":[" "]},{"start":{"row":28,"column":3},"end":{"row":29,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"remove","lines":["    "],"id":523}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "],"id":524}],[{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"remove","lines":["    "],"id":525},{"start":{"row":28,"column":96},"end":{"row":29,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":28,"column":96},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":526},{"start":{"row":29,"column":0},"end":{"row":29,"column":3},"action":"insert","lines":["   "]}],[{"start":{"row":31,"column":7},"end":{"row":31,"column":8},"action":"insert","lines":[" "],"id":527}],[{"start":{"row":28,"column":61},"end":{"row":28,"column":62},"action":"remove","lines":["0"],"id":528},{"start":{"row":28,"column":60},"end":{"row":28,"column":61},"action":"remove","lines":["0"]},{"start":{"row":28,"column":59},"end":{"row":28,"column":60},"action":"remove","lines":["1"]}],[{"start":{"row":28,"column":59},"end":{"row":28,"column":60},"action":"insert","lines":["8"],"id":529}],[{"start":{"row":28,"column":59},"end":{"row":28,"column":60},"action":"remove","lines":["8"],"id":530}],[{"start":{"row":28,"column":59},"end":{"row":28,"column":60},"action":"insert","lines":["3"],"id":531}],[{"start":{"row":28,"column":59},"end":{"row":28,"column":60},"action":"remove","lines":["3"],"id":532}],[{"start":{"row":28,"column":59},"end":{"row":28,"column":60},"action":"insert","lines":["2"],"id":533},{"start":{"row":28,"column":60},"end":{"row":28,"column":61},"action":"insert","lines":["0"]}],[{"start":{"row":28,"column":95},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":534},{"start":{"row":29,"column":0},"end":{"row":29,"column":3},"action":"insert","lines":["   "]}],[{"start":{"row":29,"column":3},"end":{"row":29,"column":67},"action":"insert","lines":["title = json_body[\"response\"][\"hits\"][0][\"result\"][\"full_title\"]"],"id":535}],[{"start":{"row":29,"column":41},"end":{"row":29,"column":42},"action":"remove","lines":["0"],"id":536}],[{"start":{"row":29,"column":41},"end":{"row":29,"column":42},"action":"insert","lines":["1"],"id":537},{"start":{"row":29,"column":42},"end":{"row":29,"column":43},"action":"insert","lines":[","]},{"start":{"row":29,"column":43},"end":{"row":29,"column":44},"action":"insert","lines":["2"]},{"start":{"row":29,"column":44},"end":{"row":29,"column":45},"action":"insert","lines":["0"]}],[{"start":{"row":29,"column":43},"end":{"row":29,"column":44},"action":"insert","lines":[" "],"id":538}],[{"start":{"row":28,"column":59},"end":{"row":28,"column":60},"action":"remove","lines":["2"],"id":539}],[{"start":{"row":28,"column":59},"end":{"row":28,"column":60},"action":"insert","lines":["3"],"id":540}],[{"start":{"row":29,"column":45},"end":{"row":29,"column":46},"action":"insert","lines":["3"],"id":541}],[{"start":{"row":29,"column":45},"end":{"row":29,"column":46},"action":"remove","lines":["3"],"id":542},{"start":{"row":29,"column":44},"end":{"row":29,"column":45},"action":"remove","lines":["2"]}],[{"start":{"row":29,"column":44},"end":{"row":29,"column":45},"action":"insert","lines":["3"],"id":543}],[{"start":{"row":32,"column":23},"end":{"row":33,"column":0},"action":"insert","lines":["",""],"id":544},{"start":{"row":33,"column":0},"end":{"row":33,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":33,"column":8},"end":{"row":33,"column":23},"action":"insert","lines":["title_src=title"],"id":545}],[{"start":{"row":33,"column":4},"end":{"row":33,"column":8},"action":"remove","lines":["    "],"id":546},{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"remove","lines":["    "]},{"start":{"row":32,"column":23},"end":{"row":33,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":32,"column":23},"end":{"row":32,"column":24},"action":"insert","lines":[","],"id":547}],[{"start":{"row":32,"column":24},"end":{"row":32,"column":25},"action":"insert","lines":[" "],"id":548}],[{"start":{"row":27,"column":13},"end":{"row":27,"column":14},"action":"remove","lines":[" "],"id":549},{"start":{"row":27,"column":13},"end":{"row":28,"column":0},"action":"insert","lines":["",""]},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"remove","lines":["    "],"id":550}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "],"id":551}],[{"start":{"row":28,"column":4},"end":{"row":28,"column":5},"action":"insert","lines":["r"],"id":552}],[{"start":{"row":28,"column":5},"end":{"row":28,"column":6},"action":"insert","lines":[" "],"id":553},{"start":{"row":28,"column":6},"end":{"row":28,"column":7},"action":"insert","lines":["-"]}],[{"start":{"row":28,"column":6},"end":{"row":28,"column":7},"action":"remove","lines":["-"],"id":554}],[{"start":{"row":28,"column":6},"end":{"row":28,"column":7},"action":"insert","lines":["="],"id":555}],[{"start":{"row":28,"column":7},"end":{"row":28,"column":8},"action":"insert","lines":[" "],"id":556}],[{"start":{"row":28,"column":7},"end":{"row":28,"column":8},"action":"remove","lines":[" "],"id":557},{"start":{"row":28,"column":6},"end":{"row":28,"column":7},"action":"remove","lines":["="]},{"start":{"row":28,"column":5},"end":{"row":28,"column":6},"action":"remove","lines":[" "]},{"start":{"row":28,"column":4},"end":{"row":28,"column":5},"action":"remove","lines":["r"]},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "],"id":558}],[{"start":{"row":28,"column":4},"end":{"row":28,"column":30},"action":"insert","lines":["r = random.randint(1, 100)"],"id":559}],[{"start":{"row":29,"column":41},"end":{"row":29,"column":62},"action":"remove","lines":["random.randint(1, 30)"],"id":560},{"start":{"row":29,"column":41},"end":{"row":29,"column":42},"action":"insert","lines":["r"]}],[{"start":{"row":30,"column":41},"end":{"row":30,"column":46},"action":"remove","lines":["1, 30"],"id":561},{"start":{"row":30,"column":41},"end":{"row":30,"column":42},"action":"insert","lines":["r"]}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"remove","lines":["    "],"id":562},{"start":{"row":27,"column":13},"end":{"row":28,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":27,"column":13},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":563},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":29,"column":2},"end":{"row":29,"column":3},"action":"remove","lines":[" "],"id":564},{"start":{"row":29,"column":1},"end":{"row":29,"column":2},"action":"remove","lines":[" "]},{"start":{"row":29,"column":0},"end":{"row":29,"column":1},"action":"remove","lines":[" "]},{"start":{"row":28,"column":30},"end":{"row":29,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":28,"column":30},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":565},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":30,"column":2},"end":{"row":30,"column":3},"action":"remove","lines":[" "],"id":566},{"start":{"row":30,"column":1},"end":{"row":30,"column":2},"action":"remove","lines":[" "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":1},"action":"remove","lines":[" "]},{"start":{"row":29,"column":76},"end":{"row":30,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":29,"column":76},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":567},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":31,"column":2},"end":{"row":31,"column":3},"action":"remove","lines":[" "],"id":568},{"start":{"row":31,"column":1},"end":{"row":31,"column":2},"action":"remove","lines":[" "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":1},"action":"remove","lines":[" "]},{"start":{"row":30,"column":68},"end":{"row":31,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":30,"column":68},"end":{"row":31,"column":0},"action":"insert","lines":["",""],"id":569},{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":28,"column":28},"end":{"row":28,"column":29},"action":"remove","lines":["0"],"id":570},{"start":{"row":28,"column":27},"end":{"row":28,"column":28},"action":"remove","lines":["0"]},{"start":{"row":28,"column":26},"end":{"row":28,"column":27},"action":"remove","lines":["1"]}],[{"start":{"row":28,"column":26},"end":{"row":28,"column":27},"action":"insert","lines":["3"],"id":571}],[{"start":{"row":28,"column":26},"end":{"row":28,"column":27},"action":"remove","lines":["3"],"id":572}],[{"start":{"row":28,"column":26},"end":{"row":28,"column":27},"action":"insert","lines":["2"],"id":573},{"start":{"row":28,"column":27},"end":{"row":28,"column":28},"action":"insert","lines":["0"]}],[{"start":{"row":21,"column":0},"end":{"row":23,"column":63},"action":"remove","lines":["#print(json_body[\"response\"][\"hits\"][0][\"type\"])","#print(json_body[\"response\"][\"hits\"][random.randint(1, 100)][\"result\"][\"song_art_image_url\"])","#print(json_body[\"response\"][\"hits\"][0][\"result\"][\"full_title\"]"],"id":575}],[{"start":{"row":28,"column":68},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":576},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]},{"start":{"row":29,"column":4},"end":{"row":29,"column":5},"action":"insert","lines":["a"]},{"start":{"row":29,"column":5},"end":{"row":29,"column":6},"action":"insert","lines":["r"]},{"start":{"row":29,"column":6},"end":{"row":29,"column":7},"action":"insert","lines":["t"]},{"start":{"row":29,"column":7},"end":{"row":29,"column":8},"action":"insert","lines":["i"]},{"start":{"row":29,"column":8},"end":{"row":29,"column":9},"action":"insert","lines":["s"]},{"start":{"row":29,"column":9},"end":{"row":29,"column":10},"action":"insert","lines":["t"]}],[{"start":{"row":29,"column":10},"end":{"row":29,"column":11},"action":"insert","lines":[" "],"id":577}],[{"start":{"row":29,"column":10},"end":{"row":29,"column":11},"action":"remove","lines":[" "],"id":578}],[{"start":{"row":29,"column":10},"end":{"row":29,"column":11},"action":"insert","lines":[" "],"id":579},{"start":{"row":29,"column":11},"end":{"row":29,"column":12},"action":"insert","lines":["="]}],[{"start":{"row":29,"column":12},"end":{"row":29,"column":13},"action":"insert","lines":[" "],"id":580}],[{"start":{"row":29,"column":13},"end":{"row":29,"column":69},"action":"insert","lines":["json_body[\"response\"][\"hits\"][r][\"result\"][\"full_title\"]"],"id":581}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["# app.py",""],"id":582}],[{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""],"id":583}],[{"start":{"row":27,"column":57},"end":{"row":27,"column":67},"action":"remove","lines":["full_title"],"id":584},{"start":{"row":27,"column":57},"end":{"row":27,"column":58},"action":"insert","lines":["i"]},{"start":{"row":27,"column":58},"end":{"row":27,"column":59},"action":"insert","lines":["m"]},{"start":{"row":27,"column":59},"end":{"row":27,"column":60},"action":"insert","lines":["a"]},{"start":{"row":27,"column":60},"end":{"row":27,"column":61},"action":"insert","lines":["g"]},{"start":{"row":27,"column":61},"end":{"row":27,"column":62},"action":"insert","lines":["e"]},{"start":{"row":27,"column":62},"end":{"row":27,"column":63},"action":"insert","lines":["_"]}],[{"start":{"row":27,"column":63},"end":{"row":27,"column":64},"action":"insert","lines":["i"],"id":585}],[{"start":{"row":27,"column":63},"end":{"row":27,"column":64},"action":"remove","lines":["i"],"id":586}],[{"start":{"row":27,"column":63},"end":{"row":27,"column":64},"action":"insert","lines":["u"],"id":587},{"start":{"row":27,"column":64},"end":{"row":27,"column":65},"action":"insert","lines":["r"]},{"start":{"row":27,"column":65},"end":{"row":27,"column":66},"action":"insert","lines":["k"]}],[{"start":{"row":27,"column":65},"end":{"row":27,"column":66},"action":"remove","lines":["k"],"id":588}],[{"start":{"row":27,"column":65},"end":{"row":27,"column":66},"action":"insert","lines":["l"],"id":589}],[{"start":{"row":30,"column":40},"end":{"row":30,"column":41},"action":"insert","lines":[","],"id":590}],[{"start":{"row":30,"column":41},"end":{"row":30,"column":42},"action":"insert","lines":[" "],"id":591}],[{"start":{"row":30,"column":42},"end":{"row":30,"column":43},"action":"insert","lines":["a"],"id":592},{"start":{"row":30,"column":43},"end":{"row":30,"column":44},"action":"insert","lines":["r"]},{"start":{"row":30,"column":44},"end":{"row":30,"column":45},"action":"insert","lines":["t"]}],[{"start":{"row":30,"column":45},"end":{"row":30,"column":46},"action":"insert","lines":["i"],"id":593},{"start":{"row":30,"column":46},"end":{"row":30,"column":47},"action":"insert","lines":["s"]},{"start":{"row":30,"column":47},"end":{"row":30,"column":48},"action":"insert","lines":["t"]}],[{"start":{"row":30,"column":48},"end":{"row":30,"column":49},"action":"insert","lines":["_"],"id":594},{"start":{"row":30,"column":49},"end":{"row":30,"column":50},"action":"insert","lines":["s"]},{"start":{"row":30,"column":50},"end":{"row":30,"column":51},"action":"insert","lines":["r"]},{"start":{"row":30,"column":51},"end":{"row":30,"column":52},"action":"insert","lines":["c"]}],[{"start":{"row":30,"column":52},"end":{"row":30,"column":53},"action":"insert","lines":["="],"id":595}],[{"start":{"row":30,"column":53},"end":{"row":30,"column":54},"action":"insert","lines":["a"],"id":596},{"start":{"row":30,"column":54},"end":{"row":30,"column":55},"action":"insert","lines":["r"]},{"start":{"row":30,"column":55},"end":{"row":30,"column":56},"action":"insert","lines":["t"]},{"start":{"row":30,"column":56},"end":{"row":30,"column":57},"action":"insert","lines":["o"]},{"start":{"row":30,"column":57},"end":{"row":30,"column":58},"action":"insert","lines":["s"]}],[{"start":{"row":30,"column":57},"end":{"row":30,"column":58},"action":"remove","lines":["s"],"id":597},{"start":{"row":30,"column":56},"end":{"row":30,"column":57},"action":"remove","lines":["o"]},{"start":{"row":30,"column":55},"end":{"row":30,"column":56},"action":"remove","lines":["t"]}],[{"start":{"row":30,"column":55},"end":{"row":30,"column":56},"action":"insert","lines":["t"],"id":598},{"start":{"row":30,"column":56},"end":{"row":30,"column":57},"action":"insert","lines":["i"]},{"start":{"row":30,"column":57},"end":{"row":30,"column":58},"action":"insert","lines":["s"]},{"start":{"row":30,"column":58},"end":{"row":30,"column":59},"action":"insert","lines":["t"]}],[{"start":{"row":30,"column":59},"end":{"row":30,"column":60},"action":"insert","lines":["g"],"id":599},{"start":{"row":30,"column":60},"end":{"row":30,"column":61},"action":"insert","lines":["i"]},{"start":{"row":30,"column":61},"end":{"row":30,"column":62},"action":"insert","lines":["t"]}],[{"start":{"row":30,"column":62},"end":{"row":30,"column":63},"action":"insert","lines":[" "],"id":600}],[{"start":{"row":30,"column":62},"end":{"row":30,"column":63},"action":"remove","lines":[" "],"id":601},{"start":{"row":30,"column":61},"end":{"row":30,"column":62},"action":"remove","lines":["t"]},{"start":{"row":30,"column":60},"end":{"row":30,"column":61},"action":"remove","lines":["i"]},{"start":{"row":30,"column":59},"end":{"row":30,"column":60},"action":"remove","lines":["g"]}]]},"ace":{"folds":[],"scrolltop":435,"scrollleft":0,"selection":{"start":{"row":30,"column":59},"end":{"row":30,"column":59},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":2,"state":"start","mode":"ace/mode/python"}},"timestamp":1567646573529}