// Week1 advanced
// Add the drop down function to the hamburger icon

// When click the icon => add the show class into icon"s class list
function clickToAddShow(){
    const eDropDown = document.getElementsByClassName("drop_down");
    for (let i = 0; i < eDropDown.length; i++) {
        eDropDown.item(i).classList.add("show");
    }
}


// When click on the region outside the drop down list => remove the show class from icon"s class list
function clickToRemoveShow(){
    window.onclick = function(event) {
        if (!event.target.matches(".menu_text") && 
            !event.target.matches(".menu_text_item") &&
            !event.target.matches(".size_figure") && 
            !event.target.matches(".menu_figure")
        )
        {
            const eDropDown = document.getElementsByClassName("drop_down");
            for (let i = 0; i < eDropDown.length; i++) {
                if (eDropDown.item(i).classList.contains("show")) {
                    eDropDown.item(i).classList.remove("show");
                }
            }
        }
    }
}

// Week3
// fetch images and append these on the block
let titleList = []
let imgUrlList = []
let globalIter = 0;
const numPromot = 3;
const eachRowTitle = 12;
function preFetchAndAppendImages(){
    let url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";
    // Get the image url from the url json

    // Use create element to create img and append img to the element => document.createElement() and appendChild()
    // Should keep the original layout format

    // Fetch the url and get the response
    // Use response to get json format dataJSON
    // Process
    
    fetch(url)
        .then((response) => {
            return response.json()
        })
        .then(
            (dataJSON) => {
                let attractions = dataJSON["result"]["results"];
                for(const val of attractions){
                    let title = val["stitle"];
                    let imgUrl = String(val["file"]).toLowerCase().split(".jpg")[0] + ".jpg";
                    titleList.push(title)
                    imgUrlList.push(imgUrl);
                }

                // Append Promotion 1~3
                // [0, 3)
                const eRow1ImgSeting = document.getElementsByClassName("figure_row1_img_setting");
                const eRow1Prmt = document.getElementsByClassName("figure_row1_prmt");
                for(globalIter=0 ; globalIter<numPromot ; globalIter++){
                    // Image src
                    let img = document.createElement("img");
                    img.src = imgUrlList[globalIter];
                    img.width = 80;
                    img.height = 50;
                    eRow1ImgSeting.item(globalIter).appendChild(img);
                    // Image title
                    let div = document.createElement("div");
                    div.textContent = titleList[globalIter];
                    eRow1Prmt.item(globalIter).appendChild(div);
                }
                // Append Title for first 12
                // [3, 3+12)
                const eRow2Title = document.getElementsByClassName("figure_row2_title");
                for( ; globalIter<numPromot+eachRowTitle ; globalIter++){
                    // Image src
                    let divImgSetting = document.createElement("div");
                    divImgSetting.classList.add("figure_row2_img_setting");
                    let img = document.createElement("img");
                    img.src = imgUrlList[globalIter];
                    img.setAttribute("width", "100%");
                    img.setAttribute("height", "100%");
                    // img.setAttribute("object-fit", "contain");
                    divImgSetting.appendChild(img);
                    eRow2Title.item(globalIter-numPromot).appendChild(divImgSetting);
                    // Image title
                    let divTitle = document.createElement("div");
                    divTitle.classList.add("figure_row2_txt");
                    divTitle.textContent = titleList[globalIter];
                    eRow2Title.item(globalIter-numPromot).appendChild(divTitle);
                }
            }
        )
}

async function loadMoreImg(){
    const eRow2 = document.getElementsByClassName("figure_row2");
    for(let i=0 ; i<eachRowTitle ; i++){
        if(i+globalIter >= imgUrlList.length){
            globalIter += i;
            break;
        }
        // Create figure row2 title
        let divRow2Title = document.createElement("div");
        divRow2Title.classList.add("figure_row2_title");
        // Image src
        let divImgSetting = document.createElement("div");
        divImgSetting.classList.add("figure_row2_img_setting");
        let img = document.createElement("img");
        img.src = imgUrlList[i+globalIter];
        img.setAttribute("width", "100%");
        img.setAttribute("height", "100%");
        // img.setAttribute("object-fit", "contain");
        divImgSetting.appendChild(img);
        divRow2Title.appendChild(divImgSetting);
        // Image title
        let divTitle = document.createElement("div");
        divTitle.classList.add("figure_row2_txt");
        divTitle.textContent = titleList[i+globalIter];
        divRow2Title.appendChild(divTitle);
        // Append to the figure row2
        eRow2.item(0).appendChild(divRow2Title);
    }
    globalIter += eachRowTitle;
}

clickToRemoveShow();
preFetchAndAppendImages();