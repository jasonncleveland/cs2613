const ms = require("../summarize_mail");

describe("summarize_mail", function () {
    it("no headers", function () {
        expect(ms.summarize_mail("example1.json")).toEqual([{}, {}, {}]);
        expect(ms.summarize_mail("example2.json")).toEqual(Array(10).fill({}));
    });

    it("Subject", function () {
        expect(ms.summarize_mail("example1.json", "Subject")).toEqual([
            { Subject: "[notmuch] archive" },
            { Subject: "Re: [notmuch] archive" },
            { Subject: "Re: [notmuch] archive" }
        ]);
    });

    it("Subject, Date", function () {
        expect(ms.summarize_mail("example1.json", "Subject", "Date")).toEqual([
            { Subject: "[notmuch] archive", Date: "Tue, 17 Nov 2009 18:21:38 -0500" },
            { Subject: "Re: [notmuch] archive", Date: "Tue, 17 Nov 2009 18:04:31 -0800" },
            { Subject: "Re: [notmuch] archive", Date: "Wed, 18 Nov 2009 02:22:12 -0800" }
        ]);
    });
});