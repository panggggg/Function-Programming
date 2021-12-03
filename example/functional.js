const REQUIRED = 'REQUIRED'
const MIN_LENGTH = 'MIN_LENGTH'

function validate(value, flag, validatorValue){
    if(flag === this.REQUIRED){
        return value.trim().length > 0
    }
    if(flag === this.MIN_LENGTH){
        return value.trim().length > validatorValue
    }
}

function getUserInput(inputElementId){
    console.log(document.getElementById(inputElementId).value)
    return document.getElementById(inputElementId).value
}

function createUser(userName, userPassword){
    if( !validate(userName, REQUIRED) || !validate(userPassword, MIN_LENGTH, 5)){
        throw new Error('Invalid input - username or password is wrong (password should be at least 5 character)')
    }
    return {
        userName: userName,
        userPassword: userPassword
    }
}

function greetUser(user){
    console.log(`Hi, I am ${user}`)
}

function signupHandler(event){
    event.preventDefault()

    const enterUsername = getUserInput('username')
    const enterPassword = getUserInput('password')
    
    try{
        const newUser = createUser(enterUsername, enterPassword)
        greetUser(newUser)
    } catch(err) {
        alert(err.message)
    }
}

function connectForm(formId, formSubmitHandler) {
    const form = document.getElementById(formId)
    form.addEventListener('submit', formSubmitHandler)
}

connectForm('user-input', signupHandler)