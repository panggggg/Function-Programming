const persons = [
    { name: "John", age: 17},
    { name: "Jane", age: 10},
    { name: "Jim", age: 15},
]

// let jane
// for(let i = 0; i < persons.length; i++){
//     const person = persons[i]
//     if(person.name === 'Jane'){
//         jane = person
//         break
//     }
// }
// console.log('Jane: ', jane)


persons.find(person => console.log(person.name === 'Jane')) // false true false

const jane = persons.find(person => person.name === 'Jane')
console.log('Jane: ', jane)

const janeIndex = persons.findIndex(person => person.name === 'Jane')
console.log('Jane Index: ', janeIndex)