let url = 'https://api.sheety.co/5613bff8e32adaf9193ea63a7bdb1140/情報/映画/2';
let body = {
  映画: {
    映画名: 'インディージョーンズ',
    公開年: 2009
  }
}
fetch(url, {
  method: 'PUT',
  body: JSON.stringify(body),
  headers: {
    "Content-Type": "application/json"
  }
})
.then((response) => response.json())
.then(json => {
  // Do something with object
  console.log(json.映画);
});