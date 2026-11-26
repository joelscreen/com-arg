if (localStorage.getItem("code") != "130367") {
    window.location.href = '/';
}

const input_box = document.getElementById("puzzle-1-code");
const submit_btn = document.getElementById("submit");
const correct = document.getElementById("correct");

submit_btn.addEventListener('click', async function() {
    const response = await fetch('/puzzle-code', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            puzzle: "4",
            code: input_box.value
        })
    })

    if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();

    if (input_box.value == "") {
        correct.textContent = "PLEASE ENTER A CODE";
        correct.style.color = "#8b0404";
        
        setTimeout(() => {
            correct.textContent = "";
        }, 2000)
    }
    else if (data.correct == false) {
        correct.textContent = "INCORRECT CODE";
        correct.style.color = "#8b0404";
        
        setTimeout(() => {
            correct.textContent = "";
        }, 2000)
    }
    else if (data.correct == true) {
        correct.textContent = "CORRECT CODE";
        correct.style.color = "#237c08";

        setTimeout(async function() {
            const response = await fetch('/puzzle-1');

            if (response.ok) {
                localStorage.setItem("code", input_box.value);
                window.location.href = '/puzzle-5'
            } else {
                correct.textContent = "ACCESS DENIED";
                correct.style.color = "#8b0404";
            }
        }, 2000)
    }
});
