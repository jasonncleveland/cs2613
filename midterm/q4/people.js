let read_json_file = require("./read_json_file").read_json_file;
let Person = require("./person").Person;

class People {
    constructor(filename) {
        let data = read_json_file(filename);
        this.length = data.length;

        data.forEach(person => {
            let age = person["died"] - person["born"] + 1;
            this[person["name"]] = new Person(person["name"], age);
        });
    }
}

module.exports.People = People;
