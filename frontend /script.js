function sendMessage() {
    const input = document.getElementById("userInput").value;

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message: input })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("chat").innerText = "Bot: " + data.reply;
    });
}
