async function summarizeArticle() {
  // نشير إلى عنصر المدخلات عنصر المخرجات ونحدد رسالة النظام، ثم نرسلهم إلى النموذج ونقوم باستدعاء الدالة التالية
  const userInput = document.getElementById('toSummarize').value;
  const chatDiv = document.getElementById('summarized');
  const systemSettings = 'the user will input a text ,your job is to write a short summary in Arabic';

  await chatgptCall(systemSettings,userInput,chatDiv,true);

  writeTitle();

  writeKeywords();
  writeKeywords_en();
}


async function writeTitle(){
  const chatDiv = document.getElementById('title');
  const systemSettings = 'You are giving a short text, give this text suitable title in arabic';
  const userInput = document.getElementById('summarized').value.slice(0,3000);
  await chatgptCall(systemSettings,userInput,chatDiv);

}


async function writeKeywords(){
  const chatDiv = document.getElementById('keywords');
  const systemSettings = 'You must write keywords or tags based on the user input and it must be in Arabic and separated by comma';
  const userInput = document.getElementById('summarized').value.slice(0,3000);
  await chatgptCall(systemSettings,userInput,chatDiv);
}
 

async function writeKeywords_en(){
  const chatDiv = document.getElementById('keywords-en');
  const systemSettings = 'You must write keywords or tags based on the user input and it must be in English and separated by comma';
  const userInput = document.getElementById('summarized').value.slice(0,3000);
  await chatgptCall(systemSettings,userInput,chatDiv);
  generateImage();
}
 