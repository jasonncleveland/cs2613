function flatten(array) {
    let reduced = array.reduce((reduced, element) => reduced.concat(element), []);
    return reduced;
}

module.exports.flatten = flatten;