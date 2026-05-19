async function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    const message = input.value;

    if (!message) return;

    chatBox.innerHTML += `<div class="user-message"><b>You:</b> ${message}</div>`;

    input.value = "";

    const response = await fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ message })
    });

    const data = await response.json();

    chatBox.innerHTML += `<div class="bot-message"><b>Bot:</b> ${data.reply}</div>`;

    chatBox.scrollTop = chatBox.scrollHeight;
}