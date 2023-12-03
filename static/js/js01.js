var imgs = document.querySelectorAll("section>ul>li")//获取图片盒子——结果为数组
console.log(imgs)
var len =imgs.length//图片数量

var current =0//初始主图片下标
var timer//定时器的返回值

change()
bind()
autoplay()

//改变主图片函数
function change(){
    //将图片分为左右两边两组——每组数量
    var mlen = Math.floor(len/2)
    for (var i=0;i<mlen;i++){
        //获取主图片左右两边的图片的下标
        //注：当图片数为偶数时会出现一个limg=rimg的情况
        var limg =len+current-i-1
        var rimg =current+i+1
        if (limg>=len){
            limg-=len
        }
        if (rimg>=len){
            rimg-=len
        }

        //给主图片左右两边的图片设置transform
        if (rimg!=limg){
            imgs[limg].style.transform= `translateX(`+(-200)*(i+1)+`px) translateZ(`+(200-i*100)+`px) rotateY(30deg) scale(`+(1-(0.1*(i+1)))+`)`
            imgs[rimg].style.transform = `translateX(`+(200)*(i+1)+`px) translateZ(`+(200-i*100)+`px) rotateY(-30deg) scale(`+(1-(0.1*(i+1)))+`)`
        }
        else {
            //给当rimg=limg这种特殊情况下的transform
            imgs[limg].style.transform = `translateZ(0px)`
        }
        //设置主图片的transform
        imgs[current].style.transform = `translateZ(300px)`

    }
}

//设置绑定
function bind(){
    //获取点击图片的下标——并赋值给current（主图片下标）然后调用change函数
    for (var i=0;i<len;i++){
        (function (i) {
            imgs[i].onclick=function () {
                current = i;
                change();
            }
        })(i);
        //当鼠标移入图片时定时器停止
        imgs[i].onmouseenter=function () {
            clearInterval(timer);
        }
        //当鼠标移除图片时开启定时器——autoplay是下面封装定时器的函数
        imgs[i].onmouseout = function () {
            autoplay();
        }
    }
}
//封装定时器
function autoplay() {
    timer = setInterval(function () {
        if(current>=len-1){
            current=0;
        }else {
            current++;
        }
        change();
    },2000)
}