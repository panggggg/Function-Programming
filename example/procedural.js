//Procedural = top to bottom

const form = document.getElementById('user-input')

function signupHandler(event){
    event.preventDefault()

    const userNameInput = document.getElementById('username')
    const passwordInput = document.getElementById('password')

    const enterUsername = userNameInput.value
    const enterPassword = passwordInput.value

    if(enterUsername.trim().length === 0){
        alert('Invalis input - username must not be empty')
        return
    }
    if(enterPassword.trim().length <= 5){
        alert('Invalid input - password must be six characters or longer')
        return
    }

    const user = {
        userName: enterUsername,
        password: enterPassword
    }

    console.log(user)
    console.log(`Hi, I am ${user.userName}`)
}

form.addEventListener('submit', signupHandler)