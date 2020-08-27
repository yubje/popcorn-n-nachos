import json
files = []

with open('./movies5.json') as json_file:
  json_data = json.load(json_file)
  for x in json_data["results"]:
    pk = x["id"]
    genres = x["genre_ids"]
    del(x["video"], x["id"], x["genre_ids"])
    x["genres"] = genres
    tmp = {"model":"movies.movie", "pk":pk, "fields": x}
    # print(tmp)
    # print('-------------')
    files.append(tmp)

with open('./newmovies5.json', 'w') as outfile:
  json.dump(files, outfile)
