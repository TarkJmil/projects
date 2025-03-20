async function sendMessage() {
  const userInput = document.getElementById('humanInput').value;
  document.getElementById('humanInput').value = '';

  const newMassage = document.createElement('div');
  newMassage.classList.add('humanMessage');
  newMassage.innerHTML = userInput;

  const massageList = document.getElementById('messageList');
  massageList.appendChild(newMassage);

  const replyMassage = document.createElement('div');
  replyMassage.classList.add('botMessage');
  massageList.appendChild(replyMassage);

  const systemSettings = 'You are a chat bot, reply in Arabic.';

  await chatgptCall(systemSettings, userInput, replyMassage);
}