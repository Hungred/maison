// Empty JS for your own code to be here


var date = new Date();

var nowMonth = date.getMonth() + 1;

var strDate = date.getDate();

var seperator = "-";

if (nowMonth >= 1 && nowMonth <= 9) {
   nowMonth = "0" + nowMonth;
}

if (strDate >= 0 && strDate <= 9) {
   strDate = "0" + strDate;
}

var nowDate = date.getFullYear() + seperator + nowMonth + seperator + strDate;

function openForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
}