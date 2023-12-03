var a = document.querySelectorAll(".menu>li>a");
var as = document.querySelectorAll(".hidden>li>a");
console.log(a);
var selectedIndex = localStorage.getItem("selectedMenuItem");

if (selectedIndex !== null) {
  a[selectedIndex].className="current";
}
for (let i = 0; i < a.length; i++) {
    a[i].addEventListener("click", function(event) {
    
        for (let j = 0; j < a.length; j++) {
            a[j].className="";
        }
    
        this.className="current";
        localStorage.setItem("selectedMenuItem", i);
      });
}
for (let i = 0; i < as.length; i++) {
  as[i].addEventListener("click", function(event) {
      localStorage.setItem("selectedMenuItem", 2);
    });
}
//  dateTiem
function displayTime() {
  var date = new Date();
  var hours = date.getHours();
  var minutes = date.getMinutes();
  var seconds = date.getSeconds();
  
  hours = formatTime(hours);
  minutes = formatTime(minutes);
  seconds = formatTime(seconds);
  
  document.getElementById("time").textContent = hours + ":" + minutes + ":" + seconds;
}

function formatTime(time) {
  if (time < 10) {
    return "0" + time;
  }
  return time;
}
setInterval(displayTime, 1000);

// changeColor
function changeBackground(imageUrl) {
  document.body.style.backgroundColor = imageUrl;
}