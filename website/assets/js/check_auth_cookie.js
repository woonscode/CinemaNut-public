user = Cookies.get("user")
console.log(user)

if (user === undefined) {
    window.location.href = "login.html" // redirect immediately to Login
}