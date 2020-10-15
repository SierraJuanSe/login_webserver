const validateForm = () => {
    let email = document.forms['registerForm']['email'].value
    let password = document.forms['registerForm']['password'].value
    let c_password = document.forms['registerForm']['c_password'].value
    correctEmail = validateEmail(email)
    correctPass = validatePassword(password, c_password)

    if (!correctEmail) {
        alert_p = document.getElementById('alert_register')
        alert_p.innerHTMl = 'Invalid Email'
        return false
    }
    if (!correctPass) {
        alert_p = document.getElementById('alert_register')
        alert_p.innerHTMl = "Passwords don't match"
        return false
    }

    alert_p = document.getElementById('alert_register')
    alert_p.innerHTMl = 'Registrado'
}

const validateEmail = (email) => {
    reg = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3,4})+$/
    return reg.test(email)
}

const validatePassword = (p, cp) => p === cp
