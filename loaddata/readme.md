# readme

1. api 를 db에 저장하기

네이버 영화 -> api key를 uri에 쓸 수 없어서 어려웠음 

curl 사용해서 저장학

fixtures 사용하기 

```
curl https:aaa.com > movies.json
```



python으로 json 파일 가공하기

```python
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

    files.append(tmp)

with open('./newmovies5.json', 'w') as outfile:
  json.dump(files, outfile)

```



```
dumpdata
loaddata
```

https://twpower.github.io/20-how-to-use-fixture-in-django



2. model 정의

user와 movies를 manytomanyfield로 연결하는데, 이 때 rate 정보를 어떻게 새로운 column으로 저장할건지

https://brunch.co.kr/@ddangdol/6

through 를 사용해서 model에 새로운 class를 임의로 정의한다. 





## vue

router link으로 데이터 보내기 

```js
 {
    path: '/movies/detail',
    name: 'MovieDetailView',
    component: MovieDetailView,
    props(route){
      return { movie_id: route.query.movie_id }
    },
  },
```



```html
<router-link :to="{ name: 'MovieDetailView', query: {movie_id : movie.id} }" >
  <button type="button" class="btn btn-warning">
   	영화 정보 상세보기 
  </button>
</router-link>
```

https://stackoverflow.com/questions/51244708/vue-cli-passing-props-data-through-router-link



### comment create 후 페이지 새로고침 

```js
methods: {
    createComment() {
      // 토큰 정보 가져오기(?)
      // console.log(this.article_id)
      const requestHeader = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.commentData.movie = this.movie_id
      // url, body, header
      axios.post(`${SERVER_URL}/articles/${this.article_id}/comments_create/`, this.commentData, requestHeader)
        // 글작성 완료했다면 목록으로 이동
        .then(() => this.$router.go())
        .catch(error => console.log(error.response.data))
    },
  },
```

페이지를 새로고침하는 경우 `this.$router.go()` 를 쓰면 현재 페이지로 다시 라우팅된다.

```vue
this.$router.push({ name: 'MovieDetailView', query: {movie_id : movie.id}})
```

다음과 같이 하면 현재 페이지로 reload가 되지 않아 에러가 발생한다.