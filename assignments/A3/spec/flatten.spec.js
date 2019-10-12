const ms = require("../flatten");

describe("flatten", function () {
    it("base case", function () {
        expect(ms.flatten([])).toEqual([]);
    });

    it("single element", function () {
        expect(ms.flatten([1])).toEqual([1]);
        expect(ms.flatten(["foo"])).toEqual(["foo"]);
        expect(ms.flatten([{ foo: 1 }])).toEqual([{ foo: 1 }]);
    });

    it("longer list, no mutation", function () {
        const data = [[[1], 2, [3]], 4, [5, 6]];
        const orig_data = data;

        expect(ms.flatten(data)).toEqual([1, 2, 3, 4, 5, 6]);
        expect(data).toEqual(orig_data);
    });


    it("deep recursion with objects", function () {
        const data = [[[[1], 2], [{ foo: 3 }]], 4, [5, 6]];
        const orig_data = data;

        expect(ms.flatten(data)).toEqual([1, 2, { foo: 3 }, 4, 5, 6]);
        expect(data).toEqual(orig_data);
    });
});