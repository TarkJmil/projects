async function transcribeFunction() {
    // الإشارة إلى بعض العناصر وتغيير حال الزر
    const transactionButton=document.querySelector('#transcribeAudio');
    const textarea=document.getElementById('toSummarize');
    const fileInput=document.getElementById('file');
    transactionButton.innerHTML='جاري التفريغ...';
    transactionButton.style.backgroundColor = '#99d1ff';
    transactionButton.style.borderColor = '#99d1ff';
    const formData=new FormData();

    formData.append('file',fileInput.files[0])


    const response=await fetch('/transcripe-api',{
      method:'POST',
      body:formData
    });
    if (!response.ok){
      throw new console.error("Network response was not ok");
    }
    const transaction=await response.text();
    textarea.value=transaction;


    transactionButton.innerHTML='type'
    transaction.style.backgroundColor=''
    transactionButton.style.borderColor = ''
    writeKeywords();
};


async function writeKeywords(){
  const chatDiv = document.getElementById('keywords');
  const systemSettings = 'You must write keywords or tags based on the user input and it must be in Arabic and separated by comma';
  const userInput = document.getElementById('toSummarize').value.slice(0,3000);
  await chatgptCall(systemSettings,userInput,chatDiv);

};
 
async function writeKeywords_en(){
  const chatDiv = document.getElementById('keywords-en');
  const systemSettings = 'You must write keywords or tags based on The article you wrote and it must be in English and separated by comma';
  const userInput = document.getElementById('toSummarize').value.slice(0,3000);
  await chatgptCall(systemSettings,userInput,chatDiv)
  generateImage();
};