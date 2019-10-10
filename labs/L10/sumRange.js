function range(start, end, step=1) {
    const array = [];
    if (step === 0 || (end < start && step > 0) || (end > start && step < 0)) {
        return array;
    }
    if (step > 0) {
        for (let i = start; i <= end; i += step) {
            array.push(i);
        }
    } else {
        for (let i = start; i >= end; i += step) {
            array.push(i);
        }
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