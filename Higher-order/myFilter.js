const persons = [
    { name: "John", age: 17},
    { name: "Jane", age: 10},
    { name: "Jim", age: 15},
]

function myFilter(arr, callback){
    const result = []
    for(let i = 0; i < arr.length; i++){
        const element = arr[i]
        if(callback(element)){
            result.push(element)
        }
    }
    return result
}

const kids = myFilter(persons, person => person.age < 17)
console.log('Kids: ', kids)