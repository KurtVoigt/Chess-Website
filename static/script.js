var turn = false;

function move(){
    let from = document.getElementById("fromTextBox").value;
    if( document.getElementById(from).innerHTML === ""){
        return;
    }
    let to = document.getElementById("toTextBox").value;
    document.getElementById(to).innerHTML = document.getElementById(from).innerHTML;
    document.getElementById(from).innerHTML = "";
    //console.log("here");*/
    console.log(document.getElementById(to).value);
};

function reset(){
    document.getElementById("a1").innerHTML = "&#9814";
    document.getElementById("b1").innerHTML = "&#9816";
    document.getElementById("c1").innerHTML = "&#9815";
    document.getElementById("d1").innerHTML = "&#9813";
    document.getElementById("e1").innerHTML = "&#9812";
    document.getElementById("f1").innerHTML = "&#9815";
    document.getElementById("g1").innerHTML = "&#9816";
    document.getElementById("h1").innerHTML = "&#9814";
    let row = document.getElementById("two").children;
    for(let i = 1; i < row.length; i++){
        row[i].innerHTML = "&#9817";
    }
    row = document.getElementById("three").children;
    for(let i = 1; i < row.length; i++){
        row[i].innerHTML = "";
    }
    row = document.getElementById("four").children;
    for(let i = 1; i < row.length; i++){
        row[i].innerHTML = "";
    }
    row = document.getElementById("five").children;
    for(let i = 1; i < row.length; i++){
        row[i].innerHTML = "";
    }
    row = document.getElementById("six").children;
    for(let i = 1; i < row.length; i++){
        row[i].innerHTML = "";
    }
    row = document.getElementById("seven").children;
    for(let i = 1; i < row.length; i++){
        row[i].innerHTML = "&#9823";
    }
    row = document.getElementById("eight").children;
    row[1].innerHTML = "&#9820";
    row[2].innerHTML = "&#9822";
    row[3].innerHTML = "&#9821";
    row[4].innerHTML = "&#9819";
    row[5].innerHTML = "&#9818";
    row[6].innerHTML = "&#9821";
    row[7].innerHTML = "&#9822";
    row[8].innerHTML = "&#9820";
    
};

let moveButton = document.querySelector("#moveButton");//.onclick = move;
moveButton.onclick = move;
let resetButton = document.querySelector("#resetButton");
//resetButton.onclick = reset;
