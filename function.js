//1. Pure function (can predict result)
function addPure(a, b) {
    return a + b
}
console.log('Pure Function: ', addPure(1, 6))


//2. Avoid Side Effect
const b = 6
function addSideEffect(a){
    return a + b
}
console.log('Side Effect: ', addSideEffect(1))


//3. First class function

//3.1 Assigning a function to a variable
const addAssigning = function addAssigning(a, b){
    return a + b
}
console.log('Assigning: ', addAssigning(1, 6))

//3.2 Returning a function (function ที่ return เป็น function)
function addReturning(a, b){
    return function(){
        return a + b
    }
}
const addTwoNumber = addReturning(1, 6)
console.log('Returning: ', addTwoNumber) //output => Returning:  [Function (anonymous)]
console.log('Returning: ', addTwoNumber()) //output => 7

//3.3 Accepting a funtion as an argument (function ที่รับ argument เป็น function)
function addNumber(a, b){
    return a + b
}
function addAccepting(add, a, b){
    return add(a, b)
}

console.log('Accepting: ', addAccepting(addNumber, 1, 6))
