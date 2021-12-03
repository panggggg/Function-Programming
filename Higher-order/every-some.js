const persons = [
    { name: "John", age: 17},
    { name: "Jane", age: 10},
    { name: "Jim", age: 15},
]

// let isKids = true
// for(let i = 0; i < persons.length; i++){
//     const person = persons[i]
//     if(person.age > 15){
//         isKids = false
//         break
//     }
// }
// console.log('Is kids: ', isKids)

const isKids = persons.every(person => person.age > 15)
console.log('isKids: ', isKids)

const isAge17 = persons.some(person => person.age < 15)
console.log('isAge17: ', isAge17)