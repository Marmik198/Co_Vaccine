$(window).on('load', function () {
    $("#clients-elements").owlCarousel({
        items: 5,
        autoplay: true,
        loop: true,
        margin: 100,
        smartSpeed: 700,
        dots: false,
        responsive: {
            0: {
                items: 2
            },
            480: {
                items: 3
            },
            768: {
                items: 5
            }
        }
    });
});

$(function () {

    showHideNav();

    $("#back-to-top").fadeOut();



    $(window).scroll(function () {

        showHideNav();

    });



    function showHideNav() {

        if ($(window).scrollTop() > 50) {

            $("nav").addClass("scrolled-navbar blue-nav-top");

            $(".nav li.rs a").addClass("hr");

            $(".site-nav-wrapper").css("padding", "0px");

            $("#back-to-top").fadeIn();

        } else {

            $("nav").removeClass("scrolled-navbar blue-nav-top");

            $(".nav li.rs a").removeClass("hr");

            $(".site-nav-wrapper").css("padding", "20px 0");

            $("#back-to-top").fadeOut();

        }

    }



    $("#mobile-nav-open-btn").click(function () {

        $("#mobile-nav").css("height", "100%");

    });



    $("#mobile-nav-close-btn, #mobile-nav a").click(function () {

        $("#mobile-nav").css("height", "0%");

    });



    $("a.smooth-scroll").click(function (event) {
        event.preventDefault();

        var section_id = $(this).attr("href");

        $("html, body").animate({

            scrollTop: $(section_id).offset().top + 30

        }, 1250, "easeInOutExpo")

    });

});

//let zipcode_form = $("#zipcode-form");
//zipcode_form.submit(function () {
//    if ($("#zipcode-input").val().length == 0) {
//        alert("Enter ZipCode!");
//    }
//    zip_lat_lon($("#zipcode-input").val())
//        .then(data => {
//            console.log(data);
//        })
//        .catch(err => console.warn(err));
//    return false;
//});
//
//async function zip_lat_lon(data) {
//    const base = "https://thezipcodes.com/api/v1/search/?zipCode=";
//    let query = data + "&apiKey=bf8f48ae396223e53445f0ebabda6302";
//    const url = base + query;
//    let response = await fetch(url, {
//        mode: 'cors'
//    });
//    console.log(response);
//    if (response.ok) {
//        const result = await response.json();
//        return result;
//    } else {
//        await Promise.reject(new Error("Status Code: " + response.status));
//    }
//}

const get = async (country, yes1, yes2, yes3) => {
    const base = "https://disease.sh/v3/covid-19/countries/";
    let query = "";
    if (yes1) {
        query = `${country}?strict=true`;
    } else if (yes2) {
        query = `${country}?yesterday=${yes2}&strict=true`;
    } else if (yes3) {
        query = `${country}?twoDaysAgo=${yes3}&strict=true`;
    }
    const url = base + query;
    const response = await fetch(url);
    if (response.ok) {
        const data = await response.json();
        return data;
    } else {
        await Promise.reject(new Error("Status Code: " + response.status));
    }
}

const form = document.querySelector("#country-form");
$("#country-form").submit(function (e) {
    e.preventDefault();
    let countryName = form.country.value.trim();
    form.country.value = "";
    get(countryName, true, false, false)
        .then(data => {
            flag(data);
            todayUI(data);
        })
        .catch(err => console.warn(err));
    get(countryName, false, true, false)
        .then(data => {
            yesterdayUI(data);
        })
        .catch(err => console.warn(err));
});

function flag(data) {
    $(".result .col-md-12").html(`<h1>${data.country}</h1><img src=${data.countryInfo.flag}>`);
}

function todayUI(data) {
    let todayData = $(".today-data")[0];
    todayData.innerHTML = `<h3>Today Data</h3>
                            <p>Cases: ${data.todayCases}</p>
                            <p>TotalCases: ${data.cases}</p>
                            <p>Deaths: ${data.todayDeaths}</p>
                            <p>TotalDeaths: ${data.deaths}</p>
                            <p>Recovered: ${data.recovered}</p>
                            <p>TotalRecovered: ${data.todayRecovered}</p>
                            <p>Active: ${data.active}</p>`;
}

function yesterdayUI(data) {
    let todayData = $(".yesterday-data")[0];
    todayData.innerHTML = `<h3>Yesterday Data</h3>
                            <p>Cases: ${data.todayCases}</p>
                            <p>TotalCases: ${data.cases}</p>
                            <p>Deaths: ${data.todayDeaths}</p>
                            <p>TotalDeaths: ${data.deaths}</p>
                            <p>Recovered: ${data.recovered}</p>
                            <p>TotalRecovered: ${data.todayRecovered}</p>
                            <p>Active: ${data.active}</p>`;
}
