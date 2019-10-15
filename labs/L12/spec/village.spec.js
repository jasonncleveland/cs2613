const roadGraph = require("../village").roadGraph;

describe("Village tests", function () {
    it("check adjacent to Alice's hous", function () {
        expect(roadGraph["Alice's House"].sort()).toEqual(["Bob's House","Cabin", "Post Office"]);
    });

    it("jasmine objectContaining", function () {
        expect(roadGraph["Alice's House"]).toEqual(jasmine.objectContaining(["Bob's House"]));
    });
});