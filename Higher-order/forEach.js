const persons = [
    { name: "John", age: 17},
    { name: "Jane", age: 10},
    { name: "Jim", age: 15},
]

// for(let i = 0; i < persons.length; i++){
//     const person = persons[i]
//     console.log(`Name ${person.name} age ${person.age}`)
// }

persons.forEach(person => console.log(`Name ${person.name} age ${person.age}`))