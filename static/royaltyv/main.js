function sidebarAction(){
  var sidebar = document.getElementById("mySidenav");
  var canvas = document.getElementById("main");

  if (sidebar.style.width != "90px"){
    sidebar.style.width = "90px";
    canvas.style.marginLeft = "90px";
  }

  else{
    sidebar.style.width = "0";
    canvas.style.marginLeft = "0";
  }
}

function animateMenuIcon(x){
  x.classList.toggle("change");
}