let read_json_file = require("./read_json_file").read_json_file;

let cache = {};
let data = null;

function by_name(name) {
    if (data == null) {
        data = read_json_file("big.json");
    }
    if (cache[name] != undefined) {
        return cache[name];
    }

    cache[name] = null;
    if (data instanceof Array) {
        data.forEach(person => {
            if (person["name"] === name) {
                cache[name] = person;
            }
        });
    }
    return cache[name];
}

exports.by_name = by_name;
