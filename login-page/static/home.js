const email=document.getElementsByName('email')
const password=document.getElementsByName('password')
const errorElement =document.getElementById('error')

from.addEventListener('submit' , (e) =>{
 
    let messages=[]
    if(email.value === '' || email.value == null ){
      messages.push('email address is not a valid address')
      
    }
  
    if(password.value.length <=6){
      messages.push('password must be longer than 6 characters')
    }
  
    if(password.value.length >=20){
      messages.push('pssword must be less than 20 characters')
    }
  
    if(password.value === 'password'){
      messages.push('password cannot be password')
    }
    if(messages.length > 0){
      e.preventDefault()
      errorElement.innerText = messages.join(', ')
    }
  })