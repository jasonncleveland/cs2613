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
}

module.exports.Message = Message;