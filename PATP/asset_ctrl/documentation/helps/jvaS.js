class MenuBars {
    constructor(menuBar, navList, navLinks) {
        this.menuBar = document.querySelector(menuBar);
        this.navList = document.querySelector(navList);
        this.navLinks = document.querySelector(navLinks);
        this.activeClass = "active";
        
        this.handleClick = this.handleClick.bind(this);
    }

    animateLinks() {
        this.navLinks.forEach((link) => {
            link.style.animation
                ? (link.style.animation = "")
                : (link.style.animation = "navLinkFade 0.5s ease forwards 0.3s");
        });
    }
    
    handleClick() {
        this.navList.classList.toggle(this.activeClass);
        this.animateLinks();
    }    
    

    addClickEvent() {
        this.menuBar.addEventListener("click", this.handleClick);
    }

    init() {
        if (this.menuBar) {
            this.addClickEvent();
        }
        return this;
    }  
}

const menuBars = new MenuBars(
    ".menu-bar",
    ".nav-list",
    ".nav-list li"
);

menuBars.init();
