// function outer() {
//     const name = 'Outer'
//     function inner() {
//         console.log(`Outer name: ${name}`)
//     }
//     inner()
// }
// outer()

function outer() {
    const name = 'Outer'
    return function inner() {
        console.log(`Outer name: ${name}`)
    }
}
const innerFunction = outer()
console.log('Inner fuction: ', innerFunction) //output => Inner fuction:  [Function: inner]
innerFunction() //output => Outer name: Outer


//Data privacy

// function times(){
//     let counter = 0
//     counter += 1
//     console.log('Counter: ', counter)
// }
// times() // 1
// times() // 1

function createTime(){
    let counter = 0 //private variable
    return function times(){
        counter += 1
        console.log('Counter: ', counter)
    }
}
const time = createTime()
time() // 1
time() // 2
time() // 3


//Stateful functions
// function addFive(a){
//     return a + 5
// }
// function addTen(a){
//     return a + 10
// }

// console.log('Add Five: ', addFive(5))
// console.log('Add Ten: ', addTen(10))

function createAdd(a){
    return function(b){ // <- stateful function คือ ฟังก์ชันที่มีการ fixed ค่าไว้แล้ว คือ a 
        return a + b
    }
}
const addFive = createAdd(5)
const addTen = createAdd(10)

console.log('Add Five: ', addFive(5))
console.log('Add Ten: ', addTen(10))