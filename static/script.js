setInterval(async () => {
   console.log('checking...');
   let res = await fetch(location.href);
   let text = await res.text();
   let el = document.createElement('html');
   el.innerHTML = text;
   if (document.querySelector('.content').innerHTML != el.querySelector('.content').innerHTML) {
      console.log('changed');
      document.querySelector('.content').innerHTML = el.querySelector('.content').innerHTML;
   }
}, 2000);