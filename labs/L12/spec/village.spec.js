const village = require("../village");
const roadGraph = village.roadGraph;
const VillageState = village.VillageState;
const runRobot = village.runRobot;
const randomRobot = village.randomRobot;

describe("Village tests", function () {
    it("check adjacent to Alice's hous", function () {
        expect(roadGraph["Alice's House"].sort()).toEqual(["Bob's House","Cabin", "Post Office"]);
    });

    it("jasmine objectContaining", function () {
        expect(roadGraph["Alice's House"]).toEqual(jasmine.objectContaining(["Bob's House"]));
    });
});

describe("valid tests", function () {
    let first = new VillageState(
        "Post Office",
        [{ place: "Post Office", address: "Alice's House" }]
    );
    let next = first.move("Alice's House");

    it("move changes place", function () {
        expect(next.place).toEqual("Alice's House");
    });

    it("parcel is delivered", function () {
        expect(next.parcels).toEqual([]);
    });

    it("move does not modify", function () {
        expect(first.place).toEqual("Post Office");
    });
});

describe("invalid address tests", function () {
    let first = new VillageState(
        "Post Office",
        [{ place: "Post Office", address: "Alice's House" }]
    );
    let next = first.move("Town Hall");

    it("move does not change place", function () {
        expect(next.place).toEqual("Post Office");
    });

    it("parcel is not delivered", function () {
        expect(next.parcels).toEqual([{ place: "Post Office", address: "Alice's House" }]);
    });
});

describe("invalid parcel tests", function () {
    let first = new VillageState(
        "Post Office",
        [{ place: "Bob's House", address: "Alice's House" }]
    );
    let next = first.move("Alice's House");

    it("parcel can't be delivered", function () {
        expect(next.parcels).toEqual([{ place: "Bob's House", address: "Alice's House" }]);
    });
});

describe("runRobot", function () {
    it("no parcels", function () {
        console.log = jasmine.createSpy("log");
        let noParcels = new VillageState("Post Office", []);
        runRobot(noParcels);

        expect(console.log).toHaveBeenCalledWith("Done in 0 turns");
    });

    it("randomRobot", function () {
        console.log = jasmine.createSpy("log");
        runRobot(VillageState.random(), randomRobot);

        expect(console.log).toHaveBeenCalledWith(jasmine.stringMatching(/^Done/));
    });
});
