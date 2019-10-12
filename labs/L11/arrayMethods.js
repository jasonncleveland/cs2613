function average (array) {
    return array.reduce((a, b) => (a + b), 0) / array.length;
}
console.log(average([1, 2, 3]));

function average2 (array) {
    let sum = 0;
    array.forEach((a) => sum += a);
    return sum / array.length;
}
console.log(average2([1, 2, 3]));