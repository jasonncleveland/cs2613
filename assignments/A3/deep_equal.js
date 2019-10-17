function deep_equal(a, b) {
    if (typeof a == "object" && a != null && typeof b == "object" && a != null) {
        if (Object.keys(a).length === Object.keys(b).length) {
            let notEqual = false;
            Object.keys(a).forEach(key => {
                if (b.hasOwnProperty(key)) {
                    notEqual = !deep_equal(a[key], b[key]) || notEqual;
                }
            });
            return !notEqual;
        }
    } else {
        return a === b;
    }
}

module.exports.deep_equal = deep_equal;