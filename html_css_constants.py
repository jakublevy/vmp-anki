front_template = """
    <div class="wrapper rounded shadow">
        <div class="foreign">
            <span>{{question}}</span>
        </div>

        <div class="questionNumber">
            <span>{{question_num}}</span>
        </div>

        <figure class="img">{{question_img}}</figure>

        <div class="native">a) {{a}}</div>
        <figure class="img">{{a_img}}</figure>

        <div class="native">b) {{b}}</div>
        <figure class="img">{{b_img}}</figure>

        <div class="native">c) {{c}}</div>
        <figure class="img">{{c_img}}</figure>
    </div>	
    <span id="correct" style="display: none">{{correct}}</span>
    <script>
    function getRndInteger(min, max) {
        return Math.floor(Math.random() * (max - min) ) + min;
    }

    const answers = [...document.getElementsByClassName('native')]
    let images = [...document.getElementsByClassName('img')]
    const parent = images[images.length - 1].parentNode
    images = images.slice(1)
    const correctIdx = parseInt(document.getElementById('correct').textContent)

    answers.forEach(x=>x.remove())
    images.forEach(x=>x.remove())

    const order = [0,1,2]
    let neworder = []
    for(let i = 0; i < 3; ++i) {
        const pos = getRndInteger(0, 3-i)
        neworder.push(order[pos])
        order.splice(pos, 1)
    }
    
    let arr = []
    let correct = false
    for(let i = 0; i < answers.length; ++i) {
        if(i == correctIdx)
            correct = true
        else
            correct = false
        
        const new_idx = neworder[i]
        arr.splice(new_idx, 0, [answers[i], images[i], correct])
    }

    localStorage.setItem('_my_order', JSON.stringify(neworder))
    localStorage.setItem('_correct_idx', JSON.stringify(correctIdx))


    let charCode = 97;
    for(let i = 0; i < arr.length; ++i) {
        let element = arr[i][0]
        element.textContent = element.textContent.replace(element.textContent[0], String.fromCharCode(charCode))
        parent.appendChild(element)
        parent.appendChild(arr[i][1])
        ++charCode
    }
</script>
    """

back_template = """
 <div id="wrapper-w" class="wrapper rounded shadow">
        <div class="foreign">
            <span>{{question}}</span>
        </div>

        <div class="questionNumber">
            <span>{{question_num}}</span>
        </div>

        <figure class="back-i img">{{question_img}}</figure>

        <div class="back-t native">a) {{a}}</div>
        <figure class="back-i img">{{a_img}}</figure>

        <div class="back-t native">b) {{b}}</div>
        <figure class="back-i img">{{b_img}}</figure>

        <div class="back-t native">c) {{c}}</div>
        <figure class="back-i img">{{c_img}}</figure>
    </div>	
    <script>
    const neworderr = JSON.parse(localStorage.getItem('_my_order'))
    const correctIdxAfterShufflee = JSON.parse(localStorage.getItem('_correct_idx'))
    const answerss = [...document.getElementsByClassName('back-t')]
    let imagess = [...document.getElementsByClassName('back-i')]
    const parentt = document.getElementById('wrapper-w');
    imagess = imagess.slice(1)
    answerss.forEach(x=>x.remove())
    imagess.forEach(x=>x.remove())
    let arrr = [];
    let correctt = false;
    for(let i = 0; i < answerss.length; ++i) {
        if(i == correctIdxAfterShufflee)
            correctt = true
        else
            correctt = false
        
        const new_idxx = neworderr[i]
        arrr.splice(new_idxx, 0, [answerss[i], imagess[i], correctt])
    }
    let charCodee = 97;
    for(let i = 0; i < arrr.length; ++i) {
        let elementt = arrr[i][0]
        elementt.textContent = elementt.textContent.replace(elementt.textContent[0], String.fromCharCode(charCodee))
        if(!arrr[i][2]) {
            elementt.style.visibility = 'hidden'
            arrr[i][1].style.visibility = 'hidden'
        }
        parentt.appendChild(elementt)
        parentt.appendChild(arrr[i][1])
        ++charCodee
    }
    </script>
    """

styling = """
    .img img,
    .shadow {
      box-shadow: 5px 6px 5px 0px rgba(0,0,0,0.68); 
     }
    body { /* Hack to display background img on ankiuser.net */
      background-color: unset;
    }

    #backgroundImg {
    /*.card:after {*/

      content: ' ';
      display: block;
      position: absolute;
      left: 0;
      top: 0;
      overflow: hidden;
      width: 99%;
      height: 97%;
      z-index: -1;
      opacity: 0.8;  
      background-repeat: no-repeat;
      background-position: 50% 0;
      -ms-background-size: cover;
      -o-background-size: cover;
      -moz-background-size: cover;
      -webkit-background-size: cover;
      background-size: cover;

    }

    .card {
      background-color: transparent;
      position: unset;
    }

     .wrapper {
       padding: 10px;
       margin: 10px;
       display: -webkit-box;
       display: -webkit-flex;
       display: -ms-flexbox;
       display: flex;	
       -webkit-flex-flow: row wrap;	
           -ms-flex-flow: row wrap;	
               flex-flow: row wrap;
       -webkit-box-align: center;
       -webkit-align-items: center;
           -ms-flex-align: center;
               align-items: center;
       /*background-color: #d0d0d0e0; */
        background-color: #000;
       color: #fff;
       font-family: Helvetica;
       font-size: 1.5em;
       font-weight: bold;
       line-height: 26px;
       text-align: left;
    /*   text-shadow: 2px 2px 3px  #121f1fee, -1px 0 10px #ffffffaf;    */
     }

    .img {
     text-align: center;
    }

     .wrapper > * {
       -webkit-box-flex: 1;
       -webkit-flex: 1 100%;
           -ms-flex: 1 100%;
               flex: 1 100%;

       margin: 5px;

     }


     .foreign {  
      /* color:rgb(255, 50, 50); */
      color:#CCCCCC;
      z-index: 1;   
     }

     .native {   
     /*  color:rgb(50, 255, 50); */
        color: goldenrod;
     }

     .rounded {
       border-radius: 18px;
       -moz-border-radius: 18px;
       -webkit-border-radius: 18px;
       border: 0px solid #000000;   
     }


     .questionNumber {    
         position: absolute;
         right: 40px;
         top: 40px;
       }

     @media all and (max-height: 400px) {

       .img img {
        width: 20%;
       }
      .wrapper, #hintButton {
        font-size: 80%;    
        line-height: 16px;
      }

     }


     @media all and (min-width: 400px) {
       .native1, .native2 {
         -webkit-box-flex: 1;
         -webkit-flex: 1 auto;
             -ms-flex: 1 auto;
                 flex: 1 auto;  
       /*  background-color: #ff0040e8; */
       } 
 }
    """