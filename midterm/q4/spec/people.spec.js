let Person = require("../person").Person;
let People = require("../people").People;

describe("person", function () {
    let people = new People("ancestry.json");

    it("read all records", function () {
        expect(people.length).toEqual(10);
    });

    it("hash table", function () {
        expect(people["Clara Aernoudts"]).toEqual(new Person("Clara Aernoudts", 95));
    });
});