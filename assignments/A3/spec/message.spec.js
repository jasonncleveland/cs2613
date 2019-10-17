const Message = require("../message").Message;
const flatten = require("../flatten").flatten;
const read_json_file = require("../read_json_file").read_json_file;

let testMsg = new Message({ "headers": { "Subject": "lunch", "Date": "now" }});

describe("Message class", function () {
    it("new message is not null", function () {
        expect(testMsg).not.toEqual(null);
    });

    it("subject accessor", function () {
        expect(testMsg.subject).toEqual("lunch");
    });


    it("JSON file data", function () {
        const data = read_json_file("example1.json");
        const flattened_data = flatten(data);

        const expected = [
            {
                "Subject": "[notmuch] archive",
                "From": "Aron Griffis <agriffis@n01se.net>",
                "To": "notmuch <notmuch@notmuchmail.org>",
                "Date": "Tue, 17 Nov 2009 18:21:38 -0500"
            },
            {
                "Subject": "Re: [notmuch] archive",
                "From": "Keith Packard <keithp@keithp.com>",
                "To": "Aron Griffis <agriffis@n01se.net>, notmuch <notmuch@notmuchmail.org>",
                "Date": "Tue, 17 Nov 2009 18:04:31 -0800"
            },
            {
                "Subject": "Re: [notmuch] archive",
                "From": "Carl Worth <cworth@cworth.org>",
                "To": "Keith Packard <keithp@keithp.com>, Aron Griffis <agriffis@n01se.net>, notmuch <notmuch@notmuchmail.org>",
                "Date": "Wed, 18 Nov 2009 02:22:12 -0800"
            }
        ];

        flattened_data.forEach((element, i) => {
            let message = new Message(element);
            
            expect(message.subject).toBe(expected[i]["Subject"]);
            expect(message.date).toBe(expected[i]["Date"]);
            expect(message.from).toBe(expected[i]["From"]);
            expect(message.to).toBe(expected[i]["To"]);
        });
    });
});