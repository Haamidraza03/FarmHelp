function check()
{
    let username=document.getElementById('name').value;
    let useremail=document.getElementById('email').value;
    let pswd1=document.getElementById('password').value;
    let pswd2=document.getElementById('cpassword').value;
    let adhaarno=document.getElementById('adhaar').value;
    let phno=document.getElementById('phone').value;
    let voterid=document.getElementById('voter').value;
    let rationcard=document.getElementById('ration').value;


    let user={
        name:username,
        adhaar:adhaarno,
        phone:phno,
        voter:voterid,
        ration:rationcard,
        email:useremail,
        password:pswd1
        
    }


    if(adhaarno.length==12 && phno.length==10 && rationcard.length==10 && voterid.length==10 && pswd1==pswd2 && username.length>1 && useremail.length>3 && pswd1.length>3 && pswd2.length>3)
    {
        fetch('https://farmhelp-7bbda-default-rtdb.firebaseio.com/user.json',
        {
            method:'post',
            body:JSON.stringify(user)
        }).then(()=>
        {
            alert('Your Data is saved successfully.Please Login.');
            document.getElementById('name').value="";
            document.getElementById('adhaar').value="";
            document.getElementById('phone').value="";
            document.getElementById('voter').value="";
            document.getElementById('ration').value="";
            document.getElementById('email').value="";
            document.getElementById('password').value="";
            document.getElementById('cpassword').value="";
            window.location.href="./login.html";
        })
    }
    else if(adhaarno.length==0 && phno.length==0 && rationcard.length==0 && voterid.length==0)
    {
        alert("Please fill all the Details.")
    }
    else if(adhaarno.length!=12)
    {
        alert("Adhaar Card No. should be of 12 digits. Please fill Accordingly!!!")
    }
    else if(phno.length!=10 && phno>1234567891)
    {
        alert("Phone No. should be of 10 digits. Please fill Accordingly!!!")
    }
    else if(rationcard.length!=10)
    {
        alert("Ration Card No. should be of 10 Alphanumeric Characters. Please fill Accordingly!!!")
    }
    else if(voterid.length!=10)
    {
        alert("Voter Id should be of 10 Alphanumeric Characters. Please fill Accordingly!!!")
    }
    else if(pswd1!=pswd2){
        alert('Password and Confirm password should be same.')
    }
    else{
        alert("Please fill all Details.")
    }
}