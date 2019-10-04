var arith = require("../loop-arith.js");
var arithRecursive = require("../loop-arith-recursive");

describe("add",
    function() {
        it("1 + 1 = 2", function() {
            expect(arith.plus(1, 1)).toBe(arithRecursive.plus(1, 1));
        });

        it("4 + 6 = 10", function() {
            expect(arith.plus(4, 6)).toBe(arithRecursive.plus(4, 6));
        });
    }
);

describe("mult",
    function() {
        it("0 * 2 = 0", function() {
            expect(arith.mult(0, 2)).toBe(arithRecursive.mult(0, 2));
        });

        it("1 * 2 = 2", function() {
            expect(arith.mult(1, 2)).toBe(arithRecursive.mult(1, 2));
        });

        it("2 * 2 = 4", function() {
            expect(arith.mult(2, 2)).toBe(arithRecursive.mult(2, 2));
        });
    }
);