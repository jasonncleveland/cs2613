let read_json_file = require("./read_json_file").read_json_file;

let data = null;

function by_name(name) {
    if (data == null) {
        data = read_json_file("ancestry.json");
    }

    // simple linear scan
    let result = null;
    if (data instanceof Array) {
        data.forEach(person => {
            if (person["name"] === name) {
                result = person;
            }
        });
    }
    return result;
}

exports.by_name = by_name;
