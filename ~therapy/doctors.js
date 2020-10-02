/*dummy data*/
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


var data = [{
        "id": 345,
        "name": "Dr. Bowen Chan",
        "gender": "M",
        "image": "./images/male.jpg",
        "availability": {
            "Monday": "8:30am - 5:30pm",
            "Wednesday": "1:30pm - 7:30pm",
            "Thrusday": "10am - 8pm",
            "Friday": "9am - 12pm"
        },
        "phone": "416-486-1956",
        "address": {
            "street": "473 Dupont Street",
            "city": "Toronto",
            "prov": "ON",
            "postal": "M6G 1Y6"
        },
        "reviews": [{
                "name": "",
                "rating": 5,
                "comments": "Very good doctor.",
                "attributes": {
                    "staff": 5,
                    "punctual": 5,
                    "helpful": 5,
                    "knowledge": 5
                }
            },
            {
                "name": "",
                "rating": 5,
                "comments": "They are particularly wonderful with my baby daughter",
                "attributes": {
                    "staff": 5,
                    "punctual": 5,
                    "helpful": 5,
                    "knowledge": 5
                }
            },
            {
                "name": "",
                "rating": 4.75,
                "comments": "Awesome doc that really knows his stuff.",
                "attributes": {
                    "staff": 5,
                    "punctual": 4,
                    "helpful": 5,
                    "knowledge": 5
                }
            },
            {
                "name": "",
                "rating": 3.75,
                "comments": "We had to find a new Dr. with the sudden passing of ours. Dr. Chan & his Associates are very caring.",
                "attributes": {
                    "staff": 3,
                    "punctual": 4,
                    "helpful": 5,
                    "knowledge": 3
                }
            }
        ]
    }, {
        "id": 564,
        "name": "Dr. Michael Lewis BSc, MD, CCFP",
        "gender": "M",
        "image": "./images/male.jpg",
        "availability": {
            "Monday": "9am - 5pm",
            "Tuesday": "9am - 12pm",
            "Friday": "9am - 12pm"
        },
        "phone": "416-486-1956",
        "address": {
            "street": "200 St. Clair Ave. West Suite 110",
            "city": "Toronto",
            "prov": "ON",
            "postal": "M4V 1R1"
        },
        "reviews": [{
            "name": "",
            "rating": 2.5,
            "comments": "Dr. Lewis is good, but the person whop answers the phone and who you depend on to get an appointment, keep track of information, etc, is terrible. Her command of the english language isn't great, and results in a LOT of errors.",
            "attributes": {
                "staff": 1,
                "punctual": 2,
                "helpful": 3,
                "knowledge": 4
            }
        }]
    }, {
        "id": 675,
        "name": "Dr. Sharon Hind BScH, MD, CCFP",
        "gender": "F",
        "image": "./images/femla.jpg",
        "availability": {
            "Monday": "10am - 2pm",
            "Tuesday": "11am - 5pm",
            "Wednesday": "10am - 5pm"
        },
        "phone": "416-486-1956",
        "address": {
            "street": "200 St. Clair Ave. West Suite 110",
            "city": "Toronto",
            "prov": "ON",
            "postal": "M4V 1R1"
        },
        "reviews": [{
                "name": "",
                "rating": 5,
                "comments": "",
                "attributes": {
                    "staff": 5,
                    "punctual": 5,
                    "helpful": 5,
                    "knowledge": 5
                }
            },
            {
                "name": "",
                "rating": 4.75,
                "comments": "",
                "attributes": {
                    "staff": 5,
                    "punctual": 5,
                    "helpful": 5,
                    "knowledge": 4
                }
            },
            {
                "name": "",
                "rating": 4.75,
                "comments": "very caring and attentive",
                "attributes": {
                    "staff": 4,
                    "punctual": 5,
                    "helpful": 5,
                    "knowledge": 5
                }
            },
            {
                "name": "",
                "rating": 4.75,
                "comments": "",
                "attributes": {
                    "staff": 4,
                    "punctual": 5,
                    "helpful": 5,
                    "knowledge": 3
                }
            }
        ]
    }, {
        "id": 152,
        "name": "Dr. Sheeja Mathai",
        "gender": "F",
        "image": "./images/femla.jpg",
        "availability": {},
        "phone": "647-722-2370",
        "address": {
            "street": "390 Steeles Avenue West",
            "city": "Vaughan",
            "prov": "ON",
            "postal": "L4J"
        },
        "reviews": []
    }, {
        "id": 222,
        "name": "Dr. Preston Tran",
        "gender": "M",
        "image": "./images/male.jpg",
        "phone": "647-722-2370",
        "address": {
            "street": "390 Steeles Avenue West",
            "city": "Vaughan",
            "prov": "ON",
            "postal": "L4J"
        },
        "reviews": [{
            "name": "",
            "rating": 4.5,
            "comments": "Wonderful doctor: respectful, skillful, thorough, takes time, cares. ",
            "attributes": {
                "staff": 4,
                "punctual": 4,
                "helpful": 5,
                "knowledge": 5
            }
        }]
    }

]

var recent = [{
    "id": 345,
    "name": "Dr. Bowen Chan",
    "gender": "M",
    "phone": "416-486-1956",
    "rating": 4.5,
    "image": "./images/male.jpg",



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
    <div  class="col-lg-6 col-md-6 col-sm-12" data-aos="zoom-in" data-aos-duration="1000">
    <p class="p-name"> Name: ${j.name}</p>
    <p class="p-desc"> Gender: ${j.gender}</p>
    <p class="p-created"> Phone Number: ${j.phone}</p>
    <p class="p-created"> Rating: ${j.rating}/5</p>
    <button id="remove">Remove</button>
    <button>Journal</button>

    </div>
    <div class="col-lg-6 col-md-6 col-sm-12" >
    <img src="${j.image}">
    </div>
    </div>
    </div>

    `
})
$('#current').append(curent);


var htmlText = data.map(function(o) {
    return `
        <div class="container">
        <div class="row">
        <div  class="col-lg-6 col-md-6 col-sm-12" data-aos="zoom-in" data-aos-duration="1000">
        <p class="p-name"> Name: ${o.name}</p>
        <p class="p-desc"> Gender: ${o.gender}</p>
        <p class="p-created"> Phone Number: ${o.phone}</p>
        <p class="p-created"> Address: ${o.address.city,o.address.street}</p>
        <button>Consult</button>        <button>More Info</button>
        </div>

        <div class="col-lg-6 col-md-6 col-sm-12">
        <img src="${o.image}">
        </div>
       </div>
       </div>
       
    `;
});

$('#wow').append(htmlText);