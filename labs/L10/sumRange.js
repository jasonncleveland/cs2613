function range(start, end) {
    const array = [];
    if (end < start) {
        return array;
    }
    for (let i = start; i <= end; i++) {
        array.push(i);
    }
    return array;
}

function sum(array) {
    let total = 0;
    array.forEach(element => {
        total += element;
    });
    return total;
}

module.exports.range = range;
module.exports.sum = sum;