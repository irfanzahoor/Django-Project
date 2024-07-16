AOS.init();

document.addEventListener("DOMContentLoaded", function () {
  var lazyImages = document.querySelectorAll(".lazy-load");

  var options = {
    threshold: 0.5, // Adjust threshold as needed
  };

  var lazyLoad = function (entries, observer) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        var img = entry.target;
        img.src = img.dataset.src;
        img.classList.add("fade-in");
        img.classList.remove("lazy-load");
        observer.unobserve(img);
      }
    });
  };

  var observer = new IntersectionObserver(lazyLoad, options);

  lazyImages.forEach(function (img) {
    observer.observe(img);
  });
});

(function () {
  var counter = 0;
  var c = 0;

  var i = setInterval(function () {
    var counterElement = document.querySelector(
      ".loading-page .counter .count"
    );
    var progressBar = document.querySelector(
      ".loading-page .counter .load-progress"
    );

    counterElement.innerHTML = c + "%";
    progressBar.style.width = c + "%";

    counter++;
    c++;

    if (counter == 101) {
      clearInterval(i);
      Loader();
    }
  }, 10);

  function Loader() {
    // Hide the loader smoothly
    var loader = document.querySelector(".loading-page");
    loader.style.opacity = 0; // Set opacity to 0
    setTimeout(function () {
      loader.style.display = "none"; // After the transition, hide the loader
    }, 500); // Adjust the timeout to match the transition duration (0.5s)
  }

  // Add an event listener for when the page finishes loading
  window.onload = function () {
    Loader();
  };
})();

window.onscroll = function () {
  let position = 20;
  if (
    document.body.scrollTop > position ||
    document.documentElement.scrollTop > position
  ) {
    document.getElementById("navbar").classList.add("navbar-scroll");
  } else {
    document.getElementById("navbar").classList.remove("navbar-scroll");
  }
};

document.body.addEventListener("click", function (e) {
  const target = e.target;
  const body = document.querySelector("body");
  const html = document.querySelector("html");
  if (target.matches('[data-nxt-toggle="collapse"]')) {
    let collapseItem = target.parentElement;
    let collapsible = collapseItem.parentElement;
    let items = collapsible.querySelectorAll(".collapse-item");

    items.forEach((el) => {
      if (el == collapseItem) {
        el.classList.toggle("active");
      } else {
        el.classList.remove("active");
      }
    });
  } else if (target.matches(".menu-btn")) {
    const sidebar = document.getElementById("sidebar");
    if (sidebar.classList.contains("active")) {
      sidebar.classList.remove("active");
      html.style.overflowY = "auto";
      body.style.overflowY = "auto";
    } else {
      sidebar.classList.add("active");
      body.style.overflowY = "hidden";
      html.style.overflowY = "hidden";
    }
  }
});
