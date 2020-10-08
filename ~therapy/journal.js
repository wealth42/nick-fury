$(document).ready(function() {
    $(window).scroll(function() {
        var scroll = $(window).scrollTop();
        if (scroll > 100) {
            $(".navbar-light").css("background", "black");
            $(".navbar-toggler").css("background", "white");

        } else {
            $(".navbar-light").css("background", "transperant");
        }
    })
})


var emotion = [{
    "Happiness": {
        "1": "Delighted",
        "2": "Ebullient"
    },
    "caring": {
        "1": "Adoring",
        "2": "Zealous",
        "3": "Zealous",
        "4": "Passionate",
        "5": "Worshipful",


    },
    "Depression": {
        "1": "Bleak",
        "2": "Dejected"
    },
    "Fear": {
        "1": "Desperate",
        "2": "Petrified",
        "3": "Terrified",
        "4": "Wrecked",

    },
}]

var recent = [{
    "id": 345,
    "name": "Dr. Bowen Chan",
    "gender": "M",
    "phone": "416-486-1956",
    "rating": 4.5,
    "image": "./images/male.jpg",
    "comments": {
        "1": "Better response from the patients",
        "2": "Health is increasing",
        "3": "Getting more exercise",
        "4": "Reduction in weight",
        "5": "Mental stability",

    },



    "image": "./images/male.jpg",
    "availability": {
        "Monday": "8:30am - 5:30pm",
        "Wednesday": "1:30pm - 7:30pm",
        "Thrusday": "10am - 8pm",
        "Friday": "9am - 12pm"
    },
}]

var curent = recent.map(function(j) {
    return `
    <div class="container">
    <div class="row">
    <div  class="col-lg-6 col-md-6 col-sm-12" id="text">
    <p class="p-name"> Name: ${j.name}</p>
    <p class="p-desc"> Gender: ${j.gender}</p>
    <p class="p-created"> Phone Number: ${j.phone}</p>
    <p class="p-created"> Rating: ${j.rating}/5</p><br>
    <button id="remove" data-aos="zoom-in" data-aos-duration="1000">Remove</button><br><br>
    <h5>Journal Details:</h5>
    <ul>
    <li> Doctor points: ${j.comments[1]}</li>
    <li> Doctor points: ${j.comments[2]}</li>
    <li> Doctor points: ${j.comments[3]}</li>
    <li> Doctor points: ${j.comments[4]}</li>
    <li> Doctor points: ${j.comments[5]}</li>
    </ul>
    </div>
    <div class="col-lg-6 col-md-12 col-sm-12" id="image">
    <img src="${j.image}">
    </div>
    </div>
    </div>
  `
})
$('#current').append(curent);

var emotion = emotion.map(function(j) {
    return `
    <div class="container">
    <div class="row">
    <div  class="col-lg-12 col-md-12 col-sm-12" data-aos="zoom-in" data-aos-duration="1000">
    <button class="buo" data-aos="zoom-in" data-aos-duration="1000">${j.Happiness[1]}</button>
    <button class="buo" data-aos="zoom-in" data-aos-duration="1100">${j.Happiness[2]}</button>
    <button class="buo" data-aos="zoom-in" data-aos-duration="1200">${j.caring[1]}</button>
    <button class="buo" data-aos="zoom-in" data-aos-duration="1300">${j.caring[2]}</button>
    <button class="buo" data-aos="zoom-in" data-aos-duration="1400">${j.caring[3]}</button>
    <button class="buo" data-aos="zoom-in" data-aos-duration="1500">${j.caring[5]}</button>
    <button class="buo" data-aos="zoom-in" data-aos-duration="1600">${j.caring[4]}</button>
    <button class="buo" data-aos="zoom-in" data-aos-duration="1700">${j.Depression[1]}</button>
    <button class="buo" data-aos="zoom-in" data-aos-duration="1800">${j.Depression[2]}</button>
    <button class="buo" data-aos="zoom-in" data-aos-duration="1900">${j.Fear[1]}</button>
    <button class="buo" data-aos="zoom-in" data-aos-duration="2000">${j.Fear[2]}</button>
    <button class="buo" data-aos="zoom-in" data-aos-duration="2100">${j.Fear[3]}</button>
    <button class="buo" data-aos="zoom-in" data-aos-duration="2200">${j.Fear[4]}</button>
    </div>
 
    </div>
    </div>
  `
})

$('#emotional').append(emotion);

var buttonList = $(".buo");


buttonList.each(function() {
    $(this).click(function() {
        $(this).toggleClass("button-style");
    });
});
