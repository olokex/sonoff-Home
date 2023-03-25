const template = document.createElement("template");
template.innerHTML = `
<style>
.button-panel {
   display: flex;
   flex-direction: column;
   justify-content: center;
   align-items: center;
   border: 20px solid #f38e6e;
   border-radius: 20px;
   padding: 30px;
   position: relative;
   width: 20em;
   height: 10em;
 }
 
 .panel-title {
   font-family: sans-serif;
   position: absolute;
   top: -25px;
   left: 50%;
   transform: translateX(-50%);
   margin: 0px;
   padding: 0 15px;
   font-size: 24px;
   color: white;
   font-weight: bold;
   text-align: center;
   background-color: #3c3c3c;
 }
 
 .button-group {
   display: flex;
   justify-content: space-evenly;
   width: 100%;
 }
 
 .google-icon {
   display: flex;
   justify-content: center;
   align-items: center;
   color: black;
   background-color: white;
   border: 5px #f38e6e solid;
   border-radius: 15px;
   width: 10em;
   height: 10em;
   cursor: pointer;
   margin: 1.3em;
   <!--transition: background-color 0.3s ease;-->
 }
.material-symbols-outlined {
   font-size: 7em;         
}

.material-symbols-outlined {
   font-variation-settings:
   'FILL' 0,
   'wght' 700,
   'GRAD' 0,
   'opsz' 48;
 }

.google-icon:hover {
   background-color: #ba684e;
}

.google-icon.active {
   background-color: #ba684e;
}

.google-icon:active {
   background-color: #752e17;
   border-color: black;
 }

.content{
   width: 400px;
}

.disable-selection {
    -webkit-user-select: none; /* Safari */
    -moz-user-select: none; /* Firefox */
    -ms-user-select: none; /* IE10+/Edge */
    user-select: none; /* Standard */
}
</style>


    <div class="button-panel">
    <h2 class="panel-title">title</h2>
    <div class="button-group">
        <button class="google-icon disable-selection"><i class="material-symbols-outlined" id="rightButton">icon</i></button>
        <button class="google-icon disable-selection"><i class="material-symbols-outlined" id="leftButton">icon</i></button>
    </div>
    </div>

`;

class SunblindButton extends HTMLElement {
    constructor() {
        super();
        const shadowRoot = this.attachShadow({mode: "closed" });
        
        const link = document.createElement('link');
        link.rel = 'stylesheet';
        link.href = 'https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200';

        shadowRoot.appendChild(link);
        
        let clone = template.content.cloneNode(true);
        shadowRoot.append(clone);
        const panel_title = shadowRoot.querySelector(".panel-title");
        panel_title.textContent = this.title.toUpperCase();

        const rightButton = shadowRoot.querySelector("#rightButton");
        const leftButton = shadowRoot.querySelector("#leftButton");

        rightButton.textContent = this.icon_right;
        leftButton.textContent = this.icon_left;

        const isMobile = /Mobile/.test(navigator.userAgent);
        console.log(isMobile);


        const eventDown = isMobile ? 'touchstart' : 'mousedown';
        const eventUp = isMobile ? 'touchend' : 'mouseup';

        leftButton.addEventListener(eventDown, () => {
            fetch(`/${this.device_id}/rotate_left`);
        });
        
        leftButton.addEventListener(eventUp, () => {
            fetch(`/${this.device_id}/stop_rotate`);
        });

        rightButton.addEventListener(eventDown, () => {
            fetch(`/${this.device_id}/rotate_right`);
        });
        
        rightButton.addEventListener(eventUp, () => {
            fetch(`/${this.device_id}/stop_rotate`);
        });

    }

    static get observedAttributes() {
        return ["title", "device-id", "icon-left", "icon-right"];
    }

    get title() {
        return this.getAttribute("title");
    }

    get icon_left() {
        return this.getAttribute("icon-left");
    }
    
    get icon_right() {
        return this.getAttribute("icon-right");
    }

    get device_id() {
        return this.getAttribute("device-id");
    }
}

customElements.define("sunblind-button", SunblindButton);