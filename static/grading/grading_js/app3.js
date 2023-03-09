//declearing html elements

const addimgDiv = document.querySelector('.profile-addimg-div');
const addimg = document.querySelector('#addphoto');
const addfile = document.querySelector('#add_img');
const adduploadBtn = document.querySelector('#adduploadBtn');

//if user hover on img div 

addimgDiv.addEventListener('mouseenter', function(){
    adduploadBtn.style.display = "block";
});

//if we hover out from img div

addimgDiv.addEventListener('mouseleave', function(){
    adduploadBtn.style.display = "none";
});

//lets work for image showing functionality when we choose an image to upload

//when we choose a foto to upload

addfile.addEventListener('change', function(){
    //this refers to file
    const choosedFile = this.files[0];

    if (choosedFile) {

        const reader = new FileReader(); //FileReader is a predefined function of JS

        reader.addEventListener('load', function(){
            addimg.setAttribute('src', reader.result);
        });

        reader.readAsDataURL(choosedFile);
    }
});