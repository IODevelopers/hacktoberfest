var digits = [1,2,3,4,5,6,7,8,9];
var searchSum = 100;
 
function concatPrefix(prefix, paths) {
    return paths
        .filter(function(p) { return p.length > 0; })
        .map(function(p) { return prefix.concat(p); });
}
 
function findPaths(sum, previousNumber, index) {
    var previousDigit = Math.abs(previousNumber%10);
    if (index >= digits.length) {
        return sum == previousNumber ? [[previousDigit]] : [];
    }
     
    var currentDigit = digits[index];
    var concatenatedNumber = previousNumber >= 0 ? 10*previousNumber + currentDigit : 10*previousNumber - currentDigit;
  
    var plusPaths = findPaths(sum-previousNumber, currentDigit, index+1);
    var minusPaths = findPaths(sum-previousNumber, -currentDigit, index+1);
    var concatPaths = findPaths(sum, concatenatedNumber, index+1);
     
    var paths = [];
    Array.prototype.push.apply(paths, concatPrefix([previousDigit, '+'], plusPaths));
    Array.prototype.push.apply(paths, concatPrefix([previousDigit, '-'], minusPaths));
    Array.prototype.push.apply(paths, concatPrefix([previousDigit, '&'], concatPaths));
    return paths;
}
 
var foundPaths = findPaths(searchSum, digits[0], 1);
 
if (foundPaths.length == 0) {
    console.log("no paths were found");
} else {
    for (var i = 0; i < foundPaths.length; i++) {
        console.log(foundPaths[i].join("").replace(/&/g, ""));
    }
}
