function rangeColor(input) {
  var wrp = document.createElement('div'),
    preBar = document.createElement('p'),
    min = parseInt(input.min, 10),
    max = parseInt(input.max, 10),
    range = max - min,
    getVal = function() {
      var w = parseInt(input.clientWidth, 10),
        t = ~~(w * (parseInt(input.value, 10) - min) / range);
      return t;
    };
  wrp.className = 'barCnt';
  preBar.className = 'preBar';

  input.className = input.className.length ? (input.className + ' colorized') : 'colorized';
  input.parentNode.replaceChild(wrp, input);

  wrp.appendChild(input);
  wrp.appendChild(preBar);



  input.addEventListener('input', function() {

    preBar.style.width = getVal() + 'px';
  });

  preBar.style.width = getVal() + 'px';
}


rangeColor(document.getElementById('slider'))