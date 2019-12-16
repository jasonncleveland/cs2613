let Flight = require("../flight").Flight;

describe("Flights", function () {
    let f01 = new Flight(0, 1);
    let f10 = new Flight(1, 0);
    let f11 = new Flight(1, 1);
    let flights = [f11, f10, f01];

    it ("compare", function () {
        expect(f01.compare(f10)).toBeLessThan(0);
        expect(f01.compare(f01)).toEqual(0);
        expect(f11.compare(f10)).toBeGreaterThan(0);
        expect(f10.compare(f11)).toBeLessThan(0);
    });

    it("sorting", function () {
        expect(
            flights.sort((a,b) => {
                return a.compare(b);
            })
        ).toEqual([f01, f10, f11]);
    });

    it("error handling", function () {
        console.log = jasmine.createSpy("log");
        
        expect(f10.compare(null)).toBeGreaterThan(0);
        expect(console.log).toHaveBeenCalledWith("Invalid Flight given. Valid Flight must contain a cost and time.");
    });
});
