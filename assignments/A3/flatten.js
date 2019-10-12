function flatten(array) {
    return array.reduce((reduced, element) => {
        if (element instanceof Array) {
            return reduced.concat(flatten(element));
        } else {
            return reduced.concat(element);
        }
    }, []);
}

module.exports.flatten = flatten;
