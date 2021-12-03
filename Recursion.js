//ฟังก์ชันที่สามารถเรียกใช้ตัวมันเองได้

function countDown(n){
    if(n < 0){
        return
    }
    console.log('Count down: ', n)
    countDown(n - 1)
}
countDown(10)
////////////////////////////////////////
// f(1) => 1
// f(2) => 1 * 2 => f(1) * 2
// f(3) => 1 * 2 * 3 => f(2) * 3
////////////////////////////////////////
function factorial(n){
    if (n === 1) return 1
    return n * factorial(n - 1)
}
console.log('Factorial: ', factorial(4))
////////////////////////////////////////
// c   =>   c
// bc  =>   cb => reverse(c) + b
// abc =>   cba => reverse(cb) + a
////////////////////////////////////////
function reverse(str){
    if(str.length === 1) return str
    const [firstCharacter] = str
    const remainingCharacter = str.substring(1)
    return reverse(remainingCharacter) + firstCharacter
}
console.log('Reverse: ', reverse('pawornwan'))