const persons = [
    { name: "John", age: 17},
    { name: "Jane", age: 10},
    { name: "Jim", age: 15},
]

function myMap(arr, callback){
    const result = []
    for(let i = 0; i < arr.length; i++){
        const element = arr[i]
        result.push(callback(element))
    }
    return result
}

const olderPersons = myMap(persons, person => ({
    ...person,
    age: person.age * 2
}))
console.log('Older persons: ', olderPersons)