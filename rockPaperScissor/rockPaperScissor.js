const weapons = ["rock", "paper", "scissor"];

let computer = Math.floor(Math.random() * 3);
let player = Math.floor(Math.random() * 3)
let message = "computer selected: " + weapons[computer] + " Vs player selected: " + weapons[player];
let results;

if(computer === player){
    results = "It's a tie";
}else if(player > computer){
    if(computer == 0 && player == 2){
        results = "computer wins";
    }else {
        results = "player wins";
    }
}else {
    if(computer == 2 && player == 0){
        results = "player wins";
    }else {
        results = "computer wins";
    }
}
console.log(message);
console.log(results);



