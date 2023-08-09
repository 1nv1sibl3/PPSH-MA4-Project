const Carousel = {
    img: document.querySelectorAll('#imgs .image-slide'),
    imgs: document.getElementById('imgs'),
    leftBtn: document.getElementById('left'),
    rightBtn: document.getElementById('right'),
    index: 0,
    interval: '',
    intervalTime: 2000,
    run() {
      Carousel.index++;
      Carousel.changeImage();
    },
    slide(direction) {
      direction ? Carousel.index++ : Carousel.index--;
      Carousel.changeImage();
      Carousel.resetInterval();
    },
    resetInterval() {
      clearInterval(Carousel.interval);
      Carousel.interval = setInterval(Carousel.run, Carousel.intervalTime);
    },
    changeImage() {
      if (Carousel.index > Carousel.img.length - 1) {
        Carousel.index = 0;
      } else if (Carousel.index < 0) {
        Carousel.index = Carousel.img.length - 1;
      }
      Carousel.imgs.style.transform = `translateX(${-Carousel.index * 16.666}% )`;
    },
    start() {
      Carousel.interval = setInterval(Carousel.run, Carousel.intervalTime);
      Carousel.leftBtn.addEventListener('click', () => Carousel.slide(false));
      Carousel.rightBtn.addEventListener('click', () => Carousel.slide(true));
    },
  };
  
  Carousel.start();
  