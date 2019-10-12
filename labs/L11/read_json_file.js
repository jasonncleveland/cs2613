let fs = require("fs");

function read_json_file(filename) {
    let contents = fs.readFileSync(filename);

    return JSON.parse(contents);
}

exports.read_json_file = read_json_file;