document.addEventListener('DOMContentLoaded', function() {
    const startChatButton = document.getElementById('start-chat');
    const initialScreen = document.getElementById('initial-screen');
    const chatInterface = document.getElementById('chat-interface');

    startChatButton.addEventListener('click', function() {
        initialScreen.style.display = 'none';
        chatInterface.style.display = 'block';
        // Add your voice recognition code here
    });
});