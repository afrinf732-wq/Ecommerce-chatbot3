async function sendMessage() {
  const input = document.getElementById("userInput");
  const chat = document.getElementById("chat");

  const userMessage = input.value;
  if (!userMessage) return;

  // Show user message
  chat.innerHTML += `<p><b>You:</b> ${userMessage}</p>`;
  input.value = "";

  try {
    const response = await fetch("http://localhost:5000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message: userMessage })
    });

    const data = await response.json();

    chat.innerHTML += `<p><b>Bot:</b> ${data.reply}</p>`;
  } catch (error) {
    chat.innerHTML += `<p style="color:red;"><b>Error:</b> Backend not connected</p>`;
  }
}
