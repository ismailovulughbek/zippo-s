document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("contact-form");
    const responseMsg = document.getElementById("responseMsg");

    form.addEventListener("submit", function (e) {
        e.preventDefault();

        const data = {
            name: form.name.value.trim(),
            email: form.email.value.trim(),
            phone: form.phone.value.trim(),
            subject: form.subject.value.trim(),
            message: form.message.value.trim()
        };


        if (!data.name || !data.email || !data.phone || !data.subject || !data.message) {
            showMessage("Please fill in all fields!", 0)
            return;
        }

        fetch("/contact_message", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })
        .then(res => res.json())
        .then(data => {
            showMessage(data.message, 1)
            if (data.status === "success") form.reset();
        })
        .catch(err => {
            showMessage(data.message, 0)
            console.error(err);
        });
    });

    function showMessage(msg, msg_type) {
        responseMsg.innerText = msg;
        responseMsg.style.opacity = "1";
        responseMsg.style.display = "block";
        responseMsg.style.fontSize = "16px";
        responseMsg.style.fontWeight = "700";
        responseMsg.style.color = msg_type === 1 ? "green" : "red";

        setTimeout(() => {
            responseMsg.style.opacity = "0";
            responseMsg.style.display = "none";
        }, 3000);
    }
});
