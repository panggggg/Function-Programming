const persons = [
    { name: "John", age: 17},
    { name: "Jane", age: 10},
    { name: "Jim", age: 15},
]

// let totalAge = 0
// for (let i = 0; i < persons.length; i++){
//     const person = persons[i]
//     totalAge += person.age
// }
// console.log('Total age: ', totalAge)

const totalAge = persons.reduce((age, person) => age + person.age , 0)
console.log('Total age: ', totalAge)