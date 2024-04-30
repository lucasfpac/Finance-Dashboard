const usernameField = document.querySelector("#usernameField");
const usernameFeedBackArea = document.querySelector(".username-invalid-feedback");

const emailField = document.querySelector('#emailField');
const emailFeedBackArea = document.querySelector(".email-invalid-feedback");

const passwordField = document.querySelector('#passwordField');
const passwordToggle = document.querySelector('.password-toggle')

const submitBtn = document.querySelector('.submit-btn')

const handleToggleInput=(e) =>{

    if(passwordToggle.textContent==='SHOW'){
        passwordToggle.textContent = "HIDE";
        passwordField.setAttribute("type", "text")
    }else{
        passwordToggle.textContent = "SHOW"
        passwordField.setAttribute("type", "password")
    }
}

passwordToggle.addEventListener('click', handleToggleInput);


usernameField.addEventListener("keyup", (e) => {
    const usernameVal = e.target.value;
    usernameField.classList.remove("is-invalid");
    usernameField.classList.remove("is-valid");
    usernameFeedBackArea.style.display = "none";
    submitBtn.removeAttribute("disabled");


    if (usernameVal.length > 0) {
    fetch("/authentication/validate-username", {
        body: JSON.stringify({ username: usernameVal }),
        method: "POST",
    })
        .then((res) => res.json())
        .then((data) => {
            console.log("data", data);
            if (data.username_error) {
                submitBtn.disabled = true;
                usernameField.classList.add("is-invalid");
                usernameFeedBackArea.style.display = "block";
                usernameFeedBackArea.style.color = "red";
                usernameFeedBackArea.innerHTML = `<p>${data.username_error}</p>`;
            }
            if (data.username_valid) {
                usernameField.classList.add("is-valid");
                usernameFeedBackArea.style.display = "block";
                usernameFeedBackArea.style.color = "green";
                usernameFeedBackArea.innerHTML = `<p>Username Available</p>`;
            }
        
        });
    }
});

emailField.addEventListener("keyup", (e) =>{
    const emailVal = e.target.value;

    emailField.classList.remove("is-invalid");
    emailField.classList.remove("is-valid");
    emailFeedBackArea.style.display = "none";   
    submitBtn.removeAttribute("disabled");


    if (emailVal.length > 0) {
        fetch("/authentication/validate-email", {
            body: JSON.stringify({ email: emailVal }),
            method: "POST",
        })
            .then((res) => res.json())
            .then((data) => {
            console.log("data", data);
            if (data.email_error) {
                submitBtn.disabled = true;
                emailField.classList.add("is-invalid");
                emailFeedBackArea.style.display = "block";
                emailFeedBackArea.style.color = "red";
                emailFeedBackArea.innerHTML = `<p>${data.email_error}</p>`;
            }
            if (data.email_valid) {
                emailField.classList.add("is-valid");
                emailFeedBackArea.style.display = "block";
                emailFeedBackArea.style.color = "green";
                emailFeedBackArea.innerHTML = `<p>email Available</p>`;
            }
            
            });
        }
    })