const Carousel = {
  slides: document.querySelectorAll('#imgs .image-slide'),
  track: document.getElementById('imgs'),
  leftBtn: document.getElementById('left'),
  rightBtn: document.getElementById('right'),
  index: 0,
  interval: null,
  intervalTime: 4000,
  get slidesPerView() {
    if (window.innerWidth >= 1100) return 3;
    if (window.innerWidth >= 700) return 2;
    return 1;
  },
  changeImage() {
    const maxIndex = Math.max(0, this.slides.length - this.slidesPerView);
    if (this.index > maxIndex) this.index = 0;
    if (this.index < 0) this.index = maxIndex;
    const offset = (100 / this.slidesPerView) * this.index;
    this.track.style.transform = `translateX(-${offset}%)`;
  },
  next(step = 1) {
    this.index += step;
    this.changeImage();
    this.resetInterval();
  },
  prev() {
    this.index -= 1;
    this.changeImage();
    this.resetInterval();
  },
  resetInterval() {
    clearInterval(this.interval);
    this.interval = setInterval(() => this.next(), this.intervalTime);
  },
  init() {
    if (!this.track) return;
    this.interval = setInterval(() => this.next(), this.intervalTime);
    this.leftBtn?.addEventListener('click', () => this.prev());
    this.rightBtn?.addEventListener('click', () => this.next());
    window.addEventListener('resize', () => this.changeImage());
  },
};

Carousel.init();
