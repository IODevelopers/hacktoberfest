var numbers = [1,2,3,4,5,6,7,8,9];
var sum = 100;
var signs = ['+', '-', '&'];
var numbersInnerLength = numbers.length-1;
var cLength = Math.pow(signs.length, numbersInnerLength);
var combinations = [];
 
for (var i = 0; i < cLength; i++) {
    var newArray = [];
    for (var j = 0; j < numbers.length; j++) {
        newArray[j*2] = numbers[j];
    }
    combinations.push(newArray);
     
}
 
for (var k = 0; k < numbersInnerLength; k++) {
    var periodLength = cLength / Math.pow(signs.length, k+1);
    var signIndex = 0;
    for (var i = 0; i < cLength; i+=periodLength) {
        for (var j = 0; j < periodLength && i+j < cLength; j++) {
            combinations[i+j][k*2+1] = signs[signIndex];
        }
        signIndex = (signIndex+1)%signs.length;
    }
}
 
for (var i = 0; i < combinations.length; i++) {
    var combination = combinations[i];
    var cstr = combination.join("").replace(/&/g, "");
    if (eval(cstr) == sum) {
        console.log(cstr);
    }
}
