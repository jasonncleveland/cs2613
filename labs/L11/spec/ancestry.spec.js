let by_name = require("../ancestry").by_name;

describe("by_name", function () {
    it("not-present", function () {
        expect(by_name("ronald mcdonal")).toBe(null);
        expect(by_name("Captain Ahab")).toBe(null);
    });

    it("first", function () {
        expect(by_name("Carolus Haverbeke")).toEqual({ "name": "Carolus Haverbeke", "sex": "m", "born": 1832, "died": 1905, "father": "Carel Haverbeke", "mother": "Maria van Brussel" });
        expect(by_name("Jacobus Bernardus van Brussel")).toEqual({ "name": "Jacobus Bernardus van Brussel", "sex": "m", "born": 1736, "died": 1809, "father": "Jan van Brussel", "mother": "Elisabeth Haverbeke" });
        expect(by_name("Joanna de Pape")).toEqual({ "name": "Joanna de Pape", "sex": "f", "born": 1654, "died": 1723, "father": "Vincent de Pape", "mother": "Petronella Wauters" });
    });
});