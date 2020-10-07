// GSAP

gsap.from(".logo", {duration: 2, opacity: 0});

const timeline = gsap.timeline();

timeline
.from(".quick-links", {duration: 1, y: "100%", opacity:0})
.from("nav", {duration: 0.5, y: "100%", opacity:0})
.from(".action-btn", {duration: 0.5, y: "100%", opacity:0})
.from(".intro-img", {duration: 0.5, y: "100%", opacity:0})
.from(".about-p", {duration: 0.5, y: "10%", opacity:0}, "-=0.5")
.from(".location", {duration: 0.5, y: "10%", opacity:0}, "-=1")
.from(".services", {duration: 0.5, y: "10%", opacity:0}, "-=0.5")


const tl_about = gsap.timeline({
  scrollTrigger: {
    trigger: ".content",
    start: "bottom bottom"
  }
});

tl_about
.from(".content", {duration: 0.5, y: "30%", opacity:0})

$("#footer i").click(function(){
  gsap.to(window, {duration: 2, scrollTo: {y: "#intro", offsetY: 50}, ease: "power3.inOut"});
})

$(".menu-toggle").click(function(){
  $("#main-nav").toggleClass("active");
})
