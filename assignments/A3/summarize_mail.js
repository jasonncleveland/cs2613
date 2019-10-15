const flatten = require("./flatten").flatten;
const read_json_file = require("./read_json_file").read_json_file;

function summarize_mail(filename, ...fields) {
    const data = read_json_file(filename);
    const summarized_mail = [];

    const recursive_search = function (obj) {
        const keys = Object.keys(obj);
        const found_keys = {};
        keys.forEach(key => {
            if (fields.includes(key)) {
                found_keys[key] = obj[key];
            }
            if (typeof obj[key] === "object") {
                Object.assign(found_keys, recursive_search(obj[key]));
            }
        });
        return found_keys;
    };
    
    const flattened_data = flatten(data);
    flattened_data.forEach(element => {
        summarized_mail.push(recursive_search(element));
    });
    return summarized_mail;
}

module.exports.summarize_mail = summarize_mail;

// summarize_mail("example1.json");