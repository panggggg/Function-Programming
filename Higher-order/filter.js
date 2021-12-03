//Higher order function
//-> Returning a function
//-> Accepting a function as an argument

const persons = [
    { name: "John", age: 17},
    { name: "Jane", age: 10},
    { name: "Jim", age: 15},
]

// const kids = []
// for(let i = 0; i < persons.length; i++){
//     const person = persons[i]
//     if(person.age <= 15){
//         kids.push(person)
//     }
// }
// console.log("Kids: ", kids)


const kids = persons.filter(person => person.age <= 15)
console.log('Kids: ', kids)