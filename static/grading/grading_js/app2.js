const imgDiv2 = document.querySelector('.profile-pic-div2');
const img2 = document.querySelector('#photo2');
const file2 = document.querySelector('#Ed_img');
const uploadBtn2 = document.querySelector('#uploadBtn2');

imgDiv2.addEventListener('mouseenter', function(){
    uploadBtn2.style.display = "block";
});

imgDiv2.addEventListener('mouseleave', function(){
    uploadBtn2.style.display = "none";
});

file2.addEventListener('change', function(){
   
    const choosedFile = this.files[0];

    if (choosedFile) {

        const reader = new FileReader(); 

        reader.addEventListener('load', function(){
            img2.setAttribute('src', reader.result);
        });

        reader.readAsDataURL(choosedFile);
    }
});