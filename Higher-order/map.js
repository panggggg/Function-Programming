const persons = [
    { name: "John", age: 17},
    { name: "Jane", age: 10},
    { name: "Jim", age: 15},
]

// const olderPerson = []
// for(let i = 0; i < persons.length; i++){
//     const person = persons[i]
//     olderPerson.push({
//         ...person,
//         age: person.age * 2
//     })
// }
// console.log('Older persons: ', olderPerson)

const olderPerson = persons.map((person) => {
    return {
        ...person,
        age: person.age * 2
    }
})
console.log('Older persons: ', olderPerson)
