
// menu-bar-btn section---------------------------------------------


const menu_bar_btn=document.querySelector('.fa-bars')

menu_bar_btn.addEventListener("click", function (ev){
    let menu_bar_page=document.querySelector('.menu-bar')
    menu_bar_page.style.display="flex"
    menu_bar_page.style.width="40%"

    let close_btn=document.querySelector('.fa-close')
    close_btn.addEventListener("click", function (ev){
        menu_bar_page.style.display="none"
        menu_bar_page.style.width="0"
    })
})