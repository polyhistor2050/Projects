let nr1 = 0;
let nr2 = 1;
let temp;

fibonnaciArray = [];
while (fibonnaciArray.length < 25){
    fibonnaciArray.push(nr1);
    temp = nr1 + nr2;
    nr1 = nr2;
    nr2 = temp;
}
console.log(fibonnaciArray);