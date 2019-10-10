const deep = require("../deepEqual");
const deepEqual = deep.deepEqual;

describe("equal", function () {
    const obj = { here: { is: "an" }, object: 2 };
    it ("self", function () {
        expect(deepEqual(obj, obj)).toBe(true);
    });

    it ("null", function () {
        expect(deepEqual(null, null)).toBe(true);
    });

    it("different", function () {
        expect(deepEqual(obj, { here: 1, object: 2 })).toBe(false);
    });

    it("equvalent", function () {
        expect(deepEqual(obj, { here: { is: "an" }, object: 2 })).toBe(true);
    });
});