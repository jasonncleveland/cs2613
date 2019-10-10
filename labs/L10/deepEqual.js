function deepEqual(a, b) {
    if (typeof a == "object" && a != null && typeof b == "object" && a != null) {
        if (Object.keys(a).length === Object.keys(b).length) {
            let notEqual = false;
            Object.keys(a).forEach(key => {
                if (b.hasOwnProperty(key)) {
                    notEqual = !deepEqual(a[key], b[key]) || notEqual;
                }
            });
            return !notEqual;
        }
    } else {
        return a === b;
    }
}

module.exports.deepEqual = deepEqual;
