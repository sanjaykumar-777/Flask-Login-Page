
//const email= document.getElementsByName('email-address')
const password= document.getElementById('nid_number')
const form= document.getElementById('form')
const errorElement =document.getElementById('error')
const email= document.getElementById('email_address').value;

let messages=[]
function validate(){
  
  
  var regx= /^([a-zA-Z0-9\._]+)@([a-zA-Z0-9])+.([a-z]+)(.[a-z]+)?$/
  
  if(regx.test(email)){
    return true;
  }
  else{
    messages.push("Sorry ! Enter a valid email address")
    return false;
  }
  }

form.addEventListener('submit' , (e) =>{
 
 
  
  
  

  if(password.value.length <=6){
    messages.push('password must be longer than 6 characters')
  }

  if(password.value.length >=20){
    messages.push('password must be less than 20 characters')
  }

  if(password.value === 'password'){
    messages.push('password cannot be password')
  }
  if(messages.length > 0){
    e.preventDefault()
    errorElement.innerText = messages.join(', ')
  }
 
  
})
