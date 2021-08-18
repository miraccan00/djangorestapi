function submitLoginForm(event){
    event.preventDefault();
    var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
"name":event.target['InputName'].value,
"videoname": event.target['InputVideoName'].value,
"videourl": event.target['InputVideoUrl'].value
});

var requestOptions = {
method: 'POST',
headers: myHeaders,
body: raw,
redirect: 'follow'
};

fetch("http://127.0.0.1:8000/api/coursecontent/", requestOptions)
.then(response => response.text())
.then(result => console.log(result))
.catch(error => console.log('error', error));
document.getElementById("name").value = "";
document.getElementById("videoname").value = "";
document.getElementById("videourl").value = "";
}


// var requestOptions = {
//   method: 'GET',
//   redirect: 'follow'
// }
// const courseContent = fetch("http://127.0.0.1:8000/api/coursecontent/", requestOptions)
// .then(response =>  response.json())
// .then((result) => {result.forEach(element =>document.getElementById("demo").innerHTML = document.getElementById("demo").innerHTML + element.name+" <br>");})
// .catch(error => console.log('error', error));

