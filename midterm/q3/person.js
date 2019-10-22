class Person {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }

    birthday() {
        return new Person(this.name, this.age + 1);
    }
}

module.exports.Person = Person;
