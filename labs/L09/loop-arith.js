function plus(a, b) {
    for (var i = 0; i < a; i++) {
        b++;
    }
    return b;
}

function mult(a, b) {
    var sum = 0;

    for (var i = 0; i < a; i++) {
        sum += b;
    }

    return sum;
}