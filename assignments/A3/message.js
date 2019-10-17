const deep_equal = require("./deep_equal").deep_equal;

class Message {
    constructor(message) {
        Object.keys(message).forEach(key => {
            this[key] = message[key];
        });

        this.subject = message["headers"]["Subject"];
        this.date = message["headers"]["Date"];
        this.from = message["headers"]["From"];
        this.to = message["headers"]["To"];
    }

    equals(other) {
        return deep_equal(this, other);
    }
}

module.exports.Message = Message;