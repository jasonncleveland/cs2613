let flatten = require("../flatten").flatten;

describe("flatten", function () {
    it("base case", function () {
        expect(flatten([])).toEqual([]);
    });

    it("single element", function () {
        expect(flatten([1])).toEqual([1]);
        expect(flatten(["foo"])).toEqual(["foo"]);
        expect(flatten([{ foo: 1 }])).toEqual([{ foo: 1}]);
    });

    it("longer list, no mutation", function () {
        let data = [[1], 2, [3], 4, [5, 6]];
        let orig_data = data;

        expect(flatten(data)).toEqual([1, 2, 3, 4, 5, 6]);
        expect(data).toEqual(orig_data);
    });

    xit("deeper nesting", function () {
        let data = [[[1], 2, [3]], 4, [5, 6]];
        let orig_data = data;

        expect(flatten(data)).toEqual([1, 2, 3, 4, 5, 6]);
        expect(data).toEqual(data);
    })
});