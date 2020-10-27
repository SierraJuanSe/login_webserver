const validateRegister = () => {
    let email = document.forms['registerForm']['email'].value
    let password = document.forms['registerForm']['password'].value
    let c_password = document.forms['registerForm']['c_password'].value
    let p = document.getElementById('alert')
    correctEmail = validateEmail(email)
    correctPass = validatePassword(password, c_password)

    if (!correctEmail) {
        p.innerHTML = 'Invalid email'
        return false
    }

    if (!correctPass) {
        p.innerHTML = "Passwords don't match"
        return false
    }

    alert_p = document.getElementById('alert_register')
    alert_p.innerHTMl = 'Account created'
}

const validateSingIn = () => {
    let email = document.forms['registerForm']['email'].value
    let p = document.getElementById('alert')
    correctEmail = validateEmail(email)

    if (!correctEmail) {
        p.innerHTML = 'Invalid email'
        return false
    }

    alert_p = document.getElementById('alert_register')
    alert_p.innerHTMl = 'Account created'
}

const validateEmail = (email) => {
    reg = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/
    return reg.test(email)
}

const validatePassword = (p, cp) => p === cp
