let btnAddNote = document.getElementById("addNote");
let btnViewNote = document.getElementById("viewNote");
let btnDelNote = document.getElementById("deleteNote");
let actBtn = document.getElementById("actButtons");

btnAddNote.onclick = function(){
    let author = window.prompt("Author ?");
    let title = window.prompt("Title ?");
    let content = window.prompt("Content ?");
    actBtn.innerHTML=`<form action="/addNote" method="POST" name="form"><input name='author' value="${author}" type="hidden"><input name='title' value="${title}" type="hidden"><input name='content' value="${content}" type="hidden"></form>`;
    document.forms["form"].submit();
}

btnViewNote.onclick = function(){
    let idNum = window.prompt("Which ID do you want to view ?");
    actBtn.innerHTML=`<form action="/viewNote" method="GET" name="form"><input name='idNote' value="${idNum}" type="hidden"></form>`
    document.forms["form"].submit();
}

btnDelNote.onclick = function(){
    let idNum = window.prompt("Which ID do you want to delete ?");
    actBtn.innerHTML=`<form action="/delNote" method="POST" name="form"><input name='idNote' value="${idNum}" type="hidden"></form>`
    document.forms["form"].submit();
}