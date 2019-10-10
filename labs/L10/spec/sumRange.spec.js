const array = require("../sumRange");

describe("range", function () {
    it("empty", function () {
        expect(array.range(2, 1)).toEqual([]);
    });

    it("single", function () {
        expect(array.range(2, 2)).toEqual([2]);
    });

    it("multiple", function () {
        expect(array.range(42, 50)).toEqual([42, 43, 44, 45, 46, 47, 48, 49, 50]);
    });

    it("step 2", function () {
        expect(array.range(1, 10, 2)).toEqual([1, 3, 5, 7, 9]);
    });

    it("step -1", function () {
        expect(array.range(5, 2, -1)).toEqual([5, 4, 3, 2]);
    });
});

describe("sum", function () {
    it("empty", function () {
        expect(array.sum([])).toBe(0);
    });

    it("single", function () {
        expect(array.sum([2])).toBe(2);
    });

    it("multiple", function () {
        expect(array.sum(array.range(1, 10))).toBe(55);
    });
});