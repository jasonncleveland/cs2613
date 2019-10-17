let village = require("../village.js");
let VillageState = village.VillageState;

describe("roadGraph",
    function () {
        let roadGraph = village.roadGraph;

        it("Alice's House",
            function () {
                expect(roadGraph["Alice's House"]).toEqual(["Bob's House", "Cabin", "Post Office"]);
            });

        it("Bob's House",
            function () {
                expect(roadGraph["Bob's House"]).toEqual(jasmine.objectContaining(["Alice's House"]));
            });
    });


describe("VillageState",
    function () {
        let first = new VillageState(
            "Post Office",
            [{ place: "Post Office", address: "Alice's House" }, { place: "Mars", destination: "Jupiter" }]
        );

        let next = first.move("Alice's House");

        it("move changes place",
            function () {
                expect(next.place).toEqual("Alice's House");
            });

        it("move changes parcels",
            function () {
                expect(next.parcels).toEqual([{ place: "Mars", destination: "Jupiter" }]);
            });

        it("immutability",
            function () {
                expect(first.place).toEqual("Post Office");
            });

        it("invalid destination",
            function () {
                expect(first.move("Mars")).toBe(first);
            });

        it("toString first",
            function () {
                expect(first.toString()).toEqual(
                    [
                        "---------",
                        "| |2| |c|",
                        "---------",
                        "|f|m|a| |",
                        "---------",
                        "|g|s|t|b|",
                        "---------",
                        "|e|d| | |",
                        "---------"
                    ].join("\n") + "\n"
                );
            });

    });


describe("runRobot",
    function () {
        it("no parcels",
            function () {
                console.log = jasmine.createSpy("log");
                let noParcels = new VillageState("Post Office", []);
                village.runRobot(noParcels);

                expect(console.log).toHaveBeenCalledWith("Done in 0 turns");
            });

        it("random robot",
            function () {
                console.log = jasmine.createSpy("log");
                village.runRobot(VillageState.random(), village.randomRobot);

                expect(console.log).toHaveBeenCalledWith(jasmine.stringMatching(/^Done/));
            });

        it("route robot",
            function () {
                console.log = jasmine.createSpy("log");
                village.runRobot(VillageState.random(), village.routeRobot, []);

                expect(console.log).toHaveBeenCalledWith(jasmine.stringMatching(/^Done/));
            });
    });
