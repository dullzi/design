
var cur=0;
function updateSlider(){
  document.getElementById('slides').style.transform='translateX(-'+cur*100+'%)';
  document.querySelectorAll('.dot').forEach(function(d,i){d.classList.toggle('active',i===cur)});
  document.getElementById('curSlide').textContent=cur+1;
}
function nextSlide(){cur=(cur+1)%3;updateSlider()}
function prevSlide(){cur=(cur+2)%3;updateSlider()}
function goSlide(i){cur=i;updateSlider()}
setInterval(function(){nextSlide()},5000);

function toggleSidebar(){
  document.getElementById('sidebar').classList.toggle('open');
  document.getElementById('overlay').classList.toggle('open');
}

function scrollCarousel(id,dir){
  var el=document.getElementById(id);
  if(el) el.scrollLeft+=dir*240;
}

var h=5,m=43,s=21;
function tick(){
  s--;if(s<0){s=59;m--;if(m<0){m=59;h--;if(h<0){h=0;m=0;s=0}}}
  function fmt(n){return n<10?'0'+n:n}
  document.getElementById('cdH').textContent=fmt(h);
  document.getElementById('cdM').textContent=fmt(m);
  document.getElementById('cdS').textContent=fmt(s);
}
setInterval(tick,1000);


document.addEventListener('DOMContentLoaded',()=>{
 if(window.gsap){
   gsap.registerPlugin(ScrollTrigger);

   gsap.from('nav',{y:-80,opacity:0,duration:1});
   gsap.from('.slide-title',{y:80,opacity:0,duration:1.2,stagger:.15});
   gsap.from('.slide-desc',{y:40,opacity:0,duration:1,delay:.3});

   gsap.utils.toArray('.prod-card,.cat-card,.benefit-item').forEach(el=>{
      gsap.from(el,{
        scrollTrigger:{trigger:el,start:'top 85%'},
        y:40,opacity:0,duration:.8
      });
   });
 }

 window.addEventListener('scroll',()=>{
   const nav=document.querySelector('nav');
   if(!nav) return;
   nav.style.boxShadow=window.scrollY>50?'0 10px 30px rgba(0,0,0,.08)':'0 4px 20px rgba(0,0,0,.05)';
 });
});
