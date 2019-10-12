let read_json_file = require("./read_json_file").read_json_file;

let data = read_json_file("ancestry.json");
// let data = read_json_file("big.json");

let names = [];

for (let i = 0; i < data.length; i++) {
    names.push(data[i].name);
}

exports.names = names;
