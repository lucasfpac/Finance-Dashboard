const usernameField = document.querySelector("#usernameField");
const feedBackArea = document.querySelector(".invalid-feedback");
usernameField.addEventListener("keyup", (e) => {
  const usernameVal = e.target.value;

  usernameField.classList.remove("is-invalid");
  feedBackArea.style.display = "none";

  if (usernameVal.length > 0) {
    fetch("/authentication/validate-username", {
      body: JSON.stringify({ username: usernameVal }),
      method: "POST",
    })
      .then((res) => res.json())
      .then((data) => {
        console.log("data", data);
        if (data.username_error) {
          usernameField.classList.add("is-invalid");
          feedBackArea.style.display = "block";
          feedBackArea.innerHTML = `<p>${data.username_error}</p>`;
        }
        if (data.username_valid) {
          usernameField.classList.add("is-valid");
          feedBackArea.style.display = "block";
          feedBackArea.innerHTML = `<p>Username Available</p>`;
        }
      });
  }
});
