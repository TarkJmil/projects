async function writeArticle() {
    // نقوم بتعطيل زر الاستطالة وقت عملية الاستطالة
    const continueButton=document.getElementById('continue-button');
    continueButton.setAttribute('disabled','');
    const chatDiv=document.getElementById('maqal');
    const userInput=document.getElementById('articleTitle').value;
    const systemSettings='the user will input a title your job is Use the title to create an article in Arabic';
    await chatgptCall(systemSettings,userInput,chatDiv);
    continueButton.removeAttribute('disabled');
    
    writeKeywords();
    writeKeywords_en();
    
  }

async function extendArticle() {
    // نقوم بتعطيل زر الاستطالة وقت عملية الاستطالة
    const continueButton=document.getElementById('continue-button');
    continueButton.setAttribute('disabled','');
    const chatDiv=document.getElementById('maqal');
    const systemSettings='the user will input an article your job is to extend the article in Arabic, Only give the extension';
    const userInput=document.getElementById('maqal').value;
    await chatgptCall(systemSettings,userInput,chatDiv);
    continueButton.removeAttribute('disabled');
  }

async function writeKeywords() {
  // نشير إلى عنصر المدخلات عنصر المخرجات ونحدد رسالة النظام، ثم نرسلهم إلى النموذج ونقوم باستدعاء الدالة التالية
  const chatDiv=document.getElementById('keywords');
  const systemSettings='the user will input an article your job Is to write tags/keywords in Arabic';
  const userInput=document.getElementById('maqal').value;
  await chatgptCall(systemSettings,userInput,chatDiv);
}
async function writeKeywords_en(){
  const chatDiv = document.getElementById('keywords-en');
  const systemSettings = 'You must write keywords or tags based on The article you wrote and it must be in English and separated by comma';
  const userInput = document.getElementById('maqal').value.slice(0,3000);
  await chatgptCall(systemSettings,userInput,chatDiv)
  generateImage();
}